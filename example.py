import requests
from requests.auth import HTTPBasicAuth

URL = "http://127.0.0.1:5000"
USER = "yael"
PASSWORD = "123456"

def register(user: str, password: str) -> str:
    data = {"username": user, "password": password}
    response = requests.post(f"{URL}/register", json=data)
    return response.json()["message"]


def authenticate(user: str, password: str) -> str:
    auth = HTTPBasicAuth(user, password)
    response = requests.post(f"{URL}/login", auth=auth)
    return response.json()["token"]

def login(token: str):
    response = requests.get(f"{URL}/user", headers={"Authorization": token})
    return response.json()

def get_file_permissions(token: str, file: str):
    response = requests.get(f"{URL}/file_permissions", headers={"Authorization": token}, json={"file": file})
    return response.json()


# unauthorized
register("yael", "123456")
token = authenticate("yael", "123456")
login(token)
get_file_permissions(token, "file1")


# working permissions
token = authenticate("user1", "adminpass")
login(token)
get_file_permissions(token, "file1")