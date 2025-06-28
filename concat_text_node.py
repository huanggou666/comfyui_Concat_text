
class ConcatText:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_1": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "text_2": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    FUNCTION = "concat"

    CATEGORY = "Text"

    def concat(self, text_1, text_2):
        result = f"{text_1},{text_2}"
        return (result,)


NODE_CLASS_MAPPINGS = {
    "ConcatText": ConcatText
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ConcatText": "ConcatText"
}
