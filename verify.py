import os
import requests
import json


def get_csrf_token() -> str:
    response = requests.post(
        url="https://auth.roblox.com/v2/login",
        cookies={".ROBLOSECURITY": os.environ.get("security_key")}
    )

    return response.headers["x-csrf-token"]



def get_auth_user() -> tuple[bool, str]:


    response = requests.get(
        url="https://users.roblox.com/v1/users/authenticated",
        headers={"x-csrf-token": get_csrf_token()},
        cookies={".ROBLOSECURITY": os.environ.get("security_key")}
    )
    
    if response.status_code != 200:
        return False, None
  
    return True, json.loads(response.content)



    
