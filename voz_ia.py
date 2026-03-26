import google.generativeai as genai
from gtts import gTTS
import os

from config import model

def gerar_resposta(texto):
    print(f"IA: {texto}")
    tts = gTTS(text=texto, lang='pt-br')
    tts .save("resposta.mp3")
    os.system("start resposta.mp3")

print("--- Olá! Eu sou a IA do seu assistente de voz. Digite algo para eu responder ou 'sair' para encerrar o programa. ---")    

while True:
    entrada_usuario = input("Você: ")
    if entrada_usuario.lower() == "sair":
        print("Encerrando o programa. Até mais!")
        break
    resposta_ia = model.generate_content(entrada_usuario)
    gerar_resposta(resposta_ia.text)