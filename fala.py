
import os 
from gtts import gTTS

fala = input("Digite a fala que deseja converter para áudio: ")
print("Convertendo fala para áudio...")
tts = gTTS(text=fala, lang='pt')
tts.save("fala.mp3")

os.system("start fala.mp3")
