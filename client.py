
import socket
import PIL 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 2000                                  # Choose the port number your server is bound to
sock.connect(('localhost', port))           # Connects to given port number on the local machine
print("connected to server")
while True:
    cmd = input("")                         # Get command line input to send to server
    split = cmd.split(' ')                  # Split the command by the space characters
    if split[0].lower() != "quit":
        print("sending command")
        sock.send(cmd.encode("utf-8"))      # Send the command line to server
        img = sock.recv(600000)
        print("received image")
        print(img)
        with open(f"img_client/image133535.jpg", 'wb') as f:
            f.write(img)
    else:
        sock.send(cmd.encode("utf-8"))      # Send the quit message to server
        sock.close()                        # Close the program
        print('Connection Closed')
        break                               # Terminate the client program