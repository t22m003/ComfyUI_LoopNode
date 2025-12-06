
class SimpleForLoop:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "total": ("INT", {"default": 1, "min": 1, "max": 100, "step": 1}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("index",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "execute"
    CATEGORY = "Loop"

    def execute(self, total):
        return (list(range(total)),)

class SimpleForLoopRange:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "start": ("INT", {"default": 0, "min": 0, "max": 10000, "step": 1}),
                "stop": ("INT", {"default": 10, "min": 0, "max": 10000, "step": 1}),
                "step": ("INT", {"default": 1, "min": 1, "max": 10000, "step": 1}),
            }
        }
    
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("index",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "execute"
    CATEGORY = "Loop"

    def execute(self, start, stop, step):
        range_vals = list(range(start, stop, step))
        return (range_vals,)
