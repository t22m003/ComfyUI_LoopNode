
# ComfyUI Loop Node

Custom node that provides loop (for-loop) functionality in ComfyUI.
This allows you to repeat execution steps by outputting a list of integers, which triggers ComfyUI's list execution behavior.

## Features

- **For Loop (Count)**: Simple loop that runs `N` times. outputs `0` to `N-1`.
- **For Loop (Range)**: Loop based on python `range(start, stop, step)`.

### Block Looping (Recursive)

- **Block Loop Start**: Marks the beginning of a loop.
    - `first_value`: Value for the first iteration.
    - `total_loops`: How many times to loop.
- **Block Loop End**: Marks the end of a loop.
    - `flow_control`: Connect the last node of your loop block here.
    - `next_value`: The value to pass to the next iteration (connects to `recycle_value` of Start internally).
    - `loop_id`: Connect to the `loop_id` output of `Block Loop Start`.
    - Note: Connect `total_loops` and `current_loop` from `Block Loop Start` to `Block Loop End`.

## Installation

Navigate to your `ComfyUI/custom_nodes/` directory and clone this repository:

```bash
git clone https://github.com/t22m003/ComfyUI_LoopNode.git
```

## Usage

Found under the category: `Loop`

## Sponsor

[![Sponsor](https://img.shields.io/badge/Sponsor-t22m003-red)](https://github.com/sponsors/t22m003)
