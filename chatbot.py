# Develop an elementary chatbot for any suitable customer interaction application
print("Contoso Chatbot")

def chatbot():
  print("Hello, I am Contoso Chatbot. How can I help you today?")
  while True:
    user_input = input("User: ")
    if user_input == "exit":
      print("Contoso Chatbot: Goodbye!")
      break
    print("Contoso Chatbot: I am sorry, I am a simple chatbot and I do not understand that.")

chatbot()


