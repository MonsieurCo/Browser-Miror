import socket
'''
To run this code I put a proxy on my computer at 127.0.0.1:2003 

'''


def server():
    HOST = '127.0.0.1'
    PORT = 2003  # random port above 1024
    MAXBYTES = 4096
    print(HOST, PORT)
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        data = conn.recv(MAXBYTES).decode("utf8")
        if not data:
            break
        print("ECHO RESQUEST: \n",data,sep="")
    conn.close()  # close the connection

if __name__ == '__main__':
    server()
