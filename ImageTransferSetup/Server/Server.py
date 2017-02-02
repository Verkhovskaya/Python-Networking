from A_networking import *
server_ip = "172.26.147.125"
server_port = 3032


"""
A_server
Use case:
def server_response(self):
    input = self.a_read()
    input += "A"
    self.a_write(input)
server = AServer(server_ip, server_port, server_response)
"""


def server_response(conn):
    other_side = conn.read()
    conn.write("ack")
    file_name = conn.read()

    if other_side == "sender":
        conn.write("ack")
        conn.receive_file(file_name)

    if other_side == "receiver":
        conn.send_file(file_name)

    conn.close()

server = AServer(server_ip, server_port, server_response)
