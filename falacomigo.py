import google.generativeai as genai
import os

from config import model

# Inicia o histórico do chat para a IA "lembrar" do que vocês falaram antes
chat = model.start_chat(history=[])

def limpar_tela():
    # Limpa o terminal para o chat ficar bonito (Windows)
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()
print("--- 🤖 GEMINI CHAT INICIADO ---")
print("Digite sua mensagem ou 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("\nEncerrando o chat. Até logo!")
        break

    try:
        # Envia a mensagem para a IA
        response = chat.send_message(pergunta)
        
        # Exibe a resposta formatada
        print(f"\nIA: {response.text}\n")
        print("-" * 30)

    except Exception as e:
        if "429" in str(e):
            print("\n❌ Erro: Cota excedida. Aguarde alguns segundos antes de perguntar novamente.")
        elif "404" in str(e):
            print("\n❌ Erro: Modelo não encontrado. Verifique o nome do modelo no código.")
        else:
            print(f"\n❌ Ocorreu um erro: {e}")