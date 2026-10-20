
from fastapi import FastAPI

app = FastAPI(
    title="AI Job Application Tracker",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ai-job-application-tracker"
    }
