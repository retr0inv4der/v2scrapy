from dataclasses import dataclass 
from dotenv import load_dotenv
import os


@dataclass
class Config :
    api_hash : str
    api_id : int 
    botname : str
    mode : int = 1 





def load_configs() : 
    mode = 1
    if mode == 1 : 
        load_dotenv("config/dev.env")
    elif mode == 2 : 
        load_dotenv("config/prod.env")

    return Config(
        botname= os.getenv("BOTNAME") , 
        api_hash=os.getenv("API_HASH") ,
        api_id= int(os.getenv("API_ID")),
        mode=mode)
    

config = load_configs()