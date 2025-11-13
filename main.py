from fastapi import FastAPI
import uvicorn
from cipher_code import CaesarCode
app = FastAPI()
a = CaesarCode.caesar_code("hello world",3)
@app.get("/test")
def start(s):
    return {"messege": "welcome user!"}

@app.get("/test/:{name}")
def save_user(s):
    with open("name.txt", "a") as f:
        pass
    return {"messege": "saved user"}


@app.post("/caesar")
def caesar(s):
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
    print(a)
