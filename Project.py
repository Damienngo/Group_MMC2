import socket;
s = socket.socket();
print("Socket Created");

#Connect to port number
port = 4567;

#Bind to port
s.bind(('',port));
print("Socket bind to %s" %(port));

#Listen to port
s.listen(5);
print("Socket is listening..");

#Forever loop to listen
while True:
    c, addr = s.accept();
    print("Connection from",addr);
