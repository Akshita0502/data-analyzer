import seaborn as sns
from fastapi import APIRouter
from app import state
import matplotlib.pyplot as plt
import os


router = APIRouter()

@router.get("/visualization")
def visualize_data():

    if state.dataset is None:
        return {"error": "no dataset found!"}

    df = state.dataset

    charts = []

    # create charts folder if not present
    os.makedirs("charts", exist_ok=True)

    total_rows = len(df)

    # ---------- HISTOGRAMS (NUMERIC COLUMNS) ----------
    numeric_values = df.select_dtypes(include="number")

    for col in numeric_values.columns:

        plt.figure()

        numeric_values[col].hist(bins=15)

        plt.title(f"Distribution of {col}")

        plt.xlabel(col)               # x axis = values of column
        plt.ylabel("Frequency")       # y axis = number of records

        filename = f"charts/{col}_histogram.png"

        plt.savefig(filename)

        plt.close()

        charts.append(f"{col}_histogram.png")

    # ---------- PIE CHARTS (CATEGORICAL COLUMNS) ----------
    categorical_values = df.select_dtypes(exclude="number")

    for col in categorical_values.columns:

        # avoid messy pie charts
        if df[col].nunique() <= 10:

            plt.figure()

            df[col].value_counts().plot.pie(
                autopct="%1.1f%%",
                startangle=90
            )

            plt.ylabel("")  # remove useless y-axis label

            plt.title(f"{col} Distribution in Dataset (Total Rows: {total_rows})")

            filename = f"charts/{col}_pie.png"

            plt.savefig(filename)

            plt.close()

            charts.append(f"{col}_pie.png")
     # ---------------- CORRELATION HEATMAP ----------------
    if numeric_values.shape[1] > 1:

        plt.figure(figsize=(8,6))

        correlation = numeric_values.corr()

        sns.heatmap(
            correlation,
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )

        plt.title("Correlation Heatmap Between Numeric Features")

        filename = "charts/correlation_heatmap.png"

        plt.savefig(filename)

        plt.close()

        charts.append("correlation_heatmap.png")


    return {
        "charts": charts
    }