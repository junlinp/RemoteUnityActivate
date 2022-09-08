import encode_decode
import sys
import socket

if __name__ == "__main__":

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serverSocket.bind(("0.0.0.0", 9090))

    serverSocket.listen()

    while True:
        (clientConnected, clientAddress) = serverSocket.accept()
        print("Accepted a connection request from {}".format(clientAddress))

        recv_data = encode_decode.FileDecode(clientConnected)

        encode_decode.FileEncode(clientConnected, recv_data)


