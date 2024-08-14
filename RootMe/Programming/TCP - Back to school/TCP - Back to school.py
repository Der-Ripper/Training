import socket

HOST = "challenge01.root-me.org"
PORT = 52002
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(BUFSIZE)
result = round(int(data[171:174]) ** 0.5 * int(data[191:195]), 2)
s.send(bytes(str(result) + "\n", "utf-8"))
data = s.recv(BUFSIZE)
print("\nFLAG :", str(data)[36:60])
s.close()
