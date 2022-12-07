import socket
import threading
import rsa          # External library for the encryption.
public_key, private_key = rsa.newkeys(1024)
public_sender = None


#This chat system utilizes a centralized script communication: Host/Receive Optons
choice = input("Do you prefer to HOST(1) or to CONNECT(2):")

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.2.66", 9999)) #user local ip address since chat is done on one maching.
    server.listen()
    client,_ = server.accept()
    client.send(public_key.save_pkcs1("PEM"))
    public_sender = rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.2.66", 9999)) #user local ip address since chat is done on one maching.
    public_sender = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))

else:
    exit()
    
#Sender Messaging
def sending_messages(e):
    while True:
        message = input("")
        e.send(rsa.encrypt(message.encode(), public_sender))
        print("You:" + message)

#Receiver Messaging
def receiving_messages(e):
    while True:
        print("Sender:" + rsa.decrypt(e.recv(1024), private_key).decode())
        
        
threading.Thread(target = sending_messages, args = (client,)).start()
threading.Thread(target = receiving_messages, args = (client,)).start()
        

    

