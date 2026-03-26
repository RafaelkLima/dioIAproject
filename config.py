import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv("safe.env") 

CHAVE_API = os.getenv("GEMINI_API_KEY") 
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-2.5-flash')

