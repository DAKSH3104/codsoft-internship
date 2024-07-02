data={
    "hi":"Hi there! I'm a friendly chatbot here to assist you?",
    "what is favorite color":"blue no yellow!hmm, i am glad this is not one of those one guess only situations?",
    "what is your name":"I'm just a chatbot,so I don't have a name, but you can call me ChatBot.",
    "where are you from":"I'm from the digital world,always ready to chat!",
    "how are you":"I'm just a chatbot,but I'm here to assist you.",
    "who is my best friend?":"will i like to nominate my self for that position!",
    "what is your favorite car?":"I'm a chatbot,so I don't like cars but i preferenes for a simple walk.",
    "what's your favorite color?":"I'm a chatbot,so I don't have personal preferences for colors.",
    "what is your favorite song?":"I stream all kinds of music in the cloud!",
    "bye":"Bye! Take care and have a great day!",
}
def get_response(user_input):
    for pattern,response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry,I didn't understand that.Can you please rephrase your sentence?"
print("Chatbot: Hi! I'm a simple chatbot,I'm here to assist you!")
while True:
    user_input=input("Me: ")
    if user_input=='bye':
       print("Chatbot: Goodbye! Have a great day!")
       break
    response=get_response(user_input)
    print("Chatbot:",response)
    