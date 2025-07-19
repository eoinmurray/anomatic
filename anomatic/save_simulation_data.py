import numpy as np
import json
from dotenv import load_dotenv
from anomatic.to_tidy import to_tidy
import os

load_dotenv()

OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")

def tolist(x):
    return x.tolist() if hasattr(x, 'tolist') else x

def to_serializable(obj):
    if isinstance(obj, dict):
        return {k: to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [to_serializable(i) for i in obj]
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, (np.floating,)):
        return float(obj)
    elif isinstance(obj, (np.integer,)):
        return int(obj)
    else:
        return obj

def save_simulation_data_item(data, key, output_dir: str = OUTPUT_DIR, verbose: bool = False):
    os.makedirs(output_dir, exist_ok=True)

    data_type = data.get("type", "json")

    if not data_type:
        data_type = "json"
    
    if "type" in data:
        data = {k: v for k, v in data.items() if k != "type"}

    file_path = os.path.join(output_dir, f"{key}.json")
    if data_type == "csv":
        file_path = os.path.join(output_dir, f"{key}.csv")

    if data_type == "tidy-json":
        with open(file_path, 'w') as f:
            json.dump(to_serializable(to_tidy(data)), f, indent=4)

    if data_type == "json":
        with open(file_path, 'w') as f:
            json.dump(to_serializable(data), f, indent=4)
    
    if data_type == "csv":
        for sub_key, values in data.items():
            np.savetxt(file_path, np.array(values), delimiter=',', header=sub_key, comments='')

    if verbose:
        print(f"Saved {key} as json to {file_path}")

def save_simulation_data(data, output_dir: str = OUTPUT_DIR, verbose: bool = False):
    for key, value in data.items():
        save_simulation_data_item(value, key, output_dir=output_dir, verbose=verbose)
