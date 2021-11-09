import socket
from urllib.parse import urlparse
'''
To run this code I put a proxy on my computer at 127.0.0.1:2003 

'''


#just send back to the browser what he gaves you

def server():
    HOST = '127.0.0.1'
    PORT = 8080  # random port above 1024
    MAXBYTES = 4096
    print(HOST, PORT)
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        rawdata = conn.recv(MAXBYTES)
        data = rawdata.decode("utf8")
        if not data:
            break
        print("ECHO RESQUEST: \n",(rawdata+b"\r\n\r\n").decode("utf8"),sep="")
        conn.send(rawdata)

    conn.close()  # close the connection

if __name__ == '__main__':
    server()
