import zmq
  
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print("waiting for connecting")
while True:
    message = socket.recv()
    message=str(message,encoding="utf-8")
    print ("message from client:", message)
     
    #  Send reply back to client
    socket.send(b"successed")

