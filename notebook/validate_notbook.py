import nbformat

notebook_path = '/Users/priyanshiyadav/Desktop/mlproject/notebook/EDA STUDENT PERFORMANCE.ipynb'

try:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print("Notebook is valid and saved.")
except Exception as e:
    print(f"Error reading or saving notebook: {e}")
