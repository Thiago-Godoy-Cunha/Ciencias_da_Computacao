import socket  # Lib sockets
import os # Lib arquivos

client_controle = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria socket exemplo aula
client_controle.connect(('localhost', 21)) # Conecta ao servidor na porta 21

# mensagem = 'Me dá os arquivoooooos'
# client_controle.sendall(mensagem.encode('utf-8'))

# Recebe resposta
data = client_controle.recv(1024)
for i, arquivo in enumerate(eval(data.decode('utf-8'))):
    print(f'{i+1} - {arquivo}')
escolha = ''
while escolha != 'exit':
    escolha = input("Digite o número conforme o arquivo que deseja receber: (exit para sair) ")
    client_controle.sendall(escolha.encode('utf-8'))

    if escolha == 'exit':
        break

    client_dados = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria socket exemplo aula
    client_dados.connect(('localhost', 20)) # Conecta ao servidor na porta 2

    # Grava arquivoi
    file = open(f'./arquivos_recebidos/{eval(data.decode("utf-8"))[int(escolha) - 1]}', 'wb') # abre o arquivo para escrita com o nome do arquivo escolhido
    file.write(client_dados.recv(1024)) # Eescreve o conteúdo recebido no arquivo
    file.close()  # Fecha o arquivo
    client_dados.close()  # Fecha o socket de dados

    for i, arquivo in enumerate(eval(data.decode('utf-8'))):
        print(f'{i+1} - {arquivo}')

client_controle.close()  # Fecha o socket