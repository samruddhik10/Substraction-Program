from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Subtraction API is running"}

@app.get("/subtract")
def subtract(num1: float, num2: float):
    result = num1 - num2

    return {
        "num1": num1,
        "num2": num2,
        "result": result
    }