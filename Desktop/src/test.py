# import socket
# import time
# Create a TCP / IP socket
# i = 0 # loop counter
# j = 45.395 # data to be sent to MATLAB
# while 1:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         s.bind(('localhost', 51001))
#         s.listen(1)
#         conn, addr = s.accept()
#         print(f"Connected: {conn, addr}")
    
#         t = conn.sendall(f"{j}".encode())
#         i += 1
#         j += 0.6
#         time.sleep(5)
#         conn.close()
#     except Exception as e:
#         print(e)

import socket
from ObjectDetector import ObjectRecognition

vision = ObjectRecognition("Robotics vision")
vision.initCamera()

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)
while 1:
    data = vision.state()
    if not data: break
    conn.sendall(data)
conn.close()