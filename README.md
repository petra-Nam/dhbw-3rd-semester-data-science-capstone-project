# Data Science Capstone Project
- Team Member: Petra, Atai, David ,Niki (Ngoc Lan Hua)

## Data Saving and Loading Guide

### Saving Updated Data


Whenever you finish working with or modifying a dataset in your notebook,  
you should **save (or update)** it inside the `data/` directory using the helper function:

```python
from utils import save_dataframe

# Example usage
save_dataframe(df, "eda_output")          # from 01_EDA.ipynb

```

### Loading Data in Another Notebook

```python

import pandas as pd
from utils import save_dataframe

df = pd.read_csv("data/eda_output.csv")
print(df.shape)
df.head()
```