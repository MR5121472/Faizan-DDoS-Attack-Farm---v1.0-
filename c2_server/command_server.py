# c2_server/command_server.py
from flask import Flask, request
app = Flask(__name__)
command = ""

@app.route("/get")
def get_cmd():
    return command

@app.route("/set", methods=["POST"])
def set_cmd():
    global command
    command = request.form.get("cmd")
    return "Command updated"

if __name__ == "__main__":
    app.run(port=5000)
