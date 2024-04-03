from dataclasses import dataclass
import random
from fastapi import FastAPI
import uvicorn
import string
import bcrypt
import hashlib


SECRET = "secret"  # should be taken from os.environ


@dataclass
class PasswordIn:
    min_chars: int = 6
    max_chars: int = 15
    contains_number: bool = False
    contains_uppercase: bool = False
    contains_special: bool = False


def generate_password(params: PasswordIn):
    chars = string.ascii_lowercase
    if params.contains_number:
        chars += "0123456789"
    if params.contains_uppercase:
        chars += string.ascii_uppercase
    if params.contains_special:
        ...
    length = random.randint(params.min_chars, params.max_chars)
    return "".join(random.choices(chars, k=length))


app = FastAPI()


# with open("passwords.txt") as f:
#     # read on start
#     f.read()


def hash_me(password):
    return hashlib.sha512((password + SECRET).encode("utf-8")).hexdigest()


@app.post("/password")
def generate(data: PasswordIn):
    password = generate_password(data)
    res = hash_me(password)
    print(res)
    print(type(res))

    hashed_password = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), SECRET.encode("utf-8"), 100000
    )
    # hashed_password.decode()
    with open("password.txt", "ab") as f:
        # f.write(res)
        f.write(hashed_password)
        f.write(b"\n")
    return password


@app.get("password")
def check_password():
    pass


if __name__ == "__main__":
    uvicorn.run("app3:app", host="0.0.0.0", port=5959, reload=True)
