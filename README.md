# PYTHON_GIF_MAKER

## Description
This project is a simple Python script to create GIF animations from a sequence of image files. It uses the `imageio` library to read images and write them as a GIF.

## How It Works
- The script reads a list of image files (e.g., `ER1.png`, `ER2.png`, etc.).
- It combines them into a single GIF file (`team.gif`).
- You can customize the image list and GIF parameters as needed.

## Usage
1. Place your images (e.g., PNG files) in the project directory or in the `images/` folder.
2. Update the `files` list in `gif.py` to match your image filenames and paths.
3. Run the script:
	```bash
	python gif.py
	```
4. The output GIF (`team.gif`) will be created in the project directory.

## Requirements
- Python 3.x
- imageio

Install dependencies with:
```bash
pip install imageio
```