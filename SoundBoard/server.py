import socket
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#IP = "192.168.114.153"
#IP = "192.168.114.148"
IP = "192.168.114.148"
try:
    while True:
        if GPIO.input(11) == GPIO.HIGH:
            client_socket.sendto("1",(IP,6666))
            print("B1")
            time.sleep(1)
        if GPIO.input(13) == GPIO.HIGH:
            client_socket.sendto("2",(IP,6666))
            print("B2")
            time.sleep(1)
        if GPIO.input(15) == GPIO.HIGH:
            client_socket.sendto("3",(IP,6666))
            print("B3")
            time.sleep(1)
        if GPIO.input(19) == GPIO.HIGH:
            client_socket.sendto("4",(IP,6666))
            print("B4")
            time.sleep(1)
finally:
    GPIO.cleanup()
    client_socket.close()
