#A little experiment to extract webpages
import socket

url = 'http://data.pr4e.org/intro-short.txt'
command = 'GET ' + url + '  HTTP/1.0\r\n\r\n'
print(command) 
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
command = command.encode()
mysocket.send(command)

while True :
    data = mysocket.recv(512)
    if (len(data) < 1) :
        break
    print(data.decode())
mysocket.close()