import numpy as np
import json
from dotenv import load_dotenv
from anarchomatic_manager.to_tidy import to_tidy
import os

load_dotenv()

OUTPUT_DIR = os.getenv("OUTPUT_DIR", "output")

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
