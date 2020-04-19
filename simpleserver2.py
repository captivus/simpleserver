# simple program to create an echo server
import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind(('', 50000))
s.listen(1)

conn, addr = s.accept()

print('Connected to:', addr)

data = conn.recv(1024)
if not data:
    print('There was no data!  Closing the connection!')

conn.send(data)
print(data)

conn.close()