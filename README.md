# FreezeLibs

[![PyPI Version](https://img.shields.io/pypi/v/FreezeLibs)](https://pypi.org/project/FreezeLibs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**FreezeLibs** is a Python library that helps you extract and save the imported libraries from Python files or projects. It generates a `requirements.txt` file in either of the following formats:
- Without versions (for simplicity).
- With versions (for reproducibility).

---

## Features

- Extract imported libraries from a single Python file or an entire project directory.
- Generate `requirements.txt` in two formats:
  - Without versions (e.g., `numpy`).
  - With versions (e.g., `numpy==1.23.5`).
- Handle libraries with different import and install names (e.g., `cv2` → `opencv-python`).
- Easy-to-use command-line interface (CLI).

---

## Installation

You can install **FreezeLibs** using `pip`:

```bash
pip install FreezeLibs
