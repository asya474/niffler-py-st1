from pydantic import BaseModel


class Envs(BaseModel):
    frontend_url:str
    gateway_url:str
    auth_url:str
    test_username:str
    test_password:str
    spend_db_url:str
    user_db_url:str
    userdata_db_url:str
    postgres_user:str
    postgres_password:str
    database_pool_size:int