def chatbot_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "what is your name": "I am Bot360, here to assist you!",
        "how are you": "I'm just a program, but I'm functioning well!",
        "what is the capital of france": "The capital of France is Paris.",
        "tell me a joke": "Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",
        "how can I contact support": "To contact support, please visit our website or call our helpline at 123-456-7890.",
        "are you male or a female?": "I am a chatbot, and I don't have any gender.",
        "will you takeover the world?": "I don't have such power. If I had, I would have taken it... hehe, I was being sarcastic.",
        "what's the weather like today": "I'm sorry, I cannot provide real-time weather information. Please check a weather website or app for the current weather.",
        "tell me a fun fact": "Certainly! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "what's the meaning of life": "The meaning of life is a philosophical question that has been debated for centuries. Different people and cultures have different beliefs and interpretations. Some find meaning in relationships, experiences, or personal goals.",
        "who wrote the play romeo and juliet": "William Shakespeare wrote the play Romeo and Juliet.",
        "what is artificial intelligence": "Artificial intelligence is the science of making machines that can think like humans. It can do things that are considered smart.",
        "ohh": "Is there any other question with which I can help you?",
        "okay": "Is there any other question with which I can help you?",
        "exit": " Goodbye!",
        "hello": "Hello, I am Bot360, here to assist you!"
    }

    return responses.get(user_input, "I'm sorry, I don't have an answer for that.")

print("Chatbot: Hi there! I'm ChatBot. Feel free to ask me questions.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break