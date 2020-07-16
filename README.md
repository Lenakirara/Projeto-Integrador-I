# Projeto Integrador I - CRIPTOGRAFIA DE CHAVE SIMÉTRICA – AES

### ATIVIDADES DO PROJETO INTEGRADOR – CURSO DE TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - 2º semestre de 2018 - Faculdade Senac-GO

- Desenvolver, em Python, um programa para criptografar arquivos, usando o algoritmo de criptografia de chaves simétricas AES (Advanced Encryption Standard).

### Funcionalidade:

- Criptografar um arquivo e transmiti-lo para um outro computador.
- Receber um arquivo criptografado e decriptografa-lo
- Gerenciar lista de arquivos transmitidos e recebidos.
- Transmissão (cliente) e recepção (servidor) do arquivo: deverá ser usado a biblioteca Socket, onde o receptor estará escutando uma porta pré-determinada (número da porta à escolha do grupo) para uma conexão TCP.
- Os arquivos transmitidos e recebidos poderão ser criptografados usando sempre a mesma chave e vetor de inicialização, ou então mudar esses valores a cada arquivo.
