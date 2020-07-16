import os
import platform
import psutil
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def info_sistema():
    so = platform.system()
    cpu = psutil.cpu_percent(interval = 1)
    mem = psutil.swap_memory()
    process = psutil.Process(os.getpid())

def criptografar(chave, arquivo):
    bloco = 2048
    arq_saida = '_crip_' + arquivo
    comp_arq = str(os.path.getsize(arquivo)).zfill(16)
    IV = Random.new().read(AES.block_size)
   
    cifrar = AES.new(chave, AES.MODE_CBC, IV)
   
    with open(arquivo, 'rb') as arq_cifrado:
        with open(arq_saida, 'wb') as arq_fo:
            arq_fo.write(comp_arq.encode('utf-8'))
            arq_fo.write(IV)
           
            while True:
                partes = arq_cifrado.read(bloco)
                n = len(partes)
                if n == 0:
                    break
                elif n % 16 != 0:
                    partes += b' ' *(16 - n % 16)
                   
                arq_fo.write(cifrar.encrypt(partes))
           
def descriptografar(chave, arquivo):
    bloco = 2048
    arq_saida = arquivo[6:]
   
    with open(arquivo, 'rb') as arq_decifrado:
        comp_arq = int(arq_decifrado.read(AES.block_size))
        IV = arq_decifrado.read(AES.block_size)
           
        decifrar = AES.new(chave, AES.MODE_CBC, IV)
               
        with open(arq_saida, 'wb') as arq_fo:
            while True:
                partes = arq_decifrado.read(bloco)
                n = len(partes)
                if n == 0:
                    break
                decifrar = decifrar.decrypt(partes)
                n = len(decifrar)
                if comp_arq > n:
                    arq_fo.write(decifrar)
                else:
                    arq_fo.write(decifrar[:comp_arq])
                comp_arq +=n
                           
            arq_fo.truncate(comp_arq)
                       
def solicitar_chave(senha):
    h = SHA256.new(senha.encode('utf-8'))
    return h.digest()
   
def Main ():
    info_sistema()
    print('\n\nSistema Operacional:\t'+platform.system()+platform.release())
    print('\nMaquina:\t'+platform.machine())
    print('\nRede:\t\t'+platform.node())
    print('\nPlataforma:\t'+platform.platform())
    print('\nCPU:\t%.2f'%psutil.cpu_percent(interval = 1))
    print('\nMemória:\t',psutil.swap_memory())
    print('\nProcesso(PID):\t',psutil.Process())
            
    print('')
    
    opçao = input('Digite (C) para criptografar ou digite (D) para descriptografar: ').upper()
    if opçao == 'C':
        arquivo = input('Digite o arquivo que deseja criptografar: ')
        senha = input('Digite a senha: ')
        criptografar(solicitar_chave(senha), arquivo)
        print('FIM!')
    elif opçao == 'D':
        arquivo = input('Digite o arquivo que deseja descriptografar: ')
        senha = input('Digite a senha: ')
        descriptografar(solicitar_chave(senha), arquivo)
        print('FIM!')
    else:
        print('Comando não digitado corretamente. Programa será encerrado.') 
 
if __name__ == '__main__':
    Main()
