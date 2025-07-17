import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")

def get_next_folder_name(output_dir: str | None = None) -> str:
    if output_dir is not None:
        base_dir = output_dir
    else:
        base_dir = OUTPUT_DIR
    os.makedirs(base_dir, exist_ok=True)
    existing = [
        name for name in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, name))
    ]
    
    nums = []
    for name in existing:
        try:
            num = int(name.split("_")[-1])
            nums.append(num)
        except ValueError:
            continue
    
    next_num = max(nums, default=0) + 1
    output_dir_name = f"{next_num:03d}"
    output_dir_path = os.path.join(base_dir, output_dir_name)
    return output_dir_path

