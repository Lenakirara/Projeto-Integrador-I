import socket
import Prog_Chave_AES

def servidor_arquivo(host, porta):
    
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(1)

    conexão, endereço = servidor.accept()

    arqv = open('_crip_servidor.txt', 'wb')

    while 1:
        dados = conexão.recv(1024)
        if not dados:
            break
        arqv.write(dados)
        
    arqv.close()
    conexão.close()
    Prog_Chave_AES.descriptografar(Prog_Chave_AES.solicitar_chave("12345600"), "_crip_servidor.txt")

servidor_arquivo("127.0.0.1", 5150)
    
