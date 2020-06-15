# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from main.python.chatbot.main import chat

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        reply = chat(message)

        self.send(text_data=json.dumps({
            'message': reply
        }))