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
socket.close()
"""

image = open("ReceivedABFile"+str(file_id) + ".txt", "w")
socket = ASocketTo(server_ip, server_port)
socket.write("receiver")
socket.read()
socket.write(str(file_id))
response = socket.read()

if response == "exists":
    socket.write("ack")
    while 1:
        message = socket.read()
        image.write(message)
        if message == "":
            break

else:
    print(response)

socket.close()
