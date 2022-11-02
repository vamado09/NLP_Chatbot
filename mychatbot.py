from flask import Flask, render_template, request
from chat import Chat_T

app = Flask(__name__)

#@app.route('/')
#def hello():
    #return "Hello, Flask";

@app.route('/')
def homepage():
    return render_template('main.html');

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    chat = Chat_T()
    return str(chat.chat(userText))

if __name__ == "__main__":
    app.run()