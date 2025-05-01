from dotenv import load_dotenv
import os 

load_dotenv()

def get_openai_api_key():
   
   api_key = os.getenv("OPENAI_API_KEY","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")

   return api_key