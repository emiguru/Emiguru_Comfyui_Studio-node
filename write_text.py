class WriteText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "lines": 10}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "write_text"
    OUTPUT_NODE = True
    CATEGORY = "Emiguru"
    
    def write_text(self, text):
        return (text,)