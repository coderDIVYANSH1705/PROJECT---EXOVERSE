import openai 
open.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.chatcompletion.create(
        model = "gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]\
    )

    return response.choices[0].messages.content.strip()
if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit" , "exit" , "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("chatbox:" , response)
        