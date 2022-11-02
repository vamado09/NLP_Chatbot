from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

class Chat_T:
    chatbot: None

    def __init__(self):
        self.chatbot = ChatBot("ChatBot")
    # Training with Personal Ques & Ans
        conversation = [
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "Thank you!",
            "You're welcome.",
            "who developed you?",
            "NLP class",
            "Do you enjoy being a chatbot?",
            "Not really lol",
            "What can you do?",
            "Not much, I was born today...",
            "Do you think NLP is useful?",
            "Yes, I do. It is an awesome field.",
            "Terminator 1 or Terminator 2?",
            "Both films were awesome",
            "Do you love me?",
            "No, go away."
        ]
        trainer = ListTrainer(self.chatbot)
        trainer.train(conversation)

    def chat(self, t1):
        response = self.chatbot.get_response(t1)
        return response