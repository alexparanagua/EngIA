import openai
import os
from dotenv import load_dotenv
from colorama import Fore, Style, init
import sys
import codecs

# Força o terminal a aceitar UTF-8 para todos os prints deste script
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

load_dotenv()
os.environ["PYTHONIOENCODING"] = "utf-8"

client = openai.Client()


init(autoreset=True)

def geracao_texto(mensagens):
    resposta = client.chat.completions.create(
        messages=mensagens,
        model="gpt-3.5-turbo-0125",
        temperature=0,
        max_tokens=1000,
        stream=True
    )
    print(f"{Fore.GREEN}Bot: ", end="")
    texto_completo = ""
    for resposta_stream in resposta:
        texto = resposta_stream.choices[0].delta.content
        if texto:
            print(texto, end="")
            texto_completo += texto
    print()
    mensagens.append({"role":"assistant", "content": texto_completo})
    return mensagens

if __name__ == "__main__":
# Substitui o emoji por algo legível se falhar
    print(f"{Fore.RED}Bem Vindo ao Chatbot\U0001f916".encode('utf-8', errors='ignore').decode('utf-8'))
    mensagens = []
    while True:
        in_user = input(f"{Fore.YELLOW}User: {Style.RESET_ALL}")
        mensagens.append({"role":"user", "content": in_user})
        mensagens = geracao_texto(mensagens)