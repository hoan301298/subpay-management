from fastapi import FastAPI

app = FastAPI(title="SubPay Management")

@app.get("/")
def root():
    return {"message": "SubPay API running"}