## Server

Uses socket to share a single txt file. After the file is read by client, keeps waiting for another client.

Usage: python server.py \<port\> \<filepath\>

## Client

Reads files from multiple ports, counts the number of words and outputs 5 most used words.

Usage: python client.py \<host\> \<ports\>
