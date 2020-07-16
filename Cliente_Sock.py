import socket
import Prog_Chave_AES

def cliente_arquivo(host, porta):
    
    servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    servidor.connect((host, porta))
    
    Prog_Chave_AES.criptografar(Prog_Chave_AES.solicitar_chave("12345600"), "cliente.txt")
    
    arqv = open('_crip_cliente.txt', 'rb')

    for i in arqv.readlines():
        servidor.send(i)
        
    arqv.close()
    servidor.close()

cliente_arquivo("127.0.0.1", 5150)