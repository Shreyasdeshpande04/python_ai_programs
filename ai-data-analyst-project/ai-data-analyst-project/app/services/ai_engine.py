from app.llm.llm_client import LlamaClient

class AIEngine:
    def __init__(self):
        self.llm = LlamaClient()

    def generate_insights(self, data_facts: dict):
        # This is where Prompt Engineering happens
        prompt = f"""
        Analyze this dataset summary and give me a professional business report.
        Data Facts: {data_facts}
        
        Please provide:
        1. Executive Summary
        2. Three Key Insights
        3. One Problem identified
        4. Recommendation for the manager
        """
        return self.llm.get_ai_response(prompt)