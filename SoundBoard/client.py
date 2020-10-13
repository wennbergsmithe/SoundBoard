import socket
from playsound import playsound
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('',6666))

try:
    while True:
        data, add = server_socket.recvfrom(256)
        if str(data) == "b'1'":
            playsound('1.wav')
        if str(data) == "b'2'":
            playsound('2.wav')
        if str(data) == "b'3'":
            playsound('3.wav')
        if str(data) == "b'4'":
            playsound('4.wav')
except:
    print("audio file not found")
finally:
    server_socket.close()
