import socket
from urllib.parse import urlparse
'''
To run this code I put a proxy on my computer at 127.0.0.1:2003 

'''


#just send back to the browser what he gaves you



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
        rawdata = conn.recv(MAXBYTES)
        data = rawdata.decode("utf8")
        if not data:
            break
        print("ECHO RESQUEST: \n",(rawdata+b"\r\n\r\n").decode("utf8"),sep="")
        parsed = data.split(" ")
        method = parsed[0]
        h = parsed[2]
        URL = parsed[1]
        u = urlparse(URL)
        print(URL)
        if u.scheme == '':
            addressTO = (u.geturl().split(":")[0], int(u.geturl().split(":")[1]))
        else:
            addressTO = (u.geturl(),8080)
        print(addressTO)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addressTO)
        #res = [method,h].append(data[2:])
        #datas = " ".join(parsed[2:])
        #print(datas)
        s.sendall(rawdata+b"\r\n\r\n")
        new_data = s.recv(4096)
        while(len(new_data)< 1):
            new_data = s.recv(4096)
        s.close()
        print("RECIEVED : ")
        print(new_data.decode("utf8"))
        conn.send(new_data)

    conn.close()  # close the connection

if __name__ == '__main__':
    server()
