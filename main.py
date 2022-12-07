import socket
import threading
import rsa          # External library for the encryption.


#This chat system utilizes a centralized script communication: Host/Receive Optons
choice = input("Do you prefer to HOST(1) or to CONNECT(2):")

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.2.66", 9999)) #user local ip address since chat is done on one maching.
    server.listen()
    client,_ = server.accept()

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.2.66", 9999)) #user local ip address since chat is done on one maching.

else:
    exit()
    
#Sender Messaging
def sending_messages(e):
    while True:
        message = input("")
        e.send(message.encode())
        print("You:" + message)

#Receiver Messaging
def receiving_messages(e):
    while True:
        print("Sender:" + e.recv(1024).decode())
        
        
threading.thread(target = sending_messages, args = (clientt,)).start()
threading.thread(target = receiving_messages, args = (clientt,)).start()
        

    

