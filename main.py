from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Request
def hello_world(): # Response
    return {"Message": "Hello World!"}


