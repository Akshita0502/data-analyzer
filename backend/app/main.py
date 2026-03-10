from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import aisummary


app = FastAPI()

app.include_router(aisummary.router)

app.mount("/charts", StaticFiles(directory="charts"), name="charts")

origins = [
    "https://data-analyzer-git-main-akshita0502s-projects.vercel.app"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from app.routes.upload import router as upload_router # we are importing the router from the upload.py file and renaming it to upload_router.
from app.routes.analysis import router as analysis_router # we are importing the router from the analysis.py file and renaming it to analysis_router.
from app.routes.visualizations import router as visualization_router 

app.include_router(upload_router) # we are including the upload_router in our main app. this will allow us to access the endpoints defined in the upload.py file.
app.include_router(analysis_router) # we are including the analysis_router in our main app. this will allow us to access the endpoints defined in the analysis.py file.
app.include_router(visualization_router) # we are including the visualization_router in our main app. this will allow us to access the endpoints defined in the visualizations.py file.
@app.get("/")
def home():
    return{"message": "this is the api backend running."}
