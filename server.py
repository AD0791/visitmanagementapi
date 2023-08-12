from fastapi import FastAPI, status

#TODO configure with the settings
app = FastAPI(
    title= "Visit Management Services",
    description="Service will handle request/response for the mobile and the web application",
    summary= "The service allows the employees to register and manage visits from guests to their office location",
    version= "v0.0.1",
)

@app.get("/",tags=["Home"],description="home endpoint",status_code=status.HTTP_200_OK)
def home():
    return {"message":"This is the root of the V.M application"}
