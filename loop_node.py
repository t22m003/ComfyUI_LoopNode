class SimpleForLoop:
    DESCRIPTION = (
        "Emits the integer sequence 0..total-1 as a list output (OUTPUT_IS_LIST), "
        "so each downstream node runs once per index via ComfyUI list expansion. "
        "Use to repeat a branch `total` times. Use SimpleForLoopRange for an "
        "explicit start/stop/step."
    )

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
        if total < 1:
            raise ValueError(f"total must be at least 1; got total={total}")
        return (list(range(total)),)


class SimpleForLoopRange:
    DESCRIPTION = (
        "Emits range(start, stop, step) as a list of integers (OUTPUT_IS_LIST), "
        "driving one downstream execution per value via ComfyUI list expansion. "
        "`stop` is exclusive. Negative step is supported for countdown ranges. "
        "Empty ranges and step=0 raise a clear ValueError."
    )

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "start": ("INT", {"default": 0, "min": -10000, "max": 10000, "step": 1}),
                "stop": ("INT", {"default": 10, "min": -10000, "max": 10000, "step": 1}),
                "step": ("INT", {"default": 1, "min": -10000, "max": 10000, "step": 1}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("index",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "execute"
    CATEGORY = "Loop"

    def execute(self, start, stop, step):
        if step == 0:
            raise ValueError(
                f"step must not be 0; got start={start}, stop={stop}, step={step}"
            )

        range_vals = list(range(start, stop, step))
        if not range_vals:
            direction = (
                "stop > start is required when step > 0"
                if step > 0
                else "stop < start is required when step < 0"
            )
            raise ValueError(
                f"range is empty for start={start}, stop={stop}, step={step}; "
                f"{direction}"
            )
        return (range_vals,)
