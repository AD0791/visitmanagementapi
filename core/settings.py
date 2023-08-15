from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    project_title = "Visit Management Services"
    project_description = "Service will handle request/response for the mobile and the web application"
    project_summary = "The service allows the employees to register and manage visits from guests to their office location"
    project_version = "v0.0.1",

    environment: str = Field(...,env='ENVIRONMENT')
    db_name: str = Field(...,env='DB_NAME')
    db_user: str = Field(...,env='DB_USER')
    db_password: str = Field(...,env='DB_PASSWORD')
    db_root_password: str = Field(...,env='DB_ROOT_PASSWORD')
    db_host: str = Field(...,env='DB_HOST')
    db_port: str = Field(...,env='DB_PORT')
    
    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"

    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance,cls):
            cls._instance = object.__new__(cls,*args,**kwargs)
        return cls._instance



settings=Settings()

