
import json
import uuid
from server import PromptServer
from aiohttp import web

class BlockLoopStart:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "first_value": ("INT", {"default": 1}),
                "total_loops": ("INT", {"default": 3, "min": 1, "max": 100}),
            },
            "optional": {
                "current_loop": ("INT", {"default": 0, "hidden": True}), # Injectable
                "recycle_value": ("INT", {"default": 0, "hidden": True}), # Injectable from previous loop
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "STRING")
    RETURN_NAMES = ("current_value", "index", "total", "loop_id")
    FUNCTION = "execute"
    CATEGORY = "Loop"

    def execute(self, first_value, total_loops, current_loop=0, recycle_value=0, unique_id=None):
        # On first run (current_loop=0), use first_value.
        # On subsequent runs, use recycle_value.
        if current_loop == 0:
            val = first_value
        else:
            val = recycle_value
            
        return (val, current_loop, total_loops, unique_id)


class BlockLoopEnd:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "flow_control": ("*",), # Anything to enforce order
                "next_value": ("INT",), # Value to pass to next iteration
                "total_loops": ("INT", {"forceInput": True}),
                "current_loop": ("INT", {"forceInput": True}),
                "loop_id": ("STRING", {"forceInput": True}), # Link to Start Node
            },
            "hidden": {
                "prompt": "PROMPT",
                "extra_pnginfo": "EXTRA_PNGINFO",
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("flow_output",)
    FUNCTION = "execute"
    CATEGORY = "Loop"
    OUTPUT_NODE = True

    def execute(self, flow_control, next_value, total_loops, current_loop, loop_id, prompt=None, extra_pnginfo=None):
        if current_loop + 1 < total_loops:
            # Prepare next iteration
            new_loop_index = current_loop + 1
            print(f"Looping: {current_loop} -> {new_loop_index} / {total_loops}")
            
            # We need to find the specific BlockLoopStart node in the prompt and update its inputs.
            # loop_id is the UNIQUE_ID of the BlockLoopStart node.
            
            new_prompt = prompt.copy()
            target_node = new_prompt.get(str(loop_id))
            
            if target_node:
                # Update inputs for the next run
                target_node['inputs']['current_loop'] = new_loop_index
                target_node['inputs']['recycle_value'] = next_value
                
                # Re-queue
                new_prompt_id = str(uuid.uuid4())
                
                async def queue_new_prompt():
                    import execution
                    server = PromptServer.instance
                    
                    # Validate
                    valid = await execution.validate_prompt(new_prompt_id, new_prompt)
                    
                    if valid[0]:
                        outputs_to_execute = valid[2]
                        # We need to get the next execution number
                        server.number += 1
                        number = server.number
                        
                        # Extra data
                        new_extra_data = extra_pnginfo.copy() if extra_pnginfo else {}
                        
                        # Put in queue
                        server.prompt_queue.put((number, new_prompt_id, new_prompt, new_extra_data, outputs_to_execute, {}))
                        print(f"Loop queued: {new_prompt_id}")
                    else:
                        print(f"Loop validation failed: {valid[1]}")

                # Schedule the task
                PromptServer.instance.loop.create_task(queue_new_prompt())
        
        return (flow_control,)
