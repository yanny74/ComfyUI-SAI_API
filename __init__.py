from .stability_api import StabilityCreativeUpscale, StabilityRemoveBackground, StabilityInpainting, StabilityCore, StabilitySearchAndReplace, StabilityOutpainting, StabilitySD3

NODE_CLASS_MAPPINGS = {
    "Stability Creative Upscale": StabilityCreativeUpscale,
    "Stability Remove Background": StabilityRemoveBackground,
    "Stability Inpainting": StabilityInpainting,
    "Stability Image Core": StabilityCore,
    "Stability Search and Replace": StabilitySearchAndReplace,
    "Stability Outpainting": StabilityOutpainting,
    "Stability SD3": StabilitySD3,
}
