from flask import Flask, render_template, request
app = Flask(__name__)
standard_answers = {
    "what is your name?":"My name is Sathvik Bot!"
}
chat_history = []
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
import joblib


'''
This is an example showing how to train a chat bot using the
ChatterBot Corpus of conversation dialog.
'''

# Enable info level logging
logging.basicConfig(level=logging.INFO)

chatbot = ChatBot('Example Bot')

# Start by training our bot with the ChatterBot corpus data
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    'chatterbot.corpus.english'
)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home", methods=['GET',"POST"])
def home():
    if request.method == "GET":
        name = request.args.get("username","Anonymous")
        msg = f"Me: Hello {name}! How can i help you?"
        chat_history.append(msg)
        return render_template("chat.html", messages=chat_history)
    else:
        user_response = request.form.get("input")
        ans = chatbot.get_response(user_response)
        # ans = standard_answers.get(user_response.lower(),"Sorry, I could not understand")
        chat_history.append("You: "+user_response)
        chat_history.append("Me: "+str(ans))

        return render_template("chat.html", messages = chat_history)
app.run(debug=True, threaded=False)
