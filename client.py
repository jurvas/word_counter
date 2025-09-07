import socket
import sys
import threading
from collections import Counter

def count_from_server(host, port, counter):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, int(port)))
        except:
            print("Connection failed on port " + str(port))
            return

        print("Connection established")
        while True:
            data = s.recv(1048576)
            if not data:
                break
            data = data.decode()
            words = data.lower().split()
            counter.update(words)


def main():
    host = sys.argv[1]
    ports = sys.argv[2:]
    counters = [Counter()] * len(ports)
    threads = []
    for i, port in enumerate(ports):
        t = threading.Thread(target=count_from_server, args=(host, port, counters[i]))
        print("Starting thread" + str(i) + " on port: " + str(port))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    total_counter = counters[0]
    for c in counters[1:]:
        total_counter += c

    for word, count in total_counter.most_common(5):
        print(word, count)

if __name__ == '__main__':
    main()