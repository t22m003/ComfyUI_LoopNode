
from .loop_node import SimpleForLoop, SimpleForLoopRange

NODE_CLASS_MAPPINGS = {
    "SimpleForLoop": SimpleForLoop,
    "SimpleForLoopRange": SimpleForLoopRange,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleForLoop": "For Loop (Count)",
    "SimpleForLoopRange": "For Loop (Range)",
}
