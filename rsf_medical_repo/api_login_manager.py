import os
import openai
from huggingface_hub import login as hf_login

class APILoginManager:
    def __init__(self, hf_api_key=None, openai_api_key=None):
        """
        Initializes the login manager with optional API keys.

        Args:
            hf_api_key (str, optional): Hugging Face API key.
            openai_api_key (str, optional): OpenAI API key.
        """
        self.hf_api_key = hf_api_key
        self.openai_api_key = openai_api_key

    def login_huggingface(self):
        """Logs in to the Hugging Face API if the key is provided."""
        if self.hf_api_key:
            hf_login(self.hf_api_key)
            print("✅ Successfully logged in to Hugging Face!")
        else:
            print("❌ Hugging Face API key not provided.")

    def login_openai(self):
        """Logs in to the OpenAI API if the key is provided."""
        if self.openai_api_key:
            os.environ["OPENAI_API_KEY"] = self.openai_api_key  # Set API key as env variable
            openai.api_key = self.openai_api_key
            print("✅ Successfully logged in to OpenAI!")
        else:
            print("❌ OpenAI API key not provided.")