import numpy as np

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
