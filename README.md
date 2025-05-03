# Prompt\_or\_image\_to\_3d

A prototype that converts either a photo (single-object image) or a text prompt into a basic 3D model (`.obj` or `.stl`). This repository demonstrates two pipelines:

* **Text-to-3D** (`text_to_3d.py`)
* **Image-to-3D** (`image_to_3d.py`)

---

## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Shoshinmai/Promt_or_image_to_3d.git
   cd Promt_or_image_to_3d
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```python
   %pip install git+https://github.com/openai/shap-e.git
   %pip install numpy trimesh pyrender
   pip install -r requirement.txt
   ```

---

## 📂 Project Structure

```
Prompt_or_image_to_3d/
├── example_object_file/       # Sample .obj/.stl outputs
├── dem2.ipynb                 # Notebook with demos and experiments
├── pre_processing.py          # Utility functions for image cleanup
├── text_to_3d.py              # Text prompt → 3D mesh pipeline
├── image_to_3d.py             # Photo input → 3D mesh pipeline
├── viz.py                     # Simple 3D visualization script
├── requirement.txt            # Python dependencies
└── README.md                  # This file
```

---

## 📝 Requirements

Dependencies are listed in `requirement.txt`. Key libraries:

* **diffusers**, **transformers**, **accelerate**, **safetensors**, **onnxruntime** — text-to-3D pipeline
* **pyyaml**, **ipywidgets** — notebook interactivity
* **Open3D** or **trimesh**, **pyrender**, **numpy** — mesh processing & visualization

---

## 💡 Text-to-3D

Generate a 3D mesh from a text prompt using the Hugging Face Shap-E pipeline.

**Usage**:

Edit the `text_to_3d.py` script directly:

```python
prompt = "a small toy car"
```

Then run:

```bash
python text_to_3d.py
```

This will generate an `.obj` file as output using the prompt defined inside the script.

---

## 🖼️ Image-to-3D

Convert a single-object photo into a 3D mesh.

**Usage**:

Edit the `image_to_3d.py` script directly:

```python
image = load_image("PATH_0F_image_FILE")
```

Then run:

```bash
python image_to_3d.py
```

This will generate an `.obj` mesh file as output using the image and path you specify inside the script.

*Optional:* Adjust preprocessing, depth estimation, and reconstruction parameters inside the script.

---

## 👓 Visualization

Visualize any generated 3D mesh model (`.obj` format) interactively using `viz.py`.

**Usage**:

Edit the `viz.py` script directly:

```python
mesh = trimesh.load('PATH_0F_.obj_FILE', force='mesh')
```

Then run:

```bash
python viz.py
```

This opens a 3D window using `pyrender` where you can orbit, zoom, and inspect the object.

---

## 🧪 Example Output

Sample `.obj` files generated from text and image inputs are available in the `example_object_file/` directory. These can be used for quick testing and visualization.

---

## 📖 License

This project is licensed under the MIT License. See `LICENSE` for details.
