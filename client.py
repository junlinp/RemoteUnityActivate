import encode_decode
import socket
import sys

if __name__ == "__main__":
    
    if len(sys.argv) < 4:
        print("Usage: {} remote_host port /path/to/file".format(sys.argv[0]))
        exit(0)

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clientSocket.connect( (sys.argv[1], int(sys.argv[2])))

    with open(sys.argv[3], 'rb') as f:
        data = f.read()

        encode_decode.FileEncode(clientSocket, data)

        recv_data = encode_decode.FileDecode(clientSocket)

        print(data == recv_data)

        with open("test.txt", "wb") as f_:
            f_.write(recv_data)

    


    
