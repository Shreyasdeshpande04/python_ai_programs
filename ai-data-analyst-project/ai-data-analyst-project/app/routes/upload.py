from fastapi import APIRouter, UploadFile, File
import shutil
import uuid
import os
from app.services.data_loader import DataLoader
from app.services.data_manager import DataManager
from app.services.visualizer import AIVisualizer
from app.services.ai_engine import AIEngine
from app.memory.session_store import save_session

router = APIRouter()
data_manager = DataManager()
ai_engine = AIEngine()

@router.post("/upload")
async def handle_upload(file: UploadFile = File(...)):
    # 1. Unique ID for this session
    session_id = str(uuid.uuid4())[:8]
    
    # 2. Save file
    file_path = f"uploads/{session_id}_{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 3. Load & Clean Autonomously
    raw_df = DataLoader.load_csv(file_path)
    cleaned_df, cleaning_status = data_manager.clean_data_autonomously(raw_df)

    # 4. Generate AI Visuals
    chart_status = AIVisualizer.generate_ai_charts(ai_engine, cleaned_df, session_id)

    # 5. Get AI Business Insight (Executive Report)
    report = ai_engine.generate_insights(cleaned_df.head(10).to_dict())

    # --- NEW: SAVE INITIAL REPORT TO FILE ---
    report_folder = "exports/reports"
    os.makedirs(report_folder, exist_ok=True)
    report_file_path = f"{report_folder}/{session_id}_executive_summary.txt"
    
    with open(report_file_path, "w", encoding="utf-8") as f:
        f.write("========================================\n")
        f.write(f"EXECUTIVE SUMMARY FOR: {file.filename}\n")
        f.write(f"SESSION ID: {session_id}\n")
        f.write("========================================\n\n")
        f.write(report)
    # ----------------------------------------

    # 6. Save to Memory for Chatting
    save_session(session_id, cleaned_df)

    return {
        "session_id": session_id,
        "cleaning_status": cleaning_status,
        "ai_report": report,
        "report_saved_at": report_file_path,
        "chart_path": f"/static/{session_id}_chart.png",
        "message": "Executive summary has been saved to the reports folder."
    }