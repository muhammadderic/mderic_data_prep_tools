import pandas as pd

def summarize(df):
  return {
    "shape": df.shape,
    "dtypes": df.dtypes,
    "null_counts": df.isnull().sum(),
    "unique_counts": df.nunique()
  }
