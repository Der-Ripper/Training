import socket
import base64

HOST = "challenge01.root-me.org"
PORT = 52023
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(BUFSIZE)
string = str(data)[str(data).index("'") + 1:str(data).rindex("'")]
s.send(bytes(base64.b64decode(string).decode("utf-8") + "\n", "utf-8"))
data = s.recv(BUFSIZE)
print(data.decode("utf-8"))
s.close()
