import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

class GeminiDocumentGenerator:
    def __init__(self):
        self.client = genai.Client()
        self.model_name = os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip()
        if self.model_name.startswith("models/"):
            self.model_name = self.model_name.replace("models/", "")

    def generate_document(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        prompt = (
            f"Generate a formal legal document.\n"
            f"Document Type: {document_type}\n"
            f"Parties Involved: {parties}\n"
            f"Terms & Conditions: {terms}\n"
            f"Effective Dates: {dates}\n"
        )

        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                )
                return response.text
            except Exception as e:
                # Catch both 503 Overloaded and 429 Rate Limit errors
                if ("429" in str(e) or "503" in str(e)) and attempt < max_retries - 1:
                    # Wait 15 seconds before retrying on rate limits
                    time.sleep(15)
                    continue
                raise e