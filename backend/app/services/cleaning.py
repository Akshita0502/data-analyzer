import pandas as pd

def calculate_missing_percentage(df):

    missing_report = {}
    cleaning_report = {}

    for col in list(df.columns):

        missing_percentage = round(df[col].isnull().mean()*100, 2)
        missing_report[col] = missing_percentage

        if missing_percentage == 0:
            cleaning_report[col] = "no action"

        elif missing_percentage < 5:
            df.dropna(subset=[col], inplace=True)
            cleaning_report[col] = "rows dropped"

        elif missing_percentage > 60:
            df.drop(columns=[col], inplace=True)
            cleaning_report[col] = "column dropped"

        else:

            if pd.api.types.is_numeric_dtype(df[col]):

                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1

                outliers = df[(df[col] < (Q1 - 1.5*IQR)) |
                              (df[col] > (Q3 + 1.5*IQR))]

                if len(outliers) > 0:
                    df[col].fillna(df[col].median(), inplace=True)
                    cleaning_report[col] = "filled median"
                else:
                    df[col].fillna(df[col].mean(), inplace=True)
                    cleaning_report[col] = "filled mean"

            else:
                df[col].fillna(df[col].mode()[0], inplace=True)
                cleaning_report[col] = "filled mode"

    return missing_report, cleaning_report