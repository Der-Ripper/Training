import socket

HOST = "challenge01.root-me.org"
PORT = 	52021
BUFSIZE = 1024

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
rot13 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(BUFSIZE)
string = str(data)[str(data).index("'") + 1:str(data).rindex("'")]
result = ''
for symbol in string:
    if symbol in alphabet:
        result += rot13[alphabet.index(symbol)]
    else:
        result += symbol
s.send(bytes(result + "\n", "utf-8"))
data = s.recv(BUFSIZE)
print(data.decode("utf-8"))
s.close()
