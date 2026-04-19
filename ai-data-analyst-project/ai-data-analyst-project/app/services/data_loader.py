import pandas as pd

class DataLoader:
    @staticmethod
    def load_csv(file_path: str):
        df = pd.read_csv(file_path)
        # Clean column names (strip spaces, lowercase)
        df.columns = df.columns.str.strip().str.lower()
        return df