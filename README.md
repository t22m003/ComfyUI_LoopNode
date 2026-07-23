
# ComfyUI Loop Node

Custom nodes that emit lists of integers through ComfyUI's `OUTPUT_IS_LIST`
list-expansion behavior. Downstream nodes execute once for each emitted value.

This is not an EasyUse-style control-flow loop and does not carry state between
iterations.

## Features

- **For Loop (Count)** (`SimpleForLoop`): emits integers from `0` to `N - 1`.
- **For Loop (Range)** (`SimpleForLoopRange`): emits integers from Python's
  `range(start, stop, step)`, including countdown ranges with a negative step.

Both nodes are available in the `Loop` category.

Ranges that produce no values raise a clear error instead of passing an empty
list into downstream nodes. For a positive step, `stop` must be greater than
`start`; for a negative step, `stop` must be less than `start`. A step of zero
is invalid.

## Installation

Navigate to your `ComfyUI/custom_nodes/` directory and clone this repository:

```bash
git clone https://github.com/t22m003/ComfyUI_LoopNode.git
```

## Usage

Load `examples/basic_loop_workflow.json` in ComfyUI for Count and Range examples
connected to `PreviewAny` nodes.

## Sponsor

[![Sponsor](https://img.shields.io/badge/Sponsor-t22m003-red)](https://github.com/sponsors/t22m003)
