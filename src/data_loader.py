import pandas as pd


def load_dataset(file_path):
    """
    Load dataset from CSV file
    """
    df = pd.read_csv(file_path)
    return df


def dataset_overview(df):
    """
    Return basic information about the dataset
    """
    overview = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "missing_values": df.isnull().sum().to_dict()
    }

    return overview