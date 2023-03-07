import os
import openai
from voiceassistant import *

openai.api_key = "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"
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

#> This Function is Create an openai Object That Will Handle Making Requests For you.
def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

#> This Function Grab all your History (input,output) and use it in calling the openai_create that will take those Histories + input to generate a response based on This Chat History
def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, output

#> Order Dyal List when i asked Him: What is the last question i asked He responsed me with the first item in set , so you think what i'm thinking about
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
#> This is one is fill up every time we talk with chatbot and he use those History to generate new responses
history = []
print("Chatbot is ready. Type 'quit' to exit.")

while True:
    # user_input = input("Human: ")
    user_input = input("You: ") + "you are a chat bot so answer this question :"
    if user_input.lower() == "quit":
        break
    history, response = chatgpt_clone(user_input, history)

    if ("write me the code" in user_input.lower()):
        print("AI:" + response)
    engine.say(response)
    engine.runAndWait()