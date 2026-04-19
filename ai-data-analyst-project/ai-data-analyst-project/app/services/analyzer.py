import pandas as pd

class DataAnalyzer:
    @staticmethod
    def analyze(df: pd.DataFrame):
        # We extract facts so we don't send a huge file to the AI
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        
        analysis_results = {
            "total_records": len(df),
            "columns": df.columns.tolist(),
            "stats": df[numeric_cols].describe().to_dict() if numeric_cols else "No numeric data",
            "top_rows": df.head(3).to_dict(orient='records')
        }
        return analysis_results