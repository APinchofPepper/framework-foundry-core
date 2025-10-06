from fastapi import FastAPI

app = FastAPI(title="Framework Foundry Core API")

@app.get("/")
def root():
    return {"message": "Framework Foundry Core API running"}
