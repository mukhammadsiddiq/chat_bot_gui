import openai
class ChatBot:
    def __init__(self):
        openai.api_key = "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"

    def get_responce(self, user_input):
        responce = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=300,
            temperature=0.5
           ).choices[0].text
        return responce


if __name__ == "__main__":
    chatbot = ChatBot()
    responce = chatbot.get_responce("make a trip for budapest.")
    print(responce)

