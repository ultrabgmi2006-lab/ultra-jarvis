from flask import Flask, request

app = Flask(__name__)

command = ""

@app.route("/")
def home():
    return "Jarvis cloud server running"

@app.route("/command")
def get_command():
    global command
    cmd = command
    command = ""
    return cmd

@app.route("/send")
def send_command():
    global command
    command = request.args.get("cmd")
    return "Command received"

app.run(host="0.0.0.0", port=5000)
