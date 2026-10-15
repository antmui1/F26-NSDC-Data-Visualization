import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

data_path = Path(__file__).with_name("Inequality in Education.csv")
data = pd.read_csv(data_path)
print(data.head(10))
