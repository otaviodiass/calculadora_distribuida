import socket
from random import randint


def terminal():
    while True:
        try:
            entrada = input('Informe qual operação e os valores:\n')
            client.send(entrada.encode())

            print(client.recv(2048).decode())
        except:
            print('Erro ao publicar mensagem.')


if __name__ == '__main__': 
    HOST = 'localhost'
    PORTA = 50000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORTA))
    terminal()
