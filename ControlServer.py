#! /usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import thread
import Queue


def handler(clientsocket, clientaddr):
    id = threading.current_thread().ident
    print "Nuevo hilo con id:", id, " e IP:", clientaddr[0]
    print "Conexiones actuales: ", threading.active_count() - 1
    while True:
        data = clientsocket.recv(1024)
        if data == '':
            print "Cerrando el hilo con id ", id, "..."
            clientsocket.close()
            thread.exit()
        elif data == 'w8sig':
            clientsocket.send("comando")
        elif data == 'w8cmd':
            comando = Qcomando.get()
            clientsocket.send(comando)
        elif data == 'admin':
            clientsocket.send('incmd')
            while data != '':
                comando = clientsocket.recv(1024)
                for i in range(threading.active_count() - 1):
                    Qcomando.put(comando)
                msg = 'Comando enviado al: %s' % comando
                clientsocket.send(msg)


if __name__ == "__main__":
    Qcomando = Queue.Queue()
    host = '0.0.0.0'
    port = 55567
    buf = 1024
    addr = (host, port)
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(addr)
    serversocket.listen(1)
    while True:
        clientsocket, clientaddr = serversocket.accept()
        hilo = threading.Thread(target=handler, args=(clientsocket, clientaddr))
        hilo.start()
    serversocket.close()
