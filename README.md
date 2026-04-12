Este projeto apresenta um assistente de voz e texto integrado ao modelo Gemini, permitindo interações multimodais onde o usuário pode conversar via terminal ou por comandos de voz, recebendo respostas narradas por inteligência artificial.

🤖 Projeto Assistente de IA com Gemini
Este repositório contém uma solução de assistente virtual que utiliza a biblioteca da Google para processamento de linguagem natural e ferramentas de conversão de texto em fala (TTS) e fala em texto (STT).

🛠️ Tecnologias Utilizadas
Linguagem: Python.

IA Generativa: Google Generative AI (Gemini 2.5 Flash).

Conversão de Texto para Áudio (TTS): gTTS (Google Text-to-Speech).

Reconhecimento de Voz (STT): SpeechRecognition.

Gerenciamento de Ambiente: python-dotenv.

📂 Estrutura do Projeto
O projeto é dividido em módulos especializados para diferentes formas de interação:

config.py: Centraliza a configuração da API Key e a inicialização do modelo Gemini.

falacomigo.py: Interface de chat textual via terminal com histórico de conversação.

gravando.py: Assistente de voz completo que ouve o microfone, processa a pergunta no Gemini e responde com áudio.

voz_ia.py: Converte entradas de texto do usuário em respostas narradas pela IA.

fala.py: Um utilitário simples para converter textos digitados em arquivos .mp3.

🚀 Como Configurar
Chave de API:

Crie um arquivo chamado safe.env na raiz do projeto.

Adicione sua chave no formato: GEMINI_API_KEY=SUA_CHAVE_AQUI.

Instalação de Dependências:
Certifique-se de ter as bibliotecas instaladas:

Bash
pip install google-generativeai python-dotenv gTTS SpeechRecognition
Execução:

Para conversar por texto: python falacomigo.py.

Para usar o assistente de voz: python gravando.py.

🔍 Detalhes Técnicos e Segurança
Arquivos Ignorados: O projeto está configurado para não subir arquivos de ambiente (.env, safe.env), pastas de cache ou arquivos temporários de áudio (.mp3) para o repositório.

Tratamento de Erros: O sistema possui tratamento para erros de cota excedida (429) e modelos não encontrados (404).

Limpeza de Resposta: No assistente de voz, o código limpa caracteres especiais (como asteriscos de formatação) antes de gerar o áudio para garantir uma narração natural.

Nota: Este projeto foi desenvolvido como parte de um desafio de integração de IA.
