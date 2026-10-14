import sys
from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
import seaborn as sns
import sklearn

print(f"Python version: {sys.version.split()[0]}")
print(f"Python interpreter: {sys.executable}")
print("\nRequired packages imported successfully:")
print(f"pandas: {pd.__version__}")
print(f"numpy: {np.__version__}")
print(f"matplotlib: {matplotlib.__version__}")
print(f"seaborn: {sns.__version__}")
print(f"plotly: {plotly.__version__}")
print(f"scikit-learn: {sklearn.__version__}")
data = pd.read_csv("data/week-3/Inequality in Education.csv")
data["Country", "ISO3"]