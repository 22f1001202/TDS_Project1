# /// script 
# requires-python = ">=3.11"
# dependencies = [
#     "fastapi",
#     "uvicorn",
#     "requests"
# ]
# ///

from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware  

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods = ['GET', 'POST'],
    allow_headers = ["*"]
)

@app.get("/")
def home():
    return {"hello world"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
