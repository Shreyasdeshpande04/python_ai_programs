from fastapi import APIRouter
import os
from app.memory.session_store import get_session
from app.services.ai_engine import AIEngine

router = APIRouter()
ai_engine = AIEngine()

@router.post("/chat/{session_id}")
async def chat_with_data(session_id: str, query: str):
    data = get_session(session_id)
    if not data:
        return {"error": "No session found"}
    
    df = data['df']
    
    # 1. Strict Prompt for Clean Text
    prompt = f"""
    Context: You are analyzing a dataset with columns {list(df.columns)}. 
    Data Snippet: {df.head(5).to_dict()}
    
    User Question: {query}
    
    Rules:
    - Give a direct, simple text answer.
    - Do NOT show Python code.
    - Do NOT show raw JSON.
    - Use bullet points if needed.
    """
    
    response = ai_engine.llm.get_ai_response(prompt)

    # 2. Save Q&A to a Text File
    history_path = f"exports/reports/{session_id}_chat_history.txt"
    os.makedirs("exports/reports", exist_ok=True)
    
    with open(history_path, "a", encoding="utf-8") as f:
        f.write(f"USER: {query}\n")
        f.write(f"AI: {response}\n")
        f.write("-" * 50 + "\n")

    return {
        "answer": response,
        "history_saved_at": history_path
    }