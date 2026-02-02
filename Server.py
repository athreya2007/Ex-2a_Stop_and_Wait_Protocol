import socket             
s = socket.socket()         
print ("Socket successfully created")
port = 12345                
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
s.listen(5)     
print ("socket is listening")    
c, addr = s.accept() 
frame=int(input("Enter frame size:")) 
for i in range(1,frame+1):
    send=f"Frame{i} sent"
    c.send(send.encode())
    msg = c.recv(1024).decode()
    print(msg)
send="Exit"
c.send(send.encode())
c.close()
