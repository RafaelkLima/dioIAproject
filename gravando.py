import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
import os

from config import model

rec = sr.Recognizer()

def ouvir_microfone():
    with sr.Microphone() as source:
        # Ajusta o ruído ambiente para ouvir melhor
        rec.adjust_for_ambient_noise(source, duration=1)
        print("🎤 Pode falar, estou ouvindo...")
        
        try:
            audio = rec.listen(source, timeout=5)
            texto = rec.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")
            return texto
        except Exception:
            print("❌ Não entendi ou o tempo acabou.")
            return None

def responder_com_voz(texto_ia):
    print(f"IA: {texto_ia}")
    texto_limpo = texto_ia.replace('*', '') # Limpa negritos da IA
    tts = gTTS(text=texto_limpo, lang='pt')
    tts.save("resposta.mp3")
    os.system("start resposta.mp3")

# --- Loop Principal ---
print("--- ASSISTENTE DE VOZ ATIVADO ---")

while True:
    fala_usuario = ouvir_microfone()
    
    if fala_usuario:
        if "sair" in fala_usuario.lower():
            print("Encerrando...")
            break
            
        # Envia para o Gemini
        try:
            response = model.generate_content(fala_usuario)
            responder_com_voz(response.text)
        except Exception as e:
            print(f"Erro na IA: {e}")