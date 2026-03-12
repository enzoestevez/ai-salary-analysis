def build_dataset_context(df):
    """
    Devuelve un resumen textual del dataset que usará la IA.
    """
    overview = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict()
    }
    context = f"Dataset has {overview['rows']} rows and {overview['columns']} columns.\n"
    context += f"Columns: {', '.join(overview['column_names'])}\n"
    context += "Missing values: " + ", ".join([f"{k}: {v}" for k, v in overview['missing_values'].items()])
    return context