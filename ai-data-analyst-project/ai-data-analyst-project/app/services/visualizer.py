import os
import matplotlib.pyplot as plt
import seaborn as sns
from app.services.code_executor import CodeExecutor

class AIVisualizer:
    @staticmethod
    def generate_ai_charts(ai_engine, df, session_id):
        summary = f"Columns: {list(df.columns)}. Sample: {df.head(2).to_dict()}"
        
        prompt = f"""
        Task: Create a Seaborn chart for this data: {summary}
        Rules:
        1. Use plt.figure(figsize=(10,6)).
        2. Save the file exactly as: plt.savefig('exports/{session_id}_chart.png', bbox_inches='tight').
        3. Do NOT use plt.show() or inplace=True.
        4. Ensure the plot is professional with titles and labels.
        Return ONLY the Python code. No text. No backticks.
        """
        
        viz_code = ai_engine.llm.get_ai_response(prompt)
        _, status = CodeExecutor.run_with_self_correction(ai_engine, viz_code, df)
        return status