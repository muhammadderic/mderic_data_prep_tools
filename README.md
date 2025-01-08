# mderic-data-prep-tools

`mderic-data-prep-tools` is a lightweight Python library that provides reusable functions for my **data understanding** and **data preprocessing** tasks when working with **pandas DataFrames**.

This library is designed for data analysts, data scientists, and ML engineers who frequently explore and clean tabular datasets in Python.

## ✨ Features
- 📊 Quick data summary (shape, nulls, dtypes, uniques)

## 📦 Installation

### ✅ Option 1: Install via GitHub (e.g. for Google Colab)
```python
!pip install git+https://github.com/muhammadderic/mderic-data-prep-tools.git
```

### ✅ Option 2: Local Development Install
```python
git clone https://github.com/muhammadderic/mderic-data-prep-tools.git
cd mderic-data-prep-tools
pip install -e .
```

### 🚀 Usage
```python
import pandas as pd
from mderic-data-prep-tools import understanding

df = pd.read_csv("your_data.csv")

# Data understanding
summary = understanding.summarize(df)
```

### 📂 Modules
#### `understanding.py`
- `summarize(df)` → returns dict of shape, dtypes, null counts, unique counts.

### 📄 License
MIT License

### 🛠 Requirements
pandas >= 1.3.2

### 👤 Author
Your Name — [@muhammadderic](https://github.com/muhammadderic)

Feel free to contribute or fork!