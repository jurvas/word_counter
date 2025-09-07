import socket
import sys

def run_server(port:int, filepath:str):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    print("Listening on port " + str(port))
    server.listen(5)

    while True:
        client, addr = server.accept()
        print("Got connection from " + str(addr))
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                client.send(line.encode("utf-8"))
        client.close()
        print("Connection closed")

def main():
    if len(sys.argv) != 3:
        print("Usage: python server.py <port> <filepath>")
        sys.exit(1)
    port = int(sys.argv[1])
    filepath = sys.argv[2]
    run_server(port, filepath)

if __name__ == '__main__':
    main()