from fastapi import APIRouter, UploadFile, File  
# we are uploading a file, so we need UploadFile and File
# why we need apirouter? because we want to create a separate route for uploading files, and we want to keep our code organized. 
# We can create a separate file for uploading files and then include that file in our main.py file. 
# This way, we can keep our code organized and maintainable.

# what is apirouter? it is a class that allows us to create a separate route for uploading files. 
# not only for uploading files, but we can create separate routes for different functionalities.


import pandas as pd # we are using pandas to read the csv file and convert it into a dataframe.
from app import state 
router = APIRouter() # it will hold endpoints related to uploading files.
@router.post("/upload") # this tells if a post comes to the /upload endpoint, then run the function below.
async def upload_file(file: UploadFile = File(...)): 
    
    # aysnc makes it async so we can handle multiple requests at the same time.
    #def upload_file is the func name 
    #file: UploadFile expect a file input called file. the file will store in file variable.
    #file(...) means mark this parameter as required. if we don't provide a file, it will return an error.

    if file.filename.endswith(".csv"): #checks for the upload
        # read it 
        df = pd.read_csv(file.file) # read the csv file and convert it into a dataframe.
        state.dataset = df
    elif file.filename.endswith(".xlsx"):
        df = pd.read_excel(file.file) # read the excel file and convert it into a dataframe.
        state.dataset = df
    
    else:
        return {"error": "Unsupported file type. Please upload a CSV or Excel file."} 
   
    
    rows, columns = df.shape 
    rows = int(rows) 
    columns = int(columns) # get the number of rows and columns in the dataframe.
    missing_values = {col: int(val) for col, val in df.isnull().sum().items()} # get the total number of missing values in the dataframe.
    preview = df.head().replace({float("nan"): None}).to_dict(orient="records")
    column_types = {col: str(dtype) for col, dtype in df.dtypes.items()}
    
    # get the first 5 rows of the dataframe and convert it into a list of dictionaries.
    
    return{
        "rows" : rows,
        "columns" : columns,
        "missing_values" : missing_values,
        "preview" : preview,
        "column_types": column_types
    }

 




