import os
import pandas as pd

def save_dataframe(df: pd.DataFrame, name: str, folder: str = "data"):
    """
    Save a DataFrame as a CSV inside the project root data folder.
    Works even if the notebook runs from a subfolder (e.g., /notebooks).
    """
    # Always create path relative to project root
    root_path = os.path.dirname(os.getcwd())  # go one level up
    data_path = os.path.join(root_path, folder)
    os.makedirs(data_path, exist_ok=True)

    path = os.path.join(data_path, f"{name}.csv")

    if os.path.exists(path):
        print(f"File already exists. Overwriting {path}")
    else:
        print(f"Creating new file {path}")

    df.to_csv(path, index=False)
    print("DataFrame saved successfully.")
    return path
