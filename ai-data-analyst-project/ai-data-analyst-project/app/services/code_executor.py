import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

class CodeExecutor:
    @staticmethod
    def clean_ai_code(code_text: str):
        clean_code = re.sub(r"```python|```", "", code_text)
        return clean_code.strip()

    @staticmethod
    def run_with_self_correction(ai_engine, code: str, df: pd.DataFrame, max_retries=3):
        pd.options.mode.copy_on_write = True
        attempts = 0
        current_code = CodeExecutor.clean_ai_code(code)
        
        while attempts < max_retries:
            try:
                local_vars = {'df': df, 'plt': plt, 'sns': sns, 'pd': pd}
                exec(current_code, {}, local_vars)
                
                if 'df_cleaned' in local_vars:
                    return local_vars['df_cleaned'], "Success"
                return df, "Success"
                
            except Exception as e:
                attempts += 1
                error_msg = str(e)
                correction_prompt = f"""
                The following Python code failed:
                {current_code}
                Error: {error_msg}
                Fix the code. Use modern Pandas 3.0 syntax. Do NOT use inplace=True. 
                Return ONLY the Python code block.
                """
                raw_new_code = ai_engine.llm.get_ai_response(correction_prompt)
                current_code = CodeExecutor.clean_ai_code(raw_new_code)
        
        return df, "Failed after retries"