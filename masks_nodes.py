import numpy as np
import scipy.ndimage as ndi
import torch

class BodyPartSelectorMask:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask": ("MASK",),
                "selection": (["head", "hands", "feet"],),
            }
        }
    
    RETURN_TYPES = ("MASK",)
    FUNCTION = "process"
    CATEGORY = "Bjornulf"

    def process_single(self, mask_np, selection):
        """
        Process a single 2D mask to select head, hands, or feet based on position.
        
        Args:
            mask_np: 2D numpy array (H, W)
            selection: str, one of "head", "hands", "feet"
        
        Returns:
            2D numpy array with selected shapes
        """
        # Convert to binary mask
        binary_mask = (mask_np > 0.5).astype(np.uint8)
        
        # Label connected components
        labeled_array, num_features = ndi.label(binary_mask)
        if num_features < 5:
            raise ValueError(f"Expected at least 5 components, found {num_features}")
        
        # Compute sizes of all components (excluding background)
        sizes = np.bincount(labeled_array.ravel())[1:]
        # Select the five largest components
        largest_indices = np.argsort(sizes)[-5:][::-1]  # Top 5 in descending order
        largest_labels = largest_indices + 1  # Map to label numbers (1-based)
        
        # Compute centroids for the five largest components
        centroids = []
        for label in largest_labels:
            positions = np.argwhere(labeled_array == label)
            if len(positions) > 0:
                centroid_row = positions[:, 0].mean()  # Average row
                centroid_col = positions[:, 1].mean()  # Average column
                centroids.append((label, centroid_row, centroid_col))
        
        # Sort by centroid row (ascending, since row 0 is top)
        centroids.sort(key=lambda x: x[1])
        
        # Assign components based on vertical position
        head_label = centroids[0][0]          # Smallest row (top)
        hand_labels = [centroids[1][0], centroids[2][0]]  # Middle two
        feet_labels = [centroids[3][0], centroids[4][0]]  # Largest rows (bottom)
        
        # Select labels based on user input
        if selection == "head":
            selected_labels = [head_label]
        elif selection == "hands":
            selected_labels = hand_labels
        elif selection == "feet":
            selected_labels = feet_labels
        else:
            raise ValueError("Selection must be 'head', 'hands', or 'feet'")
        
        # Create new mask with selected components
        new_mask = np.isin(labeled_array, selected_labels).astype(np.float32)
        return new_mask

    def process(self, mask, selection):
        """
        Process the input mask(s) and return a new mask with selected parts.
        
        Args:
            mask: torch tensor, either 2D (H, W) or 3D (N, H, W)
            selection: str, one of "head", "hands", "feet"
        
        Returns:
            Tuple containing the output mask tensor
        """
        mask_np = mask.cpu().numpy()
        
        if mask_np.ndim == 2:
            # Single mask
            result = self.process_single(mask_np, selection)
            result = result[None, ...]  # Add batch dimension: (1, H, W)
        elif mask_np.ndim == 3:
            # Batched masks
            results = [self.process_single(mask_np[i], selection) 
                      for i in range(mask_np.shape[0])]
            result = np.stack(results, axis=0)  # Stack to (N, H, W)
        else:
            raise ValueError("Mask must be 2D (H, W) or 3D (N, H, W)")
        
        return (torch.from_numpy(result),)
class LargestMaskOnly:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask": ("MASK",),
                "num_masks": ("INT", {"default": 1, "min": 1, "max": 10}),
            }
        }
    
    RETURN_TYPES = ("MASK",)
    FUNCTION = "process"
    CATEGORY = "Bjornulf"

    def process_single(self, mask_np, num_masks):
        """Process a single mask to keep the top num_masks largest components."""
        # Convert to binary mask
        binary_mask = (mask_np > 0.5).astype(np.uint8)
        # Label connected components
        labeled_array, num_features = ndi.label(binary_mask)
        
        if num_features > 0:
            # Get sizes of all components, excluding background (label 0)
            sizes = np.bincount(labeled_array.ravel())[1:]
            # Determine how many components to keep
            k = min(num_masks, num_features)
            if k > 0:
                # Get indices of the top k largest components (descending order)
                top_indices = np.argsort(sizes)[::-1][:k]
                # Map indices to labels (add 1 since sizes[1:] starts at label 1)
                top_labels = top_indices + 1
                # Create mask with only the top k components
                largest_mask = np.isin(labeled_array, top_labels).astype(np.float32)
            else:
                largest_mask = np.zeros_like(binary_mask, dtype=np.float32)
        else:
            # No components found, return an empty mask
            largest_mask = np.zeros_like(binary_mask, dtype=np.float32)
        
        return largest_mask

    def process(self, mask, num_masks):
        """Process the input mask(s) and return the top num_masks largest components."""
        # Convert mask to numpy array
        mask_np = mask.cpu().numpy()
        
        if mask_np.ndim == 2:
            # Single mask: process and add batch dimension
            result = self.process_single(mask_np, num_masks)
            result = result[None, ...]  # Shape becomes (1, H, W)
        elif mask_np.ndim == 3:
            # Batched masks: process each mask independently
            results = [self.process_single(mask_np[i], num_masks) for i in range(mask_np.shape[0])]
            result = np.stack(results, axis=0)  # Shape remains (N, H, W)
        else:
            raise ValueError("Invalid mask shape: expected 2D (H, W) or 3D (N, H, W)")
        
        # Convert back to torch tensor and return as a tuple
        return (torch.from_numpy(result),)

class BoundingRectangleMask:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask": ("MASK",),
                "up": ("INT", {"default": 0, "min": -10000, "max": 10000}),
                "down": ("INT", {"default": 0, "min": -10000, "max": 10000}),
                "right": ("INT", {"default": 0, "min": -10000, "max": 10000}),
                "left": ("INT", {"default": 0, "min": -10000, "max": 10000}),
            }
        }
    
    RETURN_TYPES = ("MASK",)
    FUNCTION = "process"
    CATEGORY = "Bjornulf"

    def process_single(self, mask_np, up, down, right, left):
        active = mask_np > 0.5
        if not np.any(active):
            return np.zeros_like(mask_np, dtype=np.float32)
        
        rows_with_active = np.any(active, axis=1)
        cols_with_active = np.any(active, axis=0)
        min_row = np.where(rows_with_active)[0][0]
        max_row = np.where(rows_with_active)[0][-1]
        min_col = np.where(cols_with_active)[0][0]
        max_col = np.where(cols_with_active)[0][-1]
        
        min_row_adj = min_row - up
        max_row_adj = max_row + down
        min_col_adj = min_col - left
        max_col_adj = max_col + right
        
        H, W = mask_np.shape
        min_row_adj = max(0, min_row_adj)
        max_row_adj = min(H - 1, max_row_adj)
        min_col_adj = max(0, min_col_adj)
        max_col_adj = min(W - 1, max_col_adj)
        
        if min_row_adj > max_row_adj or min_col_adj > max_col_adj:
            return np.zeros_like(mask_np, dtype=np.float32)
        
        new_mask = np.zeros_like(mask_np, dtype=np.float32)
        new_mask[min_row_adj:max_row_adj + 1, min_col_adj:max_col_adj + 1] = 1.0
        return new_mask

    def process(self, mask, up, down, right, left):
        mask_np = mask.cpu().numpy()
        
        if mask_np.ndim == 2:
            result = self.process_single(mask_np, up, down, right, left)
            result = result[None, ...]
        elif mask_np.ndim == 3:
            results = [self.process_single(mask_np[i], up, down, right, left) 
                      for i in range(mask_np.shape[0])]
            result = np.stack(results, axis=0)
        else:
            raise ValueError("Mask must be 2D (H, W) or 3D (N, H, W)")
        
        return (torch.from_numpy(result),)

class BoundingRectangleMaskBlur:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask": ("MASK",),
                "up": ("INT", {"default": 0, "min": -10000, "max": 10000}),
                "down": ("INT", {"default": 0, "min": -10000, "max": 10000}),
                "right": ("INT", {"default": 0, "min": -10000, "max": 10000}),
                "left": ("INT", {"default": 0, "min": -10000, "max": 10000}),
                "blur_up": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 100.0, "step": 0.1}),
                "blur_down": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 100.0, "step": 0.1}),
                "blur_left": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 100.0, "step": 0.1}),
                "blur_right": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 100.0, "step": 0.1}),
                "tapered_corners": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("MASK",)
    FUNCTION = "process"
    CATEGORY = "Bjornulf"

    def _get_bounding_box(self, mask_np):
        """Extract bounding box coordinates from active mask pixels."""
        active = mask_np > 0.5
        if not np.any(active):
            return None
        
        rows_with_active = np.any(active, axis=1)
        cols_with_active = np.any(active, axis=0)
        
        min_row = np.where(rows_with_active)[0][0]
        max_row = np.where(rows_with_active)[0][-1]
        min_col = np.where(cols_with_active)[0][0]
        max_col = np.where(cols_with_active)[0][-1]
        
        return min_row, max_row, min_col, max_col

    def _expand_bounding_box(self, bbox, up, down, left, right, shape):
        """Expand bounding box by specified amounts, clamped to image bounds."""
        min_row, max_row, min_col, max_col = bbox
        H, W = shape
        
        min_row_adj = max(0, min_row - up)
        max_row_adj = min(H - 1, max_row + down)
        min_col_adj = max(0, min_col - left)
        max_col_adj = min(W - 1, max_col + right)
        
        # Check for invalid bounds
        if min_row_adj > max_row_adj or min_col_adj > max_col_adj:
            return None
            
        return min_row_adj, max_row_adj, min_col_adj, max_col_adj

    def _create_directional_blur_mask(self, mask, direction, blur_amount):
        """Create a mask blurred in one specific direction."""
        if blur_amount <= 0:
            return np.zeros_like(mask)
            
        H, W = mask.shape
        
        # Find the edge of the mask in the specified direction
        mask_binary = mask > 0.5
        if not np.any(mask_binary):
            return np.zeros_like(mask)
            
        # Create blur based on direction
        if direction == 'up':
            # Find top edge
            top_rows = np.any(mask_binary, axis=1)
            if not np.any(top_rows):
                return np.zeros_like(mask)
            top_edge = np.where(top_rows)[0][0]
            
            # Create gradient going upward from top edge
            result = np.zeros_like(mask)
            for row in range(top_edge + 1):
                distance = top_edge - row
                strength = np.exp(-(distance ** 2) / (2 * blur_amount ** 2))
                result[row, :] = strength * np.any(mask_binary[top_edge:, :], axis=0)
                
        elif direction == 'down':
            # Find bottom edge
            top_rows = np.any(mask_binary, axis=1)
            if not np.any(top_rows):
                return np.zeros_like(mask)
            bottom_edge = np.where(top_rows)[0][-1]
            
            # Create gradient going downward from bottom edge
            result = np.zeros_like(mask)
            for row in range(bottom_edge, H):
                distance = row - bottom_edge
                strength = np.exp(-(distance ** 2) / (2 * blur_amount ** 2))
                result[row, :] = strength * np.any(mask_binary[:bottom_edge+1, :], axis=0)
                
        elif direction == 'left':
            # Find left edge
            left_cols = np.any(mask_binary, axis=0)
            if not np.any(left_cols):
                return np.zeros_like(mask)
            left_edge = np.where(left_cols)[0][0]
            
            # Create gradient going leftward from left edge
            result = np.zeros_like(mask)
            for col in range(left_edge + 1):
                distance = left_edge - col
                strength = np.exp(-(distance ** 2) / (2 * blur_amount ** 2))
                result[:, col] = strength * np.any(mask_binary[:, left_edge:], axis=1)
                
        elif direction == 'right':
            # Find right edge
            left_cols = np.any(mask_binary, axis=0)
            if not np.any(left_cols):
                return np.zeros_like(mask)
            right_edge = np.where(left_cols)[0][-1]
            
            # Create gradient going rightward from right edge
            result = np.zeros_like(mask)
            for col in range(right_edge, W):
                distance = col - right_edge
                strength = np.exp(-(distance ** 2) / (2 * blur_amount ** 2))
                result[:, col] = strength * np.any(mask_binary[:, :right_edge+1], axis=1)
        
        return result

    def _create_corner_blend(self, mask, blur_up, blur_down, blur_left, blur_right):
        """Create smooth corner blending for diagonal blur combinations using individual blur values."""
        H, W = mask.shape
        result = np.zeros_like(mask)
        
        # Find mask boundaries
        mask_binary = mask > 0.5
        if not np.any(mask_binary):
            return result
            
        rows_with_mask = np.any(mask_binary, axis=1)
        cols_with_mask = np.any(mask_binary, axis=0)
        
        if not np.any(rows_with_mask) or not np.any(cols_with_mask):
            return result
            
        top_edge = np.where(rows_with_mask)[0][0]
        bottom_edge = np.where(rows_with_mask)[0][-1]
        left_edge = np.where(cols_with_mask)[0][0]
        right_edge = np.where(cols_with_mask)[0][-1]
        
        # Create coordinate grids
        y_coords, x_coords = np.mgrid[0:H, 0:W]
        
        # Top-left corner
        if blur_up > 0 and blur_left > 0:
            # Calculate separate distances and strengths for each direction
            dist_from_top = np.maximum(0, top_edge - y_coords)
            dist_from_left = np.maximum(0, left_edge - x_coords)
            
            # Calculate strength based on individual blur values
            strength_top = np.exp(-(dist_from_top**2) / (2 * blur_up**2))
            strength_left = np.exp(-(dist_from_left**2) / (2 * blur_left**2))
            
            # Combine strengths multiplicatively for smooth corner transition
            strength = strength_top * strength_left
            
            # Only apply in the top-left quadrant
            corner_mask = (y_coords <= top_edge) & (x_coords <= left_edge)
            result = np.maximum(result, strength * corner_mask)
        
        # Top-right corner
        if blur_up > 0 and blur_right > 0:
            dist_from_top = np.maximum(0, top_edge - y_coords)
            dist_from_right = np.maximum(0, x_coords - right_edge)
            
            strength_top = np.exp(-(dist_from_top**2) / (2 * blur_up**2))
            strength_right = np.exp(-(dist_from_right**2) / (2 * blur_right**2))
            strength = strength_top * strength_right
            
            corner_mask = (y_coords <= top_edge) & (x_coords >= right_edge)
            result = np.maximum(result, strength * corner_mask)
        
        # Bottom-left corner
        if blur_down > 0 and blur_left > 0:
            dist_from_bottom = np.maximum(0, y_coords - bottom_edge)
            dist_from_left = np.maximum(0, left_edge - x_coords)
            
            strength_bottom = np.exp(-(dist_from_bottom**2) / (2 * blur_down**2))
            strength_left = np.exp(-(dist_from_left**2) / (2 * blur_left**2))
            strength = strength_bottom * strength_left
            
            corner_mask = (y_coords >= bottom_edge) & (x_coords <= left_edge)
            result = np.maximum(result, strength * corner_mask)
        
        # Bottom-right corner
        if blur_down > 0 and blur_right > 0:
            dist_from_bottom = np.maximum(0, y_coords - bottom_edge)
            dist_from_right = np.maximum(0, x_coords - right_edge)
            
            strength_bottom = np.exp(-(dist_from_bottom**2) / (2 * blur_down**2))
            strength_right = np.exp(-(dist_from_right**2) / (2 * blur_right**2))
            strength = strength_bottom * strength_right
            
            corner_mask = (y_coords >= bottom_edge) & (x_coords >= right_edge)
            result = np.maximum(result, strength * corner_mask)
        
        return result

    def _apply_directional_blur(self, mask, blur_up, blur_down, blur_left, blur_right, tapered_corners):
        """Apply independent directional blur with optional smooth corner blending."""
        result = mask.copy()
        
        # Create blur masks for each direction
        blur_masks = []
        
        if blur_up > 0:
            blur_masks.append(self._create_directional_blur_mask(mask, 'up', blur_up))
        
        if blur_down > 0:
            blur_masks.append(self._create_directional_blur_mask(mask, 'down', blur_down))
            
        if blur_left > 0:
            blur_masks.append(self._create_directional_blur_mask(mask, 'left', blur_left))
            
        if blur_right > 0:
            blur_masks.append(self._create_directional_blur_mask(mask, 'right', blur_right))
        
        # Combine all blur masks with the original
        for blur_mask in blur_masks:
            result = np.maximum(result, blur_mask)
        
        # Add smooth corner blending only if tapered_corners is enabled
        if tapered_corners:
            corner_blend = self._create_corner_blend(mask, blur_up, blur_down, blur_left, blur_right)
            result = np.maximum(result, corner_blend)
        
        return result

    def process_single(self, mask_np, up, down, right, left, blur_up, blur_down, blur_left, blur_right, tapered_corners):
        """Process a single mask with bounding box expansion and directional blur."""
        # Get bounding box of active pixels
        bbox = self._get_bounding_box(mask_np)
        if bbox is None:
            return np.zeros_like(mask_np, dtype=np.float32)
        
        # Expand bounding box
        expanded_bbox = self._expand_bounding_box(bbox, up, down, left, right, mask_np.shape)
        if expanded_bbox is None:
            return np.zeros_like(mask_np, dtype=np.float32)
        
        # Create base rectangular mask
        min_row_adj, max_row_adj, min_col_adj, max_col_adj = expanded_bbox
        new_mask = np.zeros_like(mask_np, dtype=np.float32)
        new_mask[min_row_adj:max_row_adj + 1, min_col_adj:max_col_adj + 1] = 1.0
        
        # Apply directional blur
        new_mask = self._apply_directional_blur(new_mask, blur_up, blur_down, blur_left, blur_right, tapered_corners)
        
        return new_mask

    def process(self, mask, up, down, right, left, blur_up, blur_down, blur_left, blur_right, tapered_corners):
        """Main processing function supporting both 2D and 3D masks."""
        mask_np = mask.cpu().numpy()
        
        if mask_np.ndim == 2:
            result = self.process_single(mask_np, up, down, right, left, blur_up, blur_down, blur_left, blur_right, tapered_corners)
            result = result[None, ...]
        elif mask_np.ndim == 3:
            results = []
            for i in range(mask_np.shape[0]):
                single_result = self.process_single(
                    mask_np[i], up, down, right, left, blur_up, blur_down, blur_left, blur_right, tapered_corners
                )
                results.append(single_result)
            result = np.stack(results, axis=0)
        else:
            raise ValueError("Mask must be 2D (H, W) or 3D (N, H, W)")
        
        return (torch.from_numpy(result),)