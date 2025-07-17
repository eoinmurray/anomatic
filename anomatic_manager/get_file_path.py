from anomatic_manager.get_next_folder_name import get_next_folder_name
import os

def get_file_path(filename: str, output_dir: str | None = None) -> str:
    output_dir = get_next_folder_name(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, filename)
