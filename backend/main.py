from fastapi import FastAPI

app = FastAPI(
    title="Jarvis AI",
    description="AI Assistant Backend",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "assistant": "Jarvis",
        "status": "Online",
        "message": "Welcome Kan! Your AI backend is running successfully."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }