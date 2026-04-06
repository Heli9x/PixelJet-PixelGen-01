# PixelJet-PixelGen-01
Generates images from json data containing a list of coordinates in a specified format.
**Powered by [LS-GEN](https://github.com/Heli9x/LS-GEN)**

# PixelGen Scripts

This repository contains two Python scripts for generating pixel art images from JSON data: `pixelGen.py` and `pixelGenV.py` (the "Vibe Coded" version).

## Overview

Both scripts convert pixel data stored in JSON format into PNG images. The JSON files contain arrays of pixel information with coordinates and RGB color values.

## pixelGen.py

### Description
The original PixelGen script provides basic functionality for loading pixel data from JSON files and generating images.

### Features
- Load pixel data from JSON files
- Compile pixel data into PIL images
- Resize images to desired dimensions
- Save images as PNG files
- Automatic processing of predefined image objects

### Usage

1. Ensure you have the required dependencies installed:
   ```bash
   pip install pillow
   ```

2. Place your JSON data files in the appropriate locations:
   - For custom objects: place JSON files in the root directory (e.g., `object.json`)
   - For CC0 objects: place JSON files in the `cc0/` directory (e.g., `cc0/NanoGate.json`)

3. Run the script:
   ```bash
   python pixelGen.py
   ```

4. The script will automatically process the predefined objects ('NanoGate' and 'Parity') and generate images at 200x200 and 64x64 resolutions in their respective `cc0/` subdirectories.

### Manual Usage Example
```python
from pixelGen import PixelGen

# Create a PixelGen instance with desired dimension
gen = PixelGen(10)  # 10x10 grid

# Load pixel data from JSON
gen.load_pixels("my_object")

# Compile the data into the image
gen.compile_data()

# Resize if needed
gen.resize_image(200)

# Save the image
gen.save("my_output")
```

## pixelGenV.py (Vibe Coded Version)

### Description
An improved, more robust version of the PixelGen script with enhanced features and better error handling.

### Features
- Automatic discovery and processing of all JSON files in the `data/` directory
- Improved RGB color parsing with error handling
- Automatic directory creation for output files
- Support for multiple resolutions (64px, 200px, 512px)
- Better file path management using pathlib
- More informative console output

### Usage

1. Ensure you have the required dependencies installed:
   ```bash
   pip install pillow
   ```

2. Create a `data/` directory in the project root if it doesn't exist.

3. Place your JSON pixel data files in the `data/` directory (e.g., `data/NanoGate.json`, `data/Parity.json`).

4. Run the script:
   ```bash
   python pixelGenV.py
   ```

5. The script will automatically:
   - Discover all JSON files in the `data/` directory
   - Process each file and generate images at 64px, 200px, and 512px resolutions
   - Create output directories under `cc0/` (e.g., `cc0/NanoGate/`)
   - Save the generated images with descriptive filenames

### JSON File Format

Both scripts expect JSON files containing arrays of pixel data. Each pixel is represented as an array with three elements:

```json
[
  [
    [x1, y1, "rgb(r1, g1, b1)"],
    [x2, y2, "rgb(r2, g2, b2)"],
    ...
  ],
  ...
]
```

Where:
- `x`, `y`: Integer coordinates (0-based)
- `"rgb(r, g, b)"`: RGB color string with values 0-255

### Dependencies

- Python 3.x
- PIL (Pillow) - `pip install pillow`

### Output

Images are saved as PNG files in the `cc0/` directory structure:
- pixelGen.py: `cc0/{name}/{name}_{resolution}x{resolution}.png`
- pixelGenV.py: `cc0/{name}/{name}_{resolution}px.png`

Both scripts will display the generated images using the system's default image viewer.
