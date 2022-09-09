import encode_decode
import sys
import socket
import os

def Activate(data, USER_NAME, USER_PASSWORD):
    save_file = "Unity_v2021.3.0f1.alf"
    with open(save_file, "wb") as f:
        f.write(data)
        for i in range(3):
            if os.path.exists("error.html"):
                os.remove("error.html")

            os.system(f"unity-activate -u {USER_NAME} -p {USER_PASSWORD} --debug {save_file}")
            if os.path.exists("*.ulf"):
                return True
            
        if os.path.exists("error.html"):
            return False

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} UNITY_USERNAME UNITY_PASSWORD")
        exit(0)

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    Port = 12345

    print(f"Start Server On {Port}")
    serverSocket.bind(("0.0.0.0", Port))

    serverSocket.listen()

    while True:
        (clientConnected, clientAddress) = serverSocket.accept()
        print("Accepted a connection request from {}".format(clientAddress))

        recv_data = encode_decode.FileDecode(clientConnected)
        
        if  Activate(recv_data, sys.argv[1], sys.argv[2]):
            with open("*.ulf", "rb") as f:
                clientConnected.send(f.read())
        else:
            encode_decode.FileEncode(clientConnected, recv_data)

