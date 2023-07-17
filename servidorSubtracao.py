import socket

HOST = 'localhost'
PORTA = 60001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORTA))
s.listen(5)

print("Aguardando conexão de um cliente")

while True:
    conn, end = s.accept()
    print("Conectado em :", end)

    while True:
        mensagem = conn.recv(2048).decode()

        subtracao = int(mensagem.split(',')[1]) - int(mensagem.split(',')[2])

        conn.send(str(subtracao).encode())
        break

    conn.close()
