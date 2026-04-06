import json
import os
from pathlib import Path
from PIL import Image

class PixelGen:
    def __init__(self, json_file, grid_size=10):
        self.json_path = json_file
        self.name = json_file.stem  # Gets filename without .json extension
        self.grid_size = grid_size
        self.img = Image.new("RGB", (grid_size, grid_size))
        self.pixels = self.img.load()

    def _parse_rgb(self, rgb_str):
        # Cleans "rgb(255, 165, 0)" -> (255, 165, 0)
        clean = rgb_str.replace("rgb(", "").replace(")", "").replace(" ", "")
        return tuple(map(int, clean.split(",")))

    def render(self):
        with open(self.json_path, 'r') as f:
            data = json.load(f)

        for row in data:
            for pixel_data in row:
                # Matches your (x, y, color) structure
                x, y, color_str = pixel_data
                try:
                    self.pixels[y, x] = self._parse_rgb(color_str)
                except Exception as e:
                    print(f"Error parsing pixel at {x},{y} in {self.name}: {e}")

    def export(self, res):
        # Creates 'cc0/NanoGate/' directory automatically
        output_dir = Path(f"cc0/{self.name}")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Scale up and save
        out = self.img.resize((res, res), Image.NEAREST)
        save_path = output_dir / f"{self.name}_{res}px.png"
        out.save(save_path)
        print(f"✅ Generated: {save_path}")

# --- Execution Logic ---

# 1. Define paths using Pathlib
data_folder = Path("data")
resolutions = [64, 200, 512]

# 2. Check if data folder exists
if not data_folder.exists():
    print(f"Creating '{data_folder}' folder. Please drop your JSON files there!")
    data_folder.mkdir()
else:
    # 3. Loop through every .json file in the data folder
    json_files = list(data_folder.glob("*.json"))
    
    if not json_files:
        print("No JSON files found in /data.")
    else:
        for file_path in json_files:
            print(f"Processing {file_path.name}...")
            
            gen = PixelGen(file_path)
            gen.render()
            
            for r in resolutions:
                gen.export(r)