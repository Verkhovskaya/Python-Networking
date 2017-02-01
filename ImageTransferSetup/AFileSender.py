from A_networking import *
server_ip = "172.26.147.125"
server_port = 3012
file_id = 8

"""
ASocket use case:
socket = ASocketTo(server_ip, server_port)
socket.write("HAKUNNAH MATATTA")
response = socket.read()
print(response)
"""

send_file = open("testFile.txt", "r")
socket = ASocketTo(server_ip, server_port)
socket.write("sender")
socket.read()
socket.write(str(file_id))
socket.read()
while 1:
    message = send_file.read(1000)
    socket.write(message)
    if message == "":
        break
socket.close()
