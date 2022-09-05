import chatbot as mybot

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Index.html")


@app.route("/welcome")
def welcome():
    return render_template("Welcome.html")


@app.route("/register")
def register():
    return render_template("Register.html")


@app.route("/login")
def login():
    return render_template("Login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("Dashboard.html")


@app.route("/chatbot", methods=['POST', 'GET'])
def chatbot():
    question = "Hello"
    answer = "Hey there"
    if request.method == 'POST':
        question = request.form.get('question')
        answer = mybot.getmyresponse(question)
    return render_template('Chatbot.html', question=question, answer=answer)


if __name__ == "__main__":
    app.run()
