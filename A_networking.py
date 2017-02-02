import socket
import threading


"""
A_server
Use case:
def server_response(self):
    input = self.read()
    input += "A"
    self.write(input)
server = AServer(server_ip, server_port, server_response)
"""

"""
ASocket use case:
socket = ASocketTo(server_ip, server_port)
socket.write("HAKUNNAH MATATTA")
response = socket.read()
print(response)
socket.close()
"""


class AConnection:
    use_case = "Options:\nA_socket_to\nA_server"

    def __init__(self, connection):
        self.partner = connection

    def write(self, message):
        self.partner.sendall(str(len(message)))
        self.partner.sendall("#")
        self.partner.sendall(message)

    def read(self):
        message_length = ""
        while 1:
            get_input = self.partner.recv(1)
            if get_input == "#":
                break
            else:
                message_length += get_input

        message_length = int(message_length)
        chunks = []
        bytes_recd = 0
        while bytes_recd < message_length:
            chunk = self.partner.recv(min(message_length - bytes_recd, 2048))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd += len(chunk)

        return ''.join(chunks)

    def close(self):
        self.partner.close()

    def send_file(conn, file_name):
        try:
            temp_file = open(file_name, "r")
            while 1:
                message = temp_file.read(1000)
                conn.write(message)
                if message == "":
                    break
            temp_file.close()
        except IOError:
            conn.write("")

    def receive_file(conn, new_name):
        temp_file = open(new_name, "w")
        while 1:
            message = conn.read()
            temp_file.write(message)
            print(message)
            if message == "":
                break
        temp_file.close()


class ASocketTo(AConnection):
    use_case = "socket = A_socket_to(server_ip, server_port)\nsocket.write(\"HAKUNNAH MATATTA\")"
    use_case += "\nresponse = socket.read()\nprint(response)\nsocket.close()"

    def __init__(self, server_ip, server_port):
        self.partner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.partner.connect((server_ip, server_port))


class AServer(AConnection):
    use_case = "def server_response(self):\n    input = self.read()"
    use_case += "\n    input += \"A\"\n    self.write(input)"
    use_case += "\nserver = A_server(server_ip, server_port, server_response)"
    use_case += "\nA_wait(10)\nserver.close()"

    def __init__(self, ip, port, response):
        self.partner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.partner.bind((ip, port))
        self.partner.listen(5)

        def run(the_server, response):
            while 1:
                connection, addr = the_server.accept()
                print("Connection received!")
                temp = AConnection(connection)
                threading.Thread(target=response, args=(temp,)).start()

        threading.Thread(target=run, args=(self.partner, response)).start()
