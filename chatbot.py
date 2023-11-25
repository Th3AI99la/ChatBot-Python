import openai

keyAPI = "a"

openai.api_key = keyAPI


def send_message(message_chat):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message_chat}],
    )

    return response["choices"][0]["message"]


while True:
    text = input("Escreva aqui sua mensagem:")

    if text == "sair":
        break
    else:
        response = send_message(text)
        print("Chatbot:", response)
