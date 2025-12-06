
from .loop_node import SimpleForLoop, SimpleForLoopRange
from .recursive_loop import BlockLoopStart, BlockLoopEnd

NODE_CLASS_MAPPINGS = {
    "SimpleForLoop": SimpleForLoop,
    "SimpleForLoopRange": SimpleForLoopRange,
    "BlockLoopStart": BlockLoopStart,
    "BlockLoopEnd": BlockLoopEnd,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleForLoop": "For Loop (Count)",
    "SimpleForLoopRange": "For Loop (Range)",
    "BlockLoopStart": "Block Loop Start",
    "BlockLoopEnd": "Block Loop End",
}
