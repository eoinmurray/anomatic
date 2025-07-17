import numpy as np
import json
from dotenv import load_dotenv
import os

load_dotenv()

OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")

def get_next_folder_name() -> str:
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


def to_tidy(data: dict) -> list[dict]:
    keys = list(data.keys())
    length = len(data[keys[0]])
    tidy_list = []
    for i in range(length):
        item = {k: data[k][i] for k in keys}
        # Convert numpy types to native Python types for JSON serialization
        for k, v in item.items():
            if isinstance(v, np.generic):
                item[k] = v.item()
            elif isinstance(v, np.ndarray):
                item[k] = v.tolist()
            tidy_list.append(item)
    return tidy_list


def get_file_path(filename: str) -> str:
    output_dir = get_next_folder_name()
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, filename)


def save_simulation_data(data, output_dir: str = OUTPUT_DIR, verbose: bool = False):
    os.makedirs(output_dir, exist_ok=True)

    for key, value in data.items():
        file_path = os.path.join(output_dir, f"{key}.json")

        if not all(isinstance(value[k], (list, np.ndarray)) for k in value):
            with open(file_path, 'w') as f:
                json.dump(value, f, indent=4)
            continue

        tidy_data = to_tidy(value)
        
        with open(file_path, 'w') as f:
            json.dump(tidy_data, f, indent=4)

        if verbose:
            print(f"Saved {key} data to {file_path}")
