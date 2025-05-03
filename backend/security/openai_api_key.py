from dotenv import load_dotenv
import os 

load_dotenv()

def get_openai_api_key():
   
   api_key = os.getenv("OPENAI_API_KEY")

   return api_key
