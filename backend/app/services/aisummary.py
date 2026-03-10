def generate_ai_summary(df):

    rows, cols = df.shape
    columns = list(df.columns)

    missing = df.isnull().sum()
    total_missing = missing.sum()

    numeric_cols = df.select_dtypes(include="number").columns
    categorical_cols = df.select_dtypes(exclude="number").columns

    summary = f"This dataset contains {rows} rows and {cols} columns.\n\n"

    summary += f"The columns include: {', '.join(columns)}.\n\n"

    summary += f"There are {len(numeric_cols)} numeric columns and {len(categorical_cols)} categorical columns.\n\n"

    if total_missing > 0:
        summary += "Some columns contain missing values which may require cleaning or imputation.\n\n"
    else:
        summary += "There are no missing values in this dataset.\n\n"

    summary += "This dataset appears to be structured tabular data suitable for statistical analysis and visualization."

    return summary