from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

# Import our advanced routes
from app.routes import upload, chat

app = FastAPI(
    title="Elite AI Data Analyst",
    description="Autonomous Data Cleaning, Visualizing, and Chat Agent"
)

# 1. Enable CORS (Crucial for the 'Failed to Fetch' fix)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Ensure system folders exist
folders = ["uploads", "exports", "exports/charts", "exports/reports"]
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# 3. Mount 'exports' so you can see charts in your browser
# Example: http://localhost:8000/static/my_chart.png
app.mount("/static", StaticFiles(directory="exports"), name="static")

# 4. Include Routers
app.include_router(upload.router, prefix="/api", tags=["Data Processing"])
app.include_router(chat.router, prefix="/api", tags=["AI Chat Agent"])

@app.get("/")
def health_check():
    return {
        "status": "Online",
        "engine": "Llama-3.3-70b-versatile",
        "features": ["Autonomous Cleaning", "Self-Correction", "AI-Visualizer"]
    }

if __name__ == "__main__":
    import uvicorn
    # Using 127.0.0.1 is more stable for local testing than 0.0.0.0
    uvicorn.run(app, host="127.0.0.1", port=8000)