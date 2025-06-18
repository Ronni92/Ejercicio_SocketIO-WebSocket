from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(msg):
    print(f"Mensaje recibido: {msg}")
    send(f"Hola desde el servidor: {msg}")

if __name__ == '__main__':
    socketio.run(app, port=5000)
