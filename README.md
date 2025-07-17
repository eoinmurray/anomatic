# Anomatic Manager

A personal manager tool for simulations that provides utilities for organizing and saving simulation data with automatic directory management.

## Features

- **Automatic Directory Management**: Creates numbered output directories (001, 002, etc.) for organizing simulation runs
- **Flexible File Path Generation**: Generates file paths within managed directories
- **Data Transformation**: Converts data structures to tidy format for analysis
- **Simulation Data Saving**: Saves simulation results to JSON files with automatic type conversion
- **Environment Configuration**: Supports `.env` files for configuration

## Installation

```bash
pip install -e .
```

## Usage

### Basic Example

```python
from anomatic_manager import save_simulation_data, get_file_path

# Save simulation data
data = {
    "experiment_1": {
        "values": [1, 2, 3, 4, 5],
        "errors": [0.1, 0.2, 0.15, 0.3, 0.25]
    }
}

save_simulation_data(data, verbose=True)

# Get a file path in the next numbered directory
file_path = get_file_path("results.txt")
```

### Functions

#### `save_simulation_data(data, output_dir=None, verbose=False)`

Saves simulation data to JSON files with automatic directory creation.

- `data`: Dictionary containing simulation results
- `output_dir`: Optional output directory (defaults to `OUTPUT_DIR` from environment)
- `verbose`: Print save notifications

#### `get_file_path(filename, output_dir=None)`

Generates a file path within the next numbered directory.

- `filename`: Name of the file
- `output_dir`: Optional output directory override

#### `get_next_folder_name(output_dir=None)`

Returns the path to the next numbered directory (001, 002, etc.).

- `output_dir`: Optional base directory override

#### `to_tidy(data)`

Converts dictionary data to tidy format (list of dictionaries).

- `data`: Dictionary with keys mapping to arrays/lists of equal length

## Configuration

Set the `OUTPUT_DIR` environment variable or create a `.env` file:

```
OUTPUT_DIR=my_output_directory
```

Default output directory is `output/`.

## Directory Structure

```
anomatic_manager/
├── __init__.py
├── get_file_path.py
├── get_next_folder_name.py
├── save_simulation_data.py
└── to_tidy.py
```

## Development

### Testing

```bash
pytest
```

### Dependencies

- `dotenv>=0.9.9`: Environment variable management
- `numpy>=2.2.6`: Numerical computing
- `pytest>=8.4.1`: Testing framework

## License

MIT License