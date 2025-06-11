import torch
import numpy as np
from PIL import Image

class CombineBackgroundOverlay:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "background": ("IMAGE",),
                "overlay": ("IMAGE",),
                "horizontal_position": ("FLOAT", {"default": 50, "min": -50, "max": 150, "step": 0.1}),
                "vertical_position": ("FLOAT", {"default": 50, "min": -50, "max": 150, "step": 0.1}),
            },
            "optional": {
                "mask": ("MASK",),
            },
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    RETURN_NAMES = ("image", "mask")
    FUNCTION = "combine_background_overlay"
    CATEGORY = "Bjornulf"

    def combine_background_overlay(self, background, overlay, horizontal_position, vertical_position, mask=None):
        results = []
        output_masks = []

        # Process the first background image
        bg = background[0].cpu().numpy()
        bg = np.clip(bg * 255, 0, 255).astype(np.uint8)
        if bg.shape[2] == 4:
            bg_img = Image.fromarray(bg, 'RGBA')
            bg_has_alpha = True
        else:
            bg_img = Image.fromarray(bg, 'RGB')
            bg_has_alpha = False

        # Process each overlay
        for i in range(overlay.shape[0]):
            ov = overlay[i].cpu().numpy()
            ov = np.clip(ov * 255, 0, 255).astype(np.uint8)

            # Check if overlay has an alpha channel
            if ov.shape[2] == 4:
                ov_img = Image.fromarray(ov, 'RGBA')
            else:
                ov_img = Image.fromarray(ov, 'RGB')

            # Apply mask if provided - INVERTED LOGIC: mask removes opacity
            if mask is not None:
                mask_idx = min(i, mask.shape[0] - 1)
                m = mask[mask_idx].cpu().numpy()
                m = np.clip(m * 255, 0, 255).astype(np.uint8)
                mask_img = Image.fromarray(m, 'L')

                # Resize mask to match overlay if needed
                if mask_img.size != ov_img.size:
                    mask_img = mask_img.resize(ov_img.size, Image.LANCZOS)

                # INVERT THE MASK - white areas in mask become transparent
                inverted_mask = Image.eval(mask_img, lambda x: 255 - x)

                if ov_img.mode == 'RGBA':
                    # Combine overlay's alpha with inverted mask
                    ov_alpha = np.array(ov_img.split()[3], dtype=np.float32) / 255.0
                    inverted_mask_alpha = np.array(inverted_mask, dtype=np.float32) / 255.0
                    effective_alpha = (ov_alpha * inverted_mask_alpha * 255).astype(np.uint8)
                    ov_img.putalpha(Image.fromarray(effective_alpha, 'L'))
                else:
                    # Use inverted mask as alpha for RGB overlay
                    ov_img.putalpha(inverted_mask)
            else:
                if ov_img.mode == 'RGB':
                    # Add fully opaque alpha for RGB overlay
                    ov_img.putalpha(Image.new('L', ov_img.size, 255))
                # For RGBA, keep the existing alpha

            # Calculate paste position
            x = int((horizontal_position / 100) * bg_img.width - (horizontal_position / 100) * ov_img.width)
            y = int((vertical_position / 100) * bg_img.height - (vertical_position / 100) * ov_img.height)

            # Prepare the result image
            if bg_has_alpha:
                result = bg_img.copy()
            else:
                result = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
                result.paste(bg_img, (0, 0))

            # Create output mask - start with background alpha or white
            if bg_has_alpha:
                output_mask_img = bg_img.split()[3].copy()
            else:
                output_mask_img = Image.new('L', bg_img.size, 255)

            # Paste overlay directly on top (no alpha blending)
            if x + ov_img.width > 0 and y + ov_img.height > 0 and x < result.width and y < result.height:
                # Convert overlay to RGB if needed for direct paste
                if ov_img.mode == 'RGBA':
                    ov_rgb = Image.new('RGB', ov_img.size, (255, 255, 255))
                    ov_rgb.paste(ov_img, mask=ov_img.split()[3])
                    ov_paste = ov_rgb
                    paste_mask = ov_img.split()[3]
                else:
                    ov_paste = ov_img
                    paste_mask = None
                
                # Apply input mask if provided - UPDATED LOGIC FOR INVERTED MASK
                if mask is not None:
                    mask_idx = min(i, mask.shape[0] - 1)
                    m = mask[mask_idx].cpu().numpy()
                    m = np.clip(m * 255, 0, 255).astype(np.uint8)
                    input_mask = Image.fromarray(m, 'L')
                    if input_mask.size != ov_img.size:
                        input_mask = input_mask.resize(ov_img.size, Image.LANCZOS)
                    
                    # INVERT THE INPUT MASK
                    inverted_input_mask = Image.eval(input_mask, lambda x: 255 - x)
                    
                    if paste_mask is not None:
                        # Combine overlay alpha with inverted input mask
                        paste_mask_array = np.array(paste_mask, dtype=np.float32) / 255.0
                        inverted_input_mask_array = np.array(inverted_input_mask, dtype=np.float32) / 255.0
                        combined_mask_array = (paste_mask_array * inverted_input_mask_array * 255).astype(np.uint8)
                        paste_mask = Image.fromarray(combined_mask_array, 'L')
                    else:
                        # Use inverted input mask directly
                        paste_mask = inverted_input_mask
                
                # Paste overlay directly onto result
                result.paste(ov_paste, (x, y), paste_mask)
                
                # Update output mask
                if paste_mask is not None:
                    temp_mask = Image.new('L', result.size, 0)
                    temp_mask.paste(paste_mask, (x, y))
                    
                    # Combine masks - overlay mask replaces background mask where it exists
                    output_mask_array = np.array(output_mask_img, dtype=np.float32)
                    temp_mask_array = np.array(temp_mask, dtype=np.float32)
                    combined_mask_array = np.maximum(output_mask_array, temp_mask_array).astype(np.uint8)
                    output_mask_img = Image.fromarray(combined_mask_array, 'L')
                else:
                    # No mask - overlay covers background completely in paste area
                    temp_mask = Image.new('L', result.size, 0)
                    temp_mask.paste(Image.new('L', ov_paste.size, 255), (x, y))
                    
                    output_mask_array = np.array(output_mask_img, dtype=np.float32)
                    temp_mask_array = np.array(temp_mask, dtype=np.float32)
                    combined_mask_array = np.maximum(output_mask_array, temp_mask_array).astype(np.uint8)
                    output_mask_img = Image.fromarray(combined_mask_array, 'L')

            # Convert result back to tensor
            result_np = np.array(result)
            if result_np.shape[2] == 4:
                # Convert RGBA back to RGB if background was RGB
                if not bg_has_alpha:
                    alpha = result_np[:, :, 3:4] / 255.0
                    rgb = result_np[:, :, :3]
                    white_bg = np.ones_like(rgb) * 255
                    result_np = (rgb * alpha + white_bg * (1 - alpha)).astype(np.uint8)
                    result_tensor = torch.from_numpy(result_np).float() / 255.0
                else:
                    result_tensor = torch.from_numpy(result_np).float() / 255.0
            else:
                result_tensor = torch.from_numpy(result_np).float() / 255.0

            # Convert output mask to tensor
            output_mask_tensor = torch.from_numpy(np.array(output_mask_img)).float() / 255.0

            results.append(result_tensor)
            output_masks.append(output_mask_tensor)

        final_result = torch.stack(results)
        final_masks = torch.stack(output_masks)
        return (final_result, final_masks)