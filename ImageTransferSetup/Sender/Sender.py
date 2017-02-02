from A_networking import *
server_ip = "172.26.147.125"
server_port = 3032
file_name = "testFile.txt"

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
socket.write(file_name)
socket.read()
socket.send_file(file_name)
socket.close()