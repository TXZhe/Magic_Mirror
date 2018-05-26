import socket
import threading
import time
import sys
import os
import struct
import requests
import json
import face_plus

'''
Set up server
'''
def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #s.bind(('192.168.43.58', 6666))
        s.bind(('10.128.0.2', 6666))
        s.listen(10)
    except socket.error as msg:
        print (msg)
        sys.exit(1)
    print ('Waiting connection...')

    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()

'''
Deal with recevied files
'''
def deal_data(conn, addr):
    print ('Accept new connection from {0}'.format(addr))
    #conn.settimeout(500)
    conn.send("Hi, Welcome to the server!".encode())

    while 1:
        fileinfo_size = struct.calcsize('128sq')
        buf = conn.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128sq', buf)
            fn = filename.strip("\00".encode())
            new_filename = os.path.join("./".encode(), fn)
            print ('file new name is {0}, filesize if {1}'.format(new_filename, filesize))

            recvd_size = 0
            fp = open(new_filename, 'wb')
            print ('start receiving...')

            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = conn.recv(1024)
                    recvd_size += len(data)
                else:
                    data = conn.recv(filesize - recvd_size)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
            print ('end receive...')
            reco = face_plus.sent_to_face(fn.decode('utf-8'))
            print(reco)
            conn.send(reco.encode())
        conn.close()
        break

if __name__ == '__main__':
    socket_service()
