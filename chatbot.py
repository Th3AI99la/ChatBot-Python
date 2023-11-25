import openai

keyAPI = "sk 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"

openai.api_key = keyAPI


def send_message(message_chat):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message_chat}],
    )

    return response["choices"][0]["message"]


print(send_message("Em que ano o Brasil foi descoberto?"))
