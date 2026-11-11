import socket  # Lib sockets
import os # Lib arquivos

controle = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria socket exemplo aula
controle.bind(('localhost', 21)) # config IP, porta
controle.listen() # Escuta

conn, addr = controle.accept() # Aceite
print(f"Conectado por {addr}")

arq_list = os.listdir('./arquivos')
conn.sendall(str(arq_list).encode('utf-8'))  # Envia lista de arquivos

# Loop para receber mensagens
while True:
    data = conn.recv(1024)  # Lê até 1024 bytes
    if data.decode('utf-8') == 'exit':
        break  # Sai do loop se não houver dados
    while data.decode('utf-8') != 'exit':
        conn.sendall(f"Enviando arquivo {arq_list[int(data.decode('utf-8')) - 1]} pela porta 20".encode('utf-8'))  # Envia mensagem de confirmação
    
        # Cria socket pra envio de dados
        dados = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria socket exemplo aula
        dados.bind(('localhost', 20)) # config IP, porta
        dados.listen() # Escuta

        print("Aguardando resposta para envio do arquivo...")

        conn_dados, addr_dados = dados.accept() # Aceite modo passivo

        print(f"Conectado por {addr_dados}, enviando arquivo...")

        file = open(f'./arquivos/{arq_list[int(data.decode("utf-8")) - 1]}', 'rb')  # Abre arquivo de acordo com index recebido
        conn_dados.sendall(file.read())  # Envia o arquivo
        file.close()  # Fecha o arquivo

        conn_dados.close()  # Fecha a conexão de dados

conn.close()  # Fecha a conexão
print("Conexão encerrada.")
print()
