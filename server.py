from fastapi import FastAPI, status
from core.settings import settings

app = FastAPI(
    title= settings.project_title,
    description=settings.project_description,
    summary= settings.project_summary,
    version= settings.project_version
)

@app.get("/",tags=["Home"],description="home endpoint",status_code=status.HTTP_200_OK)
def home():
    return {"message":"This is the root of the V.M application"}
