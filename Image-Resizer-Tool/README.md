# 🖼️ Image Resizer Tool

## 🎯 Objective
This project is a Python tool that automatically **resizes and converts all images** in a given folder using the **Pillow** library.

---

## 🧰 Tools Used
- **Python 3**
- **Pillow (PIL)**
- **os** module

Install Pillow:
```bash
pip install pillow
```

---

## 📁 Folder Structure
```
ImageResizer/
│
├── image_resizer.py
├── README.md
├── input_images/      # Place your images here
└── output_images/     # Resized images will be saved here
```

---

## ⚙️ How It Works
1. Reads all images from `input_images/`
2. Resizes them to a defined width and height
3. Converts images to a selected format (default: JPEG)
4. Saves the processed images to `output_images/`

---

## 🧩 Configuration
In `image_resizer.py`, you can customize these:
```python
resize_width = 800
resize_height = 600
output_format = "JPEG"
```

You can change the output format to `"PNG"`, `"BMP"`, or `"GIF"` if desired.

---

## ▶️ How to Run
1. Open a terminal in the project folder.
2. Run the script:
```bash
python image_resizer.py
```
3. All resized images will appear in the `output_images/` folder.

---

## 📸 Example Use Case
Useful for:
- Preparing a **photo gallery**
- Creating **machine learning datasets**
- Optimizing **website images**

---

## 🏁 Outcome
✅ Automated batch image resizing and format conversion — fast, efficient, and reusable.
