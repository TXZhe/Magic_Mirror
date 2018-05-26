import socket, time
import os
import struct
import sys

#filepath = "/home/capstone/magic_mirror/client/"

class COMM_C:
    def __init__(self):
        print 'Prepare for connecting...'

    def sent_photo_get_reco(self, num):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #s.connect(('192.168.43.58', 6666))
            s.connect(('35.192.231.239', 6666))
        except socket.error as msg:
            print msg
            sys.exit(1)
        print s.recv(1024)

        filepath = "/home/capstone/magic_mirror/client/" + str(num) + ".jpg"
        #filepath = "/home/pi/Magic_mirror/" + str(num) + ".jpg"

        if os.path.isfile(filepath):
            fileinfo_size = struct.calcsize('128sq')
            fhead = struct.pack('128sq', os.path.basename(filepath),os.stat(filepath).st_size)
            s.send(fhead)
            print 'client filepath: {0}'.format(filepath)

            fp = open(filepath, 'rb')
            while True:
                data = fp.read(1024)
                if not data:
                    print '{0} file send over...'.format(filepath)
                    break
                s.send(data)

        recommand = "-1"
        buy = 0
        while True:
            receivedData = s.recv(1024)
            if(receivedData.startswith('rec')):
                recommand = receivedData.split(':')[-2]
                buy = receivedData.split(':')[-1]
                s.close()
                break
        return recommand,buy

if __name__ == '__main__':
    test = COMM_C()
    tmp,buy = test.sent_photo_get_reco(1)
    print tmp
    print buy
