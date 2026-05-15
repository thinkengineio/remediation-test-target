import hashlib
import requests

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_token(token: str) -> dict:
    resp = requests.get("https://auth.example.com/verify",
                        params={"token": token})
    return resp.json()
