import openai
from dotenv import load_dotenv
import os

# Carregue variáveis de ambiente do arquivo key.env
load_dotenv("key.env")

# Use a chave de API carregada do arquivo key.env
openai.api_key = os.getenv("OPENAI_API_KEY")


def send_message(message_chat):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message_chat}],
        )
        return response["choices"][0]["message"]
    except Exception as e:
        print(f"Erro ao interagir com a API: {e}")
        return None


def main():
    print("\nBem-vindo ao Chatbot interativo! Digite 'sair' para encerrar.")

    while True:
        user_input = input("Você: ")

        if user_input.lower() == "sair":
            print("Até logo!")
            break

        response = send_message(user_input)

        if response:
            print("Chatbot:", response)
        else:
            print("Algo deu errado. Por favor, tente novamente.")


if __name__ == "__main__":
    main()
