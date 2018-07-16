from asyncore import dispatcher
import asyncore, socket

HOST = ''
PORT = 5005
LISTENNUM = 5

class ChatServer(dispatcher):
    def __init__(self, port = PORT, host = HOST, listen = LISTENNUM):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(listen)


    def handle_accept(self):
        conn, addr = self.accept()
        print "Connection attempt from", addr[0]

if __name__ == '__main__':
    s = ChatServer()
    try: asyncore.loop()
    except KeyboardInterrupt: pass
