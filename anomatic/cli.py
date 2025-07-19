import fire
import os
import subprocess
import os
import shutil

os.environ["PAGER"] = "cat"

def ui():
  """Launch the Anomatic UI."""

  if shutil.which("bun") is None:
    print("Bun is not installed. Please install Bun to run the UI.")
    return

  ui_dir = os.path.join("ui")
  subprocess.run(["bun", "run", "dev"], cwd=ui_dir)

def main():
  fire.Fire({
      'ui': ui
  })
