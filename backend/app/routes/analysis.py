from fastapi import APIRouter
from app.services.cleaning import calculate_missing_percentage
from app import state   
 
router = APIRouter() # it will hold endpoints related to analysis.  
@router.get("/analysis") # this tells if a get request comes to the /analysis endpoint, then run the function below.
def analyze_dataset():

    if state.dataset is None: #if dataset is not uploaded give error.
        return{"error": "no dataset found!"}
    df = state.dataset
    missing_report, cleaning_report = calculate_missing_percentage(df)
    numeric_values = df.select_dtypes(include = "number") #selects numeric columms, to perform std,mean,median,mode.

    categorical_values = df.select_dtypes(exclude="number") #selects categorical columms, to perform mode.
    categorical_analysis = {} 

    for col in categorical_values.columns:
        unique_values = df[col].nunique() #get the number of unique values in the categorical column.
        total_rows = len(df) #get the total number of rows in the dataframe.
        if unique_values<(0.5*total_rows):
          categorical_analysis[col] = df[col].value_counts().to_dict() #get the count of each category in the categorical column and convert it into a dictionary.

    mean_values = numeric_values.mean().fillna(0).to_dict()
    median_values = {col: float(val) for col, val in numeric_values.median().items()}
    std_values = {col: float(val) for col, val in numeric_values.std().items()}
    min_values = {col: float(val) for col, val in numeric_values.min().items()}
    max_values = {col: float(val) for col, val in numeric_values.max().items()}
    variance_values = {col: float(val) for col, val in numeric_values.var().items()}
   
    
    #.mean() normal pandas syntax 
    #.mean().items() creates a key value pair of column name and mean value.
    #{col: float(val) for col, val in numeric_values.mean().items()} creates dictonary easy to read by json format. 
    #converts val to float json reads float and not numpy float.


    return {
        "columns": list(df.columns), #get the column names and convert it into a list.
        "mean" : mean_values,
        "median" : median_values,
        "std" : std_values,
        "min" : min_values,
        "max" : max_values,
        "variance" : variance_values,
        "missing_percentage" : missing_report,
        "cleaning_actions" : cleaning_report,
        "categorical_analysis" : categorical_analysis
        
    }   