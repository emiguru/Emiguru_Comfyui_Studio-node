from .show_stuff import ShowFloat, ShowInt, ShowStringText, ShowJson
from .ffmpeg_images_to_video import imagesToVideo
from .write_text import WriteText
from .text_replace import TextReplace
# from .write_image_environment import WriteImageEnvironment
# from .write_image_characters import WriteImageCharacters
# from .write_image_character import WriteImageCharacter
# from .write_image_allinone import WriteImageAllInOne
from .combine_texts import CombineTexts
from .ffmpeg_configuration import FFmpegConfig
from .loop_texts import LoopTexts
from .random_texts import RandomTexts
from .random_model_clip_vae import RandomModelClipVae
from .video_pingpong import VideoPingPong
from .loop_float import LoopFloat
from .loop_integer import LoopInteger
from .loop_basic_batch import LoopBasicBatch
from .loop_samplers import LoopSamplers
from .loop_schedulers import LoopSchedulers
# from .ollama import ollamaLoader OBSOLETE
from .show_text import ShowText
from .save_text import SaveText
from .save_tmp_image import SaveTmpImage
from .save_image_path import SaveImagePath
from .save_img_to_folder import SaveImageToFolder
from .resize_image import ResizeImage
from .resize_image_percentage import ResizeImagePercentage
from .loop_my_combos_samplers_schedulers import LoopCombosSamplersSchedulers
from .remove_transparency import RemoveTransparency
from .image_to_grayscale import GrayscaleTransform
from .combine_background_overlay import CombineBackgroundOverlay
from .save_emiguru_lobechat import SaveEmiguruLobeChat
from .green_to_transparency import GreenScreenToTransparency
from .random_line_from_input import RandomLineFromInput
from .loop_lines import LoopAllLines
from .random_seed_with_text import TextToStringAndSeed
from .load_image_alpha import LoadImageWithTransparency
from .image_mask_cutter import ImageMaskCutter
from .character_description import CharacterDescriptionGenerator
from .text_to_speech import TextToSpeech, XTTSConfig
from .loop_combine_texts_by_lines import CombineTextsByLines
from .free_vram_hack import FreeVRAM
#, PurgeCLIPNode
from .pause_resume_stop import PauseResume
from .pick_input import PickInput
from .loop_images import LoopImages
from .random_image import RandomImage
from .loop_model_clip_vae import LoopModelClipVae
from .write_text_advanced import WriteTextAdvanced
from .loop_write_text import LoopWriteText
from .load_images_from_folder import LoadImagesFromSelectedFolder
from .select_image_from_list import SelectImageFromList
from .random_model_selector import RandomModelSelector
from .if_else import IfElse, MatchTextToInput
from .image_details import ImageDetails
from .video_details import VideoDetails
from .combine_images import CombineImages
# from .pass_preview_image import PassPreviewImage
from .text_scramble_character import ScramblerCharacter
from .audio_video_sync import AudioVideoSync
from .video_path_to_images import VideoToImagesList
from .ffmpeg_images_to_video_path import ImagesListToVideo
from .video_preview import VideoPreview
from .loop_model_selector import LoopModelSelector
from .random_lora_selector import RandomLoraSelector
from .loop_lora_selector import LoopLoraSelector
from .loop_sequential_integer import LoopIntegerSequential
from .loop_lines_sequential import LoopLinesSequential
from .ffmpeg_concat_videos import ConcatVideos
from .ffmpeg_concat_videos_from_list import ConcatVideosFromList
from .ffmpeg_combine_video_audio import CombineVideoAudio
from .images_merger_horizontal import MergeImagesHorizontally
from .images_merger_vertical import MergeImagesVertically
from .ollama_talk import OllamaTalk
from .ollama_image_vision import OllamaImageVision, OllamaVisionPromptSelector
from .ollama_config_selector import OllamaConfig
from .ollama_system_persona import OllamaSystemPersonaSelector
from .ollama_system_job import OllamaSystemJobSelector
from .speech_to_text import SpeechToText
from .text_to_anything import TextToAnything
from .anything_to_text import AnythingToText
from .anything_to_int import AnythingToInt
from .anything_to_float import AnythingToFloat
from .add_line_numbers import AddLineNumbers
from .ffmpeg_convert import ConvertVideo
# from .hiresfix import HiResFix
# from .show_images import ImageBlend
from .text_generator import TextGenerator, TextGeneratorScene, TextGeneratorStyle, TextGeneratorCharacterFemale, TextGeneratorCharacterMale, TextGeneratorOutfitMale, TextGeneratorOutfitFemale, ListLooper, ListLooperScene, ListLooperStyle, ListLooperCharacter, ListLooperOutfitFemale, ListLooperOutfitMale, TextGeneratorCharacterPose, TextGeneratorCharacterObject, TextGeneratorCharacterCreature
from .API_flux import APIGenerateFlux
from .API_StableDiffusion import APIGenerateStability
from .API_civitai import APIGenerateCivitAI, APIGenerateCivitAIAddLORA, CivitAIModelSelectorPony, CivitAIModelSelectorSD15, CivitAIModelSelectorSDXL, CivitAIModelSelectorFLUX_S, CivitAIModelSelectorFLUX_D, CivitAILoraSelectorSD15, CivitAILoraSelectorSDXL, CivitAILoraSelectorPONY, CivitAILoraSelectorHunyuan, LoadCivitAILinks
from .API_falAI import APIGenerateFalAI
from .latent_resolution_selector import LatentResolutionSelector
from .loader_lora_with_path import LoaderLoraWithPath
from .load_text import LoadTextFromFolder, LoadTextFromPath
from .string_splitter import TextSplitin5, TextSplitin10
from .line_selector import LineSelector
from .text_to_speech_kokoro import KokoroTTS
from .note_text import DisplayNote
from .note_image import ImageNote, ImageNoteLoadImage
from .model_clip_vae_selector import ModelClipVaeSelector
from .global_variables import LoadGlobalVariables, SaveGlobalVariables
from .lora_stacks import AllLoraSelector
from .hugginface_download import HuggingFaceDownloader
from .preview_first_image import PreviewFirstImage
# from .video_latent import VideoLatentResolutionSelector
# from .empty_latent_video import EmptyVideoLatentWithSingle
# from .text_generator_t2v import TextGeneratorText2Video
from .images_compare import FourImageViewer
# from .pickme import WriteTextPickMe, PickMe
from .write_pickme_chain import WriteTextPickMeChain
# from .todo import ToDoList
from .text_to_variable import TextToVariable
from .random_stuff import RandomIntNode, RandomFloatNode
from .global_seed_manager import GlobalSeedManager
from .play_sound import PlayAudio
from .switches import SwitchText, SwitchAnything
from .write_pickme_global import WriteTextPickMeGlobal, LoadTextPickMeGlobal
from .list_selector import ListSelector
from .text_analyzer import TextAnalyzer
from .math_node import MathNode
from .save_tmp_audio import SaveTmpAudio
from .save_tmp_video import SaveTmpVideo
from .audio_preview import AudioPreview
from .style_selector import StyleSelector
# from .switches import ConditionalSwitch
from .split_image import SplitImageGrid, ReassembleImageGrid
from .API_openai import APIGenerateGPT4o

from .masks_nodes import LargestMaskOnly, BoundingRectangleMask, BoundingRectangleMaskBlur
from .openai_nodes import OpenAIVisionNode
# MultiOpenAIVisionNode
from .loop_random_seed import LoopRandomSeed

# from .video_text_generator import VideoTextGenerator
# from .run_workflow_from_api import ExecuteWorkflowNode, ApiDynamicTextInputs
# from .remote_nodes import RemoteVAEDecoderNodeTiled, RemoteVAEDecoderNode, LoadFromBase64, SaveTensors, LoadTensor
# from .fix_face import FixFace, FaceSettings
from .image_cut_and_shift import HorizontalCutAndShift
from .load_image_from_path import LoadImageWithTransparencyFromPath
# from .kofi_nodes import CivitAILoraSelectorWanVideo, CivitAILoraSelectorHunyuan
# from .json_prompt_extractor import JSONImagePromptExtractor

from .upscaler_transparency import ImageUpscaleWithModelTransparency
from .load_base64_transparency import loadImageBase64Transparency
#RemoteTextEncodingWithCLIPs

NODE_CLASS_MAPPINGS = {
    "Emiguru_ImageUpscaleWithModelTransparency": ImageUpscaleWithModelTransparency,
    "Emiguru_loadImageBase64Transparency": loadImageBase64Transparency,
    # "Emiguru_LoraSelectorHunyuan": CivitAILoraSelectorHunyuan,
    # "Emiguru_LoraSelectorWanVideo": CivitAILoraSelectorWanVideo,
    # "Emiguru_JSONImagePromptExtractor": JSONImagePromptExtractor,
    "Emiguru_MatchTextToInput": MatchTextToInput,
    "Emiguru_LargestMaskOnly": LargestMaskOnly,
    "Emiguru_BoundingRectangleMask": BoundingRectangleMask,
    "Emiguru_BoundingRectangleMaskBlur": BoundingRectangleMaskBlur,
    "Emiguru_OpenAIVisionNode": OpenAIVisionNode,
    # "Emiguru_MultiOpenAIVisionNode": MultiOpenAIVisionNode,
    "Emiguru_LoopRandomSeed": LoopRandomSeed,
    "Emiguru_HorizontalCutAndShift": HorizontalCutAndShift,
    "Emiguru_LoadImageWithTransparencyFromPath": LoadImageWithTransparencyFromPath,
    # "Emiguru_PurgeCLIPNode": PurgeCLIPNode,
    # "Emiguru_RemoteTextEncodingWithCLIPs": RemoteTextEncodingWithCLIPs,
    
    # "Emiguru_FixFace": FixFace,
    # "Emiguru_FaceSettings": FaceSettings,
    # "Emiguru_SaveTensors": SaveTensors,
    # "Emiguru_LoadTensor": LoadTensor,
    # "Emiguru_LoadFromBase64": LoadFromBase64,
    # "Emiguru_RemoteVAEDecoderNode": RemoteVAEDecoderNode,
    # "Emiguru_RemoteVAEDecoderNodeTiled": RemoteVAEDecoderNodeTiled,
    # "Emiguru_VideoTextGenerator": VideoTextGenerator,
    # "Emiguru_ExecuteWorkflowNode": ExecuteWorkflowNode,
    # "Emiguru_ApiDynamicTextInputs": ApiDynamicTextInputs,
    "Emiguru_APIGenerateGPT4o": APIGenerateGPT4o,
    
    # "Emiguru_ConditionalSwitch": ConditionalSwitch,
    "Emiguru_LoadCivitAILinks": LoadCivitAILinks,
    "Emiguru_SplitImageGrid": SplitImageGrid,
    "Emiguru_ReassembleImageGrid": ReassembleImageGrid,
    "Emiguru_StyleSelector": StyleSelector,
    "Emiguru_OllamaVisionPromptSelector": OllamaVisionPromptSelector,
    "Emiguru_AudioPreview": AudioPreview,
    "Emiguru_SaveTmpAudio": SaveTmpAudio,
    "Emiguru_SaveTmpVideo": SaveTmpVideo,
    "Emiguru_MathNode": MathNode,
    "Emiguru_TextAnalyzer": TextAnalyzer,
    "Emiguru_ListSelector": ListSelector,
    "Emiguru_WriteTextPickMeGlobal": WriteTextPickMeGlobal,
    "Emiguru_LoadTextPickMeGlobal": LoadTextPickMeGlobal,
    "Emiguru_PlayAudio": PlayAudio,
    "Emiguru_SwitchText": SwitchText,
    "Emiguru_SwitchAnything": SwitchAnything,
    "Emiguru_GlobalSeedManager": GlobalSeedManager,
    "Emiguru_RandomIntNode": RandomIntNode,
    "Emiguru_RandomFloatNode": RandomFloatNode,
    "Emiguru_TextToVariable": TextToVariable,
    # "Emiguru_ToDoList": ToDoList,
    # "Emiguru_WriteTextPickMe": WriteTextPickMe,
    "Emiguru_WriteTextPickMeChain": WriteTextPickMeChain,
    # "Emiguru_PickMe": PickMe,
    "Emiguru_FourImageViewer": FourImageViewer,
    "Emiguru_PreviewFirstImage": PreviewFirstImage,
    "Emiguru_HuggingFaceDownloader": HuggingFaceDownloader,
    # "Emiguru_VideoLatentResolutionSelector": VideoLatentResolutionSelector,
    "Emiguru_AllLoraSelector": AllLoraSelector,
    "Emiguru_LoadGlobalVariables": LoadGlobalVariables,
    "Emiguru_SaveGlobalVariables": SaveGlobalVariables,
    "Emiguru_ModelClipVaeSelector": ModelClipVaeSelector,
    "Emiguru_DisplayNote": DisplayNote,
    "Emiguru_ImageNote": ImageNote,
    "Emiguru_ImageNoteLoadImage": ImageNoteLoadImage,
    "Emiguru_LineSelector": LineSelector,
    # "Emiguru_EmptyVideoLatentWithSingle": EmptyVideoLatentWithSingle,
    "Emiguru_XTTSConfig": XTTSConfig,
    "Emiguru_KokoroTTS": KokoroTTS,
    # "Emiguru_TextGeneratorText2Video": TextGeneratorText2Video,
    "Emiguru_LatentResolutionSelector": LatentResolutionSelector,
    "Emiguru_LoaderLoraWithPath": LoaderLoraWithPath,
    "Emiguru_LoadTextFromPath": LoadTextFromPath,
    "Emiguru_LoadTextFromFolder": LoadTextFromFolder,
    "Emiguru_TextSplitin5": TextSplitin5,
    "Emiguru_TextSplitin10": TextSplitin10,
    "Emiguru_APIGenerateFlux": APIGenerateFlux,
    "Emiguru_APIGenerateFalAI": APIGenerateFalAI,
    "Emiguru_APIGenerateStability": APIGenerateStability,
    "Emiguru_APIGenerateCivitAI": APIGenerateCivitAI,
    "emiguru_civitAIModelSelectorPony": CivitAIModelSelectorPony,
    "emiguru_civitAIModelSelectorSD15": CivitAIModelSelectorSD15,
    "emiguru_civitAIModelSelectorSDXL": CivitAIModelSelectorSDXL,
    "emiguru_civitAIModelSelectorFLUX_S": CivitAIModelSelectorFLUX_S,
    "emiguru_civitAIModelSelectorFLUX_D": CivitAIModelSelectorFLUX_D,
    "emiguru_civitAILoraSelectorSD15": CivitAILoraSelectorSD15,
    "emiguru_civitAILoraSelectorSDXL": CivitAILoraSelectorSDXL,
    "emiguru_civitAILoraSelectorPONY": CivitAILoraSelectorPONY,
    "emiguru_civitAILoraSelectorHunyuan": CivitAILoraSelectorHunyuan,
    # "emiguru_civitAILoraSelector": CivitAILoraSelector,
    "Emiguru_APIGenerateCivitAIAddLORA": APIGenerateCivitAIAddLORA,
    "Emiguru_TextGenerator": TextGenerator,
    "Emiguru_TextGeneratorCharacterPose": TextGeneratorCharacterPose,
    "Emiguru_TextGeneratorCharacterObject": TextGeneratorCharacterObject,
    "Emiguru_TextGeneratorScene": TextGeneratorScene,
    "Emiguru_TextGeneratorStyle": TextGeneratorStyle,
    "Emiguru_TextGeneratorCharacterFemale": TextGeneratorCharacterFemale,
    "Emiguru_TextGeneratorCharacterMale": TextGeneratorCharacterMale,
    "Emiguru_TextGeneratorCharacterCreature": TextGeneratorCharacterCreature,
    "Emiguru_TextGeneratorOutfitFemale": TextGeneratorOutfitFemale,
    "Emiguru_TextGeneratorOutfitMale": TextGeneratorOutfitMale,
    "Emiguru_ListLooper": ListLooper,
    "Emiguru_ListLooperScene": ListLooperScene,
    "Emiguru_ListLooperStyle": ListLooperStyle,
    "Emiguru_ListLooperCharacter": ListLooperCharacter,
    "Emiguru_ListLooperOutfitMale": ListLooperOutfitMale,
    "Emiguru_ListLooperOutfitFemale": ListLooperOutfitFemale,
    # "Emiguru_HiResFix": HiResFix,
    # "Emiguru_ImageBlend": ImageBlend,
    "Emiguru_ShowInt": ShowInt, 
    "Emiguru_TextReplace" : TextReplace,
    "Emiguru_ShowFloat": ShowFloat,
    "Emiguru_ShowJson": ShowJson,
    "Emiguru_ShowStringText": ShowStringText,
    # "Emiguru_ollamaLoader": ollamaLoader, OBSOLETE
    "Emiguru_FFmpegConfig": FFmpegConfig,
    "Emiguru_ConvertVideo": ConvertVideo,
    "Emiguru_AddLineNumbers": AddLineNumbers,
    "Emiguru_TextToAnything": TextToAnything,
    "Emiguru_AnythingToText": AnythingToText,
    "Emiguru_AnythingToInt": AnythingToInt,
    "Emiguru_AnythingToFloat": AnythingToFloat,
    "Emiguru_SpeechToText": SpeechToText,
    "Emiguru_OllamaConfig": OllamaConfig,
    "Emiguru_OllamaSystemPersonaSelector": OllamaSystemPersonaSelector,
    "Emiguru_OllamaSystemJobSelector": OllamaSystemJobSelector,
    "Emiguru_OllamaImageVision": OllamaImageVision,
    "Emiguru_OllamaTalk": OllamaTalk,
    "Emiguru_MergeImagesHorizontally": MergeImagesHorizontally,
    "Emiguru_MergeImagesVertically": MergeImagesVertically,
    "Emiguru_CombineVideoAudio": CombineVideoAudio,
    "Emiguru_ConcatVideos": ConcatVideos,
    "Emiguru_ConcatVideosFromList": ConcatVideosFromList,
    "Emiguru_LoopLinesSequential": LoopLinesSequential,
    "Emiguru_LoopIntegerSequential": LoopIntegerSequential,
    "Emiguru_LoopLoraSelector": LoopLoraSelector,
    "Emiguru_RandomLoraSelector": RandomLoraSelector,
    "Emiguru_LoopModelSelector": LoopModelSelector,
    "Emiguru_VideoPreview": VideoPreview,
    "Emiguru_ImagesListToVideo": ImagesListToVideo,
    "Emiguru_VideoToImagesList": VideoToImagesList,
    "Emiguru_AudioVideoSync": AudioVideoSync,
    "Emiguru_ScramblerCharacter": ScramblerCharacter,
    "Emiguru_CombineImages": CombineImages,
    "Emiguru_ImageDetails": ImageDetails,
    "Emiguru_VideoDetails": VideoDetails,
    "Emiguru_IfElse": IfElse,
    "Emiguru_RandomModelSelector": RandomModelSelector,
    "Emiguru_SelectImageFromList": SelectImageFromList,
    "Emiguru_WriteText": WriteText,
    "Emiguru_LoadImagesFromSelectedFolder": LoadImagesFromSelectedFolder,
    "Emiguru_LoopModelClipVae": LoopModelClipVae,
    "Emiguru_LoopWriteText": LoopWriteText,
    "Emiguru_LoopImages": LoopImages,
    "Emiguru_RandomImage": RandomImage,
    # "Emiguru_PassPreviewImage": PassPreviewImage,
    "Emiguru_PickInput": PickInput,
    "Emiguru_PauseResume": PauseResume,
    "Emiguru_FreeVRAM": FreeVRAM,
    "Emiguru_CombineTextsByLines": CombineTextsByLines,
    "Emiguru_TextToSpeech": TextToSpeech,
    "Emiguru_CharacterDescriptionGenerator": CharacterDescriptionGenerator,
    "Emiguru_ImageMaskCutter": ImageMaskCutter,
    "Emiguru_LoadImageWithTransparency": LoadImageWithTransparency,
    "Emiguru_LoopAllLines": LoopAllLines,
    "Emiguru_TextToStringAndSeed": TextToStringAndSeed,
    "Emiguru_GreenScreenToTransparency": GreenScreenToTransparency,
    "Emiguru_RandomLineFromInput": RandomLineFromInput,
    "Emiguru_SaveEmiguruLobeChat": SaveEmiguruLobeChat,
    "Emiguru_WriteTextAdvanced": WriteTextAdvanced,
    "Emiguru_RemoveTransparency": RemoveTransparency,
    "Emiguru_GrayscaleTransform": GrayscaleTransform,
    "Emiguru_CombineBackgroundOverlay": CombineBackgroundOverlay,
    "Emiguru_ShowText": ShowText,
    "Emiguru_SaveText": SaveText,
    "Emiguru_ResizeImage": ResizeImage,
    "Emiguru_ResizeImagePercentage": ResizeImagePercentage,
    "Emiguru_SaveImageToFolder": SaveImageToFolder,
    "Emiguru_SaveTmpImage": SaveTmpImage,
    "Emiguru_SaveImagePath": SaveImagePath,
    "Emiguru_CombineTexts": CombineTexts,
    "Emiguru_LoopTexts": LoopTexts,
    "Emiguru_RandomTexts": RandomTexts,
    "Emiguru_RandomModelClipVae": RandomModelClipVae,
    "Emiguru_imagesToVideo": imagesToVideo,
    "Emiguru_VideoPingPong": VideoPingPong,
    "Emiguru_LoopFloat": LoopFloat,
    "Emiguru_LoopInteger": LoopInteger,
    "Emiguru_LoopBasicBatch": LoopBasicBatch,
    "Emiguru_LoopSamplers": LoopSamplers,
    "Emiguru_LoopSchedulers": LoopSchedulers,
    "Emiguru_LoopCombosSamplersSchedulers": LoopCombosSamplersSchedulers,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Emiguru_loadImageBase64Transparency": "📥🖼 Load Image Base64 (Transparency)",
    "Emiguru_ImageUpscaleWithModelTransparency": "🖼 Upscale Image with Transparency (with model)",
    #"Emiguru_LoraSelectorHunyuan": "☕ Lora Selector Hunyuan",
    #"Emiguru_LoraSelectorWanVideo": "☕ Lora Selector WanVideo",
    #"Emiguru_JSONImagePromptExtractor": "JSONImagePromptExtractor", 
    "Emiguru_MatchTextToInput": "🔛📝 Match 10 Text to Input",
    "Emiguru_LargestMaskOnly": "👺🔪 Largest Mask Only",
    "Emiguru_BoundingRectangleMask": "👺➜▢ Convert mask to rectangle",
    "Emiguru_BoundingRectangleMaskBlur": "👺➜▢ Convert mask to rectangle (with Blur)",
    "Emiguru_OpenAIVisionNode": "🔮 OpenAI Vision Node",
    #"Emiguru_MultiOpenAIVisionNode": "🔮 OpenAI Vision Node (⚠️ Multiple images accepted as input ⚠️)",
    "Emiguru_LoopRandomSeed": "♻🎲 Loop Random Seed",
    "Emiguru_LoadImageWithTransparencyFromPath": "📥🖼 Load Image with Transparency From Path",
    # "Emiguru_RemoteTextEncodingWithCLIPs": "[BETA] 🔮 Remote Text Encoding with CLIPs",
    # "Emiguru_ConditionalSwitch": "ConditionalSwitch",
    # "Emiguru_PurgeCLIPNode": "🧹📎 Purge CLIP",
    "Emiguru_HorizontalCutAndShift": "🔪🖼 Horizontal Cut and Shift 🔼🔽",
    
    # "Emiguru_FixFace": "[BETA] 🔧🧑 Fix Face",
    # "Emiguru_FaceSettings": "[BETA] 🧑 Face Settings [Fix Face] ⚙",
    # "Emiguru_SaveTensors": "[BETA] 💾 Save Tensors (tmp_api.pt) ⚠️💣",
    # "Emiguru_LoadTensor": "[BETA] 📥 Load Tensor (tmp_api.pt)",
    # "Emiguru_RemoteVAEDecoderNode": "[BETA] 🔮 Remote VAE Decoder",
    # "Emiguru_RemoteVAEDecoderNodeTiled": "[BETA] 🔮 Remote VAE Decoder (Tiled)",
    # "Emiguru_LoadFromBase64": "[BETA] 📥🔮 Load from Base64",
    # "Emiguru_ApiDynamicTextInputs": "[BETA] 📥🔮📝 Text Manager Api (Execute Workflow)",
    # "Emiguru_ExecuteWorkflowNode": "[BETA] 🔮⚡ Remote Execute Workflow",
    # "Emiguru_VideoTextGenerator": "[BETA] 🔥📝📹 Video Text Generator 📹📝🔥",
    
    "Emiguru_LoadCivitAILinks": "📥🕑🤖 Load CivitAI Links",
    "Emiguru_StyleSelector": "🎨📜 Style Selector (🎲 or ♻ or ♻📑) + Civitai urn",
    "Emiguru_ReassembleImageGrid": "🖼📹🔨 Reassemble Image/Video Grid",
    "Emiguru_SplitImageGrid": "🖼📹🔪 Split Image/Video Grid",
    "Emiguru_SaveTmpAudio": "💾🔊 Save Audio (tmp_api.wav/mp3) ⚠️💣",
    "Emiguru_SaveTmpVideo": "💾📹 Save Video (tmp_api.mp4/mkv/webm) ⚠️💣",
    "Emiguru_AudioPreview": "🔊▶ Audio Preview (Audio player)",
    "Emiguru_MathNode": "🧮 Basic Math",
    "Emiguru_TextAnalyzer": "📊🔍 Text Analyzer",
    "Emiguru_OllamaVisionPromptSelector": "🦙👁 Ollama Vision Prompt Selector",
    "Emiguru_ListSelector": "📑👈 Select from List",
    "Emiguru_PlayAudio": "🔊▶ Play Audio",
    "Emiguru_SwitchText": "🔛📝 Text Switch On/Off",
    "Emiguru_SwitchAnything": "🔛✨ Anything Switch On/Off",
    "Emiguru_GlobalSeedManager": "🌎🎲 Global Seed Manager",
    "Emiguru_RandomIntNode": "🎲 Random Integer",
    "Emiguru_RandomFloatNode": "🎲 Random Float",
    "Emiguru_WriteTextPickMeGlobal": "🌎✒👉 Global Write Pick Me",
    "Emiguru_LoadTextPickMeGlobal": "🌎📥 Load Global Pick Me",
    "Emiguru_TextToVariable": "📌🅰️ Set Variable from Text",
    # "Emiguru_ToDoList": "ToDoList",
    # "Emiguru_WriteTextPickMe": "✒👉 Write Pick Me",
    "Emiguru_WriteTextPickMeChain": "✒👉 Write Pick Me Chain",
    # "Emiguru_PickByText": "✒👉 Pick Me by Text",
    # "Emiguru_PickMe": "✋ Recover Pick Me ! ✋",
    "Emiguru_FourImageViewer": "🖼👁 Preview 1-4 images (compare)",
    "Emiguru_PreviewFirstImage": "🖼👁 Preview (first) image",
    "Emiguru_HuggingFaceDownloader": "💾 Huggingface Downloader",
    "Emiguru_AllLoraSelector": "👑 Combine Loras, Lora stack",
    "Emiguru_LoadGlobalVariables": "📥🅰️ Load Global Variables",
    "Emiguru_SaveGlobalVariables": "💾🅰️ Save Global Variables",
    "Emiguru_ModelClipVaeSelector": "📝👈 Model-Clip-Vae selector (🎲 or ♻ or ♻📑)",
    "Emiguru_DisplayNote": "📒 Note",
    "Emiguru_ImageNote": "🖼📒 Image Note",
    "Emiguru_ImageNoteLoadImage": "📥🖼📒 Image Note (Load image)",
    # "Emiguru_VideoLatentResolutionSelector": "🩷📹 Empty Video Latent Selector",
    # "Emiguru_EmptyVideoLatentWithSingle": "Emiguru_EmptyVideoLatentWithSingle",
    "Emiguru_XTTSConfig": "🔊 TTS Configuration ⚙",
    "Emiguru_TextToSpeech": "📝➜🔊 TTS - Text to Speech",
    # "Emiguru_HiResFix": "HiResFix",
    # "Emiguru_ImageBlend": "🎨 Image Blend",
    # "Emiguru_APIHiResCivitAI": "🎨➜🎨 API Image hires fix (CivitAI)",
    # "emiguru_civitAILoraSelector": "lora Civit",
    "Emiguru_KokoroTTS": "📝➜🔊 Kokoro - Text to Speech",
    "Emiguru_LineSelector": "📝👈🅰️ Line selector (🎲 or ♻ or ♻📑)",
    "Emiguru_LoaderLoraWithPath": "📥👑 Load Lora with Path",
    # "Emiguru_TextGeneratorText2Video": "🔥📝📹 Text Generator for text to video 📹📝🔥",
    "Emiguru_TextSplitin5": "📝🔪 Text split in 5",
    "Emiguru_TextSplitin10": "📝🔪 Text split in 10",
    "Emiguru_LatentResolutionSelector": "🩷 Empty Latent Selector",
    "emiguru_civitAIModelSelectorSD15": "📥 Load checkpoint SD1.5 (+Download from CivitAi)",
    "emiguru_civitAIModelSelectorSDXL": "📥 Load checkpoint SDXL (+Download from CivitAi)",
    "emiguru_civitAIModelSelectorPony": "📥 Load checkpoint Pony (+Download from CivitAi)",
    "emiguru_civitAIModelSelectorFLUX_D": "📥 Load checkpoint FLUX Dev (+Download from CivitAi)",
    "emiguru_civitAIModelSelectorFLUX_S": "📥 Load checkpoint FLUX Schnell (+Download from CivitAi)",
    "emiguru_civitAILoraSelectorSD15": "📥👑 Load Lora SD1.5 (+Download from CivitAi)",
    "emiguru_civitAILoraSelectorSDXL": "📥👑 Load Lora SDXL (+Download from CivitAi)",
    "emiguru_civitAILoraSelectorPONY": "📥👑 Load Lora Pony (+Download from CivitAi)",
    "emiguru_civitAILoraSelectorHunyuan": "📥👑📹 Load Lora Hunyuan Video (+Download from CivitAi)",
    "Emiguru_APIGenerateFalAI": "☁🎨 API Image Generator (FalAI) 🎨☁",
    "Emiguru_APIGenerateCivitAI": "☁🎨 API Image Generator (CivitAI) 🎨☁",
    "Emiguru_APIGenerateCivitAIAddLORA": "☁👑 Add Lora (API ONLY - CivitAI) 👑☁",
    "Emiguru_APIGenerateFlux": "☁🎨 API Image Generator (Black Forest Labs - Flux) 🎨☁",
    "Emiguru_APIGenerateStability": "☁🎨 API Image Generator (Stability - Stable Diffusion) 🎨☁",
    "Emiguru_TextGenerator": "🔥📝 Image Text Generator 📝🔥",
    "Emiguru_TextGeneratorCharacterFemale": "👩‍🦰📝 Text Generator (Character Female)",
    "Emiguru_TextGeneratorCharacterMale": "👨‍🦰📝 Text Generator (Character Male)",
    "Emiguru_TextGeneratorCharacterPose": "💃🕺📝 Text Generator (Character Pose)",
    "Emiguru_TextGeneratorCharacterObject": "🔧👨‍🔧📝 Text Generator (Object for Character)",
    "Emiguru_TextGeneratorCharacterCreature": "👾📝 Text Generator (Character Creature)",
    "Emiguru_TextGeneratorScene": "🌄📝 Text Generator (Scene)",
    "Emiguru_TextGeneratorStyle": "🎨📝 Text Generator (Style)",
    "Emiguru_TextGeneratorOutfitFemale": "👗 Text Generator (Outfit Female)",
    "Emiguru_TextGeneratorOutfitMale": "👚 Text Generator (Outfit Male)",
    "Emiguru_ListLooper": "♻🔥📝 List Looper (Text Generator)",
    "Emiguru_ListLooperScene": "♻🌄📝 List Looper (Text Generator Scenes)",
    "Emiguru_ListLooperStyle": "♻🎨📝 List Looper (Text Generator Styles)",
    "Emiguru_ListLooperPose": "♻💃🕺📝 List Looper (Text Generator Poses)",
    "Emiguru_ListLooperCharacter": "♻👨‍🦰👩‍🦰👾 List Looper (Text Generator Characters)",
    "Emiguru_ListLooperOutfitMale": "♻👚 List Looper (Text Generator Outfits Male)",
    "Emiguru_ListLooperOutfitFemale": "♻👗 List Looper (Text Generator Outfits Female)",
    "Emiguru_ShowInt": "👁 Show (Int)",
    "Emiguru_ShowFloat": "👁 Show (Float)",
    "Emiguru_ShowJson": "👁 Show (JSON)",
    "Emiguru_ShowStringText": "👁 Show (String/Text)",
    "Emiguru_OllamaTalk": "🦙💬 Ollama Talk",
    "Emiguru_OllamaImageVision": "🦙👁 Ollama Vision",
    "Emiguru_OllamaConfig": "🦙 Ollama Configuration ⚙",
    "Emiguru_XTTSConfig": "🔊 TTS Configuration ⚙",
    "Emiguru_OllamaSystemJobSelector": "🦙 Ollama Job Selector 👇",
    "Emiguru_OllamaSystemPersonaSelector": "🦙 Ollama Persona Selector 👇",
    "Emiguru_SpeechToText": "🔊➜📝 STT - Speech to Text",
    "Emiguru_TextToSpeech": "📝➜🔊 TTS - Text to Speech",
    "Emiguru_TextToAnything": "📝➜✨ Text to Anything",
    "Emiguru_AnythingToText": "✨➜📝 Anything to Text",
    "Emiguru_AnythingToInt": "✨➜🔢 Anything to Int",
    "Emiguru_AnythingToFloat": "✨➜🔢 Anything to Float",
    "Emiguru_TextReplace": "📝➜📝 Replace text",
    "Emiguru_AddLineNumbers": "🔢 Add line numbers",
    "Emiguru_FFmpegConfig": "⚙📹 FFmpeg Configuration 📹⚙",
    "Emiguru_ConvertVideo": "📹➜📹 Convert Video (FFmpeg)",
    "Emiguru_VideoDetails": "📹🔍 Video details (FFmpeg) ⚙",
    "Emiguru_WriteText": "✒ Write Text",
    "Emiguru_MergeImagesHorizontally": "🖼🖼 Merge Images/Videos 📹📹 (Horizontally)",
    "Emiguru_MergeImagesVertically": "🖼🖼 Merge Images/Videos 📹📹 (Vertically)",
    "Emiguru_CombineVideoAudio": "📹🔊 Combine Video + Audio",
    "Emiguru_ConcatVideos": "📹🔗 Concat Videos (FFmpeg)",
    "Emiguru_ConcatVideosFromList": "📹🔗 Concat Videos from list (FFmpeg)",
    "Emiguru_LoopLinesSequential": "♻📑 Loop Sequential (input Lines)",
    "Emiguru_LoopIntegerSequential": "♻📑 Loop Sequential (Integer)",
    "Emiguru_LoopLoraSelector": "♻👑 Loop Lora Selector",
    "Emiguru_RandomLoraSelector": "🎲👑 Random Lora Selector",
    "Emiguru_LoopModelSelector": "♻ Loop Load checkpoint (Model Selector)",
    "Emiguru_VideoPreview": "📹👁 Video Preview",
    "Emiguru_ImagesListToVideo": "🖼➜📹 Images to Video path (tmp video) (FFmpeg)",
    "Emiguru_VideoToImagesList": "📹➜🖼 Video Path to Images (Load video)",
    "Emiguru_AudioVideoSync": "🔊📹 Audio Video Sync",
    "Emiguru_ScramblerCharacter": "🔀🎲 Text scrambler (🧑 Character)",
    "Emiguru_WriteTextAdvanced": "✒🗔🅰️ Advanced Write Text",
    "Emiguru_LoopWriteText": "♻ Loop (✒🗔🅰️ Advanced Write Text)",
    "Emiguru_LoopModelClipVae": "♻ Loop (Model+Clip+Vae)",
    "Emiguru_LoopImages": "♻🖼 Loop (Images)",
    "Emiguru_CombineTextsByLines": "♻ Loop (All Lines from input 🔗 combine by lines)",
    "Emiguru_LoopTexts": "♻ Loop (Texts)",
    "Emiguru_LoopFloat": "♻ Loop (Float)",
    "Emiguru_LoopInteger": "♻ Loop (Integer)",
    "Emiguru_LoopBasicBatch": "♻ Loop",
    "Emiguru_LoopAllLines": "♻ Loop (All Lines from input)",
    "Emiguru_LoopSamplers": "♻ Loop (All Samplers)",
    "Emiguru_LoopSchedulers": "♻ Loop (All Schedulers)",
    "Emiguru_LoopCombosSamplersSchedulers": "♻ Loop (My combos Sampler⚔Scheduler)",
    "Emiguru_RandomImage": "🎲🖼 Random Image",
    "Emiguru_RandomLineFromInput": "🎲 Random line from input",
    "Emiguru_RandomTexts": "🎲 Random (Texts)",
    "Emiguru_RandomModelClipVae": "🎲 Random (Model+Clip+Vae)",
    "Emiguru_RandomModelSelector": "🎲 Random Load checkpoint (Model Selector)",
    # "Emiguru_PassPreviewImage": "🖼⮕ Pass Preview Image",
    "Emiguru_CharacterDescriptionGenerator": "🧑📝 Character Description Generator",
    "Emiguru_GreenScreenToTransparency": "🟩➜▢ Green Screen to Transparency",
    "Emiguru_SaveEmiguruLobeChat": "🖼💬 Save image for Emiguru LobeChat",
    "Emiguru_TextToStringAndSeed": "🔢🎲 Text with random Seed",
    "Emiguru_ShowText": "👁 Show (Text, Int, Float)",
    "Emiguru_ImageMaskCutter": "🖼✂ Cut Image with Mask",
    "Emiguru_LoadImageWithTransparency": "📥🖼 Load Image with Transparency ▢",
    "Emiguru_CombineBackgroundOverlay": "🖼+🖼 Stack two images (Background+Overlay alpha)",
    "Emiguru_GrayscaleTransform": "🖼➜🔲 Image to grayscale (black & white)",
    "Emiguru_RemoveTransparency": "▢➜⬛ Remove image Transparency (alpha)",
    "Emiguru_ResizeImage": "📏 Resize Image",
    "Emiguru_ResizeImagePercentage": "📏 Resize Image Percentage",
    "Emiguru_SaveImagePath": "💾🖼 Save Image (exact path, exact name) ⚠️💣",
    "Emiguru_SaveImageToFolder": "💾🖼📁 Save Image(s) to a folder",
    "Emiguru_SaveTmpImage": "💾🖼 Save Image (tmp_api.png) ⚠️💣",
    "Emiguru_SaveText": "💾 Save Text",
    "Emiguru_LoadTextFromPath": "📥 Load Text From Path",
    "Emiguru_LoadTextFromFolder": "📥 Load Text From Emiguru Folder",
    "Emiguru_CombineTexts": "🔗 Combine (Texts)",
    "Emiguru_imagesToVideo": "🖼➜📹 images to video (FFMPEG Save Video)",
    "Emiguru_VideoPingPong": "📹 video PingPong",
    "Emiguru_ollamaLoader": "🦙 Ollama (Description)",
    "Emiguru_FreeVRAM": "🧹 Free VRAM hack",
    "Emiguru_PickInput": "⏸️ Paused. Select input, Pick 👇",
    "Emiguru_PauseResume": "⏸️ Paused. Resume or Stop, Pick 👇",
    "Emiguru_LoadImagesFromSelectedFolder": "📥🖼📂 Load Images from output folder",
    "Emiguru_SelectImageFromList": "🖼👈 Select an Image, Pick",
    "Emiguru_IfElse": "🔀 If-Else (input / compare_with)",
    "Emiguru_ImageDetails": "🖼🔍 Image Details",
    "Emiguru_CombineImages": "🖼🔗 Combine Images",
    "Emiguru_APIGenerateGPT4o": "☁🎨 API Image Generator (openai, gpt-image-1)",
}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
