import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Conectado al servidor")
    sio.send("Hola servidor")

@sio.on('message')
def on_message(data):
    print("Servidor respondió:", data)

sio.connect('http://localhost:5000')
sio.wait()
