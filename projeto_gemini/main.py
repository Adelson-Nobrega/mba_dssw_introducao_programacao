import os
from google import genai
from dotenv import load_dotenv

# Carregar os dados presentes no .env
load_dotenv()

# Acessa a variável de ambiente API_KEY
API_KEY = os.environ.get('API_KEY')

client = genai.Client(api_key=API_KEY)

pergunta = input('Digite sua pergunta ao Gemini: ')

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=pergunta,
)

print(response.text)