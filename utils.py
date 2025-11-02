import os
import pandas as pd

def save_dataframe(df: pd.DataFrame, name: str, folder: str = "data"):
    """
    Save a DataFrame as a CSV
    """
    # Go one level up from notebooks (to project root)
    root_path = os.path.dirname(os.getcwd())

    # Get the project folder name ('capstone-project')
    project_name = os.path.basename(root_path)

    # Construct data folder path
    data_path = os.path.join(root_path, folder)
    os.makedirs(data_path, exist_ok=True)

    # Full file path
    path = os.path.join(data_path, f"{name}.csv")

    # Display-friendly path (capstone-project/data/eda_output.csv)
    display_path = os.path.join(project_name, folder, f"{name}.csv")


    if os.path.exists(path):
        print(f"File already exists. Overwriting {display_path}")
    else:
        print(f"Creating new file {display_path}")


    df.to_csv(path, index=False)
    print("DataFrame saved successfully.")
    return path
