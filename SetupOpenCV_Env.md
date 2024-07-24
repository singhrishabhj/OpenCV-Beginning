# Setting Up Virtual Environment for OpenCV

To set up a virtual environment to run OpenCV and necessary packages, follow these steps:

### 1. Create a Virtual Environment

```bash
python3 -m venv env  # Replace `env` with your preferred environment name
```

### 2. Activate the Virtual Environment

```bash
source env/bin/activate
```

### 3. Install OpenCV

```bash
pip install opencv-python
```
*(Note: Press `Tab` after `pip` to see the available versions.)*

### 4. Install Matplotlib

```bash
pip install matplotlib
```

---



- **Create a Virtual Environment**: This command sets up a virtual Python environment named `env` (you can replace `env` with any name you choose) in the current directory.

- **Activate the Virtual Environment**: Activating the environment ensures that all Python commands run within this isolated environment, preventing conflicts with other projects or system Python packages.

- **Install OpenCV**: Installs the OpenCV package for Python, necessary for computer vision tasks.

- **Install Matplotlib**: Installs Matplotlib, a plotting library that can be useful for visualizing data in Python scripts.

Make sure to run these commands in sequence to properly set up your environment for working with OpenCV and Matplotlib in Python.

