import requests
from email_classifier.utils import clean_email_text

class EmailClassifier:
    def __init__(self, ollama_url: str = "http://localhost:11434", model: str = "llama3"):
        """
        Initialize the email classifier with Ollama API settings.
        
        Args:
            ollama_url (str): URL of the Ollama API.
            model (str): Ollama model name.
        """
        self.ollama_url = ollama_url
        self.model = model

    def classify_email(self, email_text: str) -> str:
        """
        Classify an email's sentiment using Ollama's local LLM.
        
        Args:
            email_text (str): The email text to classify.
        
        Returns:
            str: Classification label (e.g., 'positive', 'negative', 'neutral').
        """
        cleaned_text = clean_email_text(email_text)
        if not cleaned_text:
            return "neutral"
        
        prompt = f"Classify the sentiment of this email as positive, negative, or neutral: {cleaned_text}"
        
        try:
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={"model": self.model, "prompt": prompt, "stream": False}
            )
            response.raise_for_status()
            result = response.json().get("response", "").lower()
            
            # Extract sentiment from response
            if "positive" in result:
                return "positive"
            elif "negative" in result:
                return "negative"
            else:
                return "neutral"
        except requests.RequestException as e:
            print(f"Error communicating with Ollama: {e}")
            return "neutral"