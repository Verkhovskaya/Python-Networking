from A_networking import *
server_ip = "172.26.147.125"
server_port = 3012


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
    file_id = conn.read()

    if other_side == "sender":
        temp_file = open(file_id + ".txt", "w")
        conn.write("ack")

        while 1:
            message = conn.read()
            temp_file.write(message)
            print(message)
            if message == "":
                break

        global files
        files[file_id] = temp_file
        print(files)
        temp_file.close()
        conn.close()

    if other_side == "receiver":
        try:
            temp_file = open(file_id + ".txt")
            conn.write("exists")
            conn.read()
            while 1:
                message = temp_file.read(1000)
                conn.write(message)
                if message == "":
                    break
            temp_file.close()
            conn.close()
        except IOError:
            conn.write("no file")

server = AServer(server_ip, server_port, server_response)
