from flask import Flask, render_template, request
app = Flask(__name__)
standard_answers = {
    "what is your name?":"My name is Sathvik Bot!"
}
chat_history = []

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
        ans = standard_answers.get(user_response.lower(),"Sorry, I could not understand")
        chat_history.append("You: "+user_response)
        chat_history.append("Me: "+ans)

        return render_template("chat.html", messages = chat_history)
app.run(debug=True)
