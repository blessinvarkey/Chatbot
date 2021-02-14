'''
Using the Chatterbot -corpus
Gets input from the user
Processes the input and returns value that generated the highest confidence value from logic adapters
Returns response to the user
'''
from flask import Flask, render_template, request
from chatterbot import Chatterbot
from chatterbot.trainers import ChatterbotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot('Chatterbot', storage_adapter="chatterbot.storage.SQLStorateAdapter")
trainer = ChatterbotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("get")
