import socket

class Server(object):
    def __init__(self, server, host):
        self.server = server
        self.host = host

    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.bind(('127.0.0.1', 50001))

    print('Давай общаться! ')
    while True:
        data, addr = socket.recvfrom(1024)
        recvmsg = data.decode('utf-8')
        if recvmsg == 'q':
            print("Другой участник добровольно закончил чат с тобой, пока!")
            break

        f = open("REC.txt", "w")
        str = []

        REC_text = 'sever', 'client'
        f.write("server:"+recvmsg+"\n")
        f.write("client:"+recvmsg+"\n")

        f.close()

        try:
            for line in f:
                str.append(line)

        except Exception:
            pass

        finally:
            f.close()

        print('сообщение от участника: '+recvmsg)
        replymsg = input('Ответить: ')
        socket.sendto(replymsg.encode('utf-8'), addr)

    socket.close()