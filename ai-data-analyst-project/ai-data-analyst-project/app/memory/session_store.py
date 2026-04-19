# Simple in-memory storage (Real industry uses Redis/MongoDB)
sessions = {}

def save_session(session_id, df):
    sessions[session_id] = {
        "df": df,
        "history": []
    }

def get_session(session_id):
    return sessions.get(session_id)