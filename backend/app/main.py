from fastapi import FastAPI

app = FastAPI(title="Graph Supply Chain Risk Analyzer")


@app.get("/")
def root():
    return {"message": "Backend is running"}