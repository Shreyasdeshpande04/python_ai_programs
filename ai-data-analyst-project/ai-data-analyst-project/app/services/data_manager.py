import pandas as pd
from app.services.code_executor import CodeExecutor
from app.services.ai_engine import AIEngine

class DataManager:
    def __init__(self):
        self.ai_engine = AIEngine()
        self.executor = CodeExecutor()

    def clean_data_autonomously(self, df: pd.DataFrame):
        profile = {
            "columns": list(df.columns),
            "sample": df.head(2).to_dict()
        }

        cleaning_prompt = f"""
        You are a Data Engineer. Use Modern Pandas 3.0.
        Data: {profile}
        Rules:
        1. NEVER use 'inplace=True'. Use direct assignment: df['col'] = df['col'].method().
        2. Convert date-looking columns to datetime.
        3. Fill nulls appropriately.
        4. The final dataframe must be named 'df_cleaned'.
        Return ONLY the Python code. No text. No backticks.
        """
        
        cleaning_code = self.ai_engine.llm.get_ai_response(cleaning_prompt)
        cleaned_df, status = self.executor.run_with_self_correction(
            self.ai_engine, cleaning_code, df
        )
        return cleaned_df, status