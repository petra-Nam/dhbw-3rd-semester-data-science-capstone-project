import os
import pandas as pd

#save
def save_dataframe(df: pd.DataFrame, name: str, folder: str = "data"):
    """
    Save a DataFrame as a CSV inside the specified folder.
    If the file already exists, it will be overwritten (updated).

    Args:
        df (pd.DataFrame): DataFrame to save
        name (str): File name without extension (e.g., 'eda_output')
        folder (str): Folder path (default = 'data')

    Returns:
        str: Path to saved CSV file
    """
    os.makedirs(folder, exist_ok=True)
    path = f"{folder}/{name}.csv"

    # Check if file already exists
    if os.path.exists(path):
        print(f"File already exists. Overwriting {path}")
    else:
        print(f"Creating new file {path}")

    # Save or overwrite
    df.to_csv(path, index=False)
    print(f"DataFrame saved successfully.")
    return path
