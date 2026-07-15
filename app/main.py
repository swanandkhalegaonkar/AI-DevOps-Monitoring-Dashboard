from fastapi import FastAPI

app = FastAPI(
    title="AI DevOps Monitoring Dashboard",
    version="1.0.0",
    description="A FastAPI application for monitoring system metrics and AI-based analysis."
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI DevOps Monitoring Dashboard 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }