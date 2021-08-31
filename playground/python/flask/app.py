from flask_socketio import SocketIO

from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "hi"
socketio = SocketIO(app)


# @app.route("/")
# def sessions():
#     return "Hello World"


@socketio.on("message")
def handle_my_custom_event(mes):
    print("received my event: " + str(mes))
    socketio.emit("my response", mes)


if __name__ == "__main__":
    socketio.run(app, debug=True)
