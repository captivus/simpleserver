# simple program to create an echo server
import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.bind(('', 50000))
s.listen(1)

conn, addr = s.accept()
print('Connected to:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        print('There was no data!  Closing the connection!')
        break
    if data.decode('utf-8') == 'MonkDawg\n':
        print('MonkDawg detected!!')
        conn.send(b'Smelly mufq!\n')
    else: conn.send(data)

conn.close()