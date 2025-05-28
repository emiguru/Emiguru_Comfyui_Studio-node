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

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "combine_background_overlay"
    CATEGORY = "Bjornulf"

    def combine_background_overlay(self, background, overlay, horizontal_position, vertical_position, mask=None):
        results = []

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

            # Apply mask if provided
            if mask is not None:
                mask_idx = min(i, mask.shape[0] - 1)
                m = mask[mask_idx].cpu().numpy()
                m = np.clip(m * 255, 0, 255).astype(np.uint8)
                mask_img = Image.fromarray(m, 'L')

                # Resize mask to match overlay if needed
                if mask_img.size != ov_img.size:
                    mask_img = mask_img.resize(ov_img.size, Image.LANCZOS)

                if ov_img.mode == 'RGBA':
                    # Combine overlay’s alpha with mask
                    ov_alpha = np.array(ov_img.split()[3], dtype=np.float32) / 255.0
                    mask_alpha = np.array(mask_img, dtype=np.float32) / 255.0
                    effective_alpha = (ov_alpha * mask_alpha * 255).astype(np.uint8)
                    ov_img.putalpha(Image.fromarray(effective_alpha, 'L'))
                else:
                    # Use mask as alpha for RGB overlay
                    ov_img.putalpha(mask_img)
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

            # Paste overlay with alpha blending
            if x + ov_img.width > 0 and y + ov_img.height > 0 and x < result.width and y < result.height:
                temp = Image.new('RGBA', result.size, (0, 0, 0, 0))
                temp.paste(ov_img, (x, y), ov_img)
                result = Image.alpha_composite(result.convert('RGBA'), temp)

            # Convert result back to tensor
            result_np = np.array(result)
            if bg_has_alpha:
                result_tensor = torch.from_numpy(result_np).float() / 255.0
            else:
                # Convert RGBA to RGB, blending with white only where needed
                if result_np.shape[2] == 4:
                    alpha = result_np[:, :, 3:4] / 255.0
                    rgb = result_np[:, :, :3]
                    white_bg = np.ones_like(rgb) * 255
                    result_np = (rgb * alpha + white_bg * (1 - alpha)).astype(np.uint8)
                result_tensor = torch.from_numpy(result_np).float() / 255.0

            results.append(result_tensor)

        final_result = torch.stack(results)
        return (final_result,)