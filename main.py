from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/test")
def start(s):
    return {"messege": "welcome user!"}

@app.get("/test/:{name}")
def save_user(s):
    return {"messege": "saved user"}


@app.post("/caasar")
def caesar(s):
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
