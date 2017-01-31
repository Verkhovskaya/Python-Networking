from A_networking import *
import time


def server_response(connection):
    get_input = connection.a_read()
    if get_input == "5":
        print("Immediate!")
    else:
        time.sleep(10)
        print("Delayed")


server = AServer("###", 3219, server_response)
time.sleep(5)
server.a_close()