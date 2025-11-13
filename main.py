from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/test")
def start():
    return {"messege": "welcome user!"}

@app.get("/test/:name")
def save_user():
    return {"messege": "saved user"}


@app.post("/caasar")
def caesar():
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
