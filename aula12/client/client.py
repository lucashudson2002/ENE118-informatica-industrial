import socket
import cv2
import numpy as np

class Cliente():
    """
    Classe Cliente - API Socket
    """
    def __init__(self, server_ip, port):
        """
        Construtor da classe Cliente
        """
        self.__server_ip = server_ip
        self.__port = port
    
    def start(self):
        """
        Método que inicializa a execução do Cliente
        """
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        endpoint = (self.__server_ip,self.__port)
        try:
            self.__tcp.connect(endpoint)
            print("Conexão realizada com sucesso!")
            self.__method()
        except:
            print("Servidor não disponível")

    
    def __method(self):
        """
        Método que implementa as requisições do cliente
        """
        try:
            msg = ''
            while msg != '\x18':
                msg = input("Digite um  número de 1 a 4 para ser a face escolhida para detecção (x para sair): ")
                if msg == 'x':
                    break
                elif msg == '' or int(msg)<0 or int(msg)>4:
                    continue
                img = cv2.imread(f'../faces/image_{int(msg):04}.jpg')
                _, img_bytes = cv2.imencode('.jpg', img)
                img_bytes = bytes(img_bytes)
                tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')
                self.__tcp.send(tamanho_da_imagem_codificado)
                self.__tcp.send(img_bytes)
                
                tamanho_da_imagem_codificado = self.__tcp.recv(1024)
                tamanho_da_imagem_codificado = int.from_bytes(tamanho_da_imagem_codificado, 'big')
                img_bytes = self.__tcp.recv(1024)
                while(len(img_bytes)<tamanho_da_imagem_codificado):
                    img_bytes += self.__tcp.recv(1024)
                img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)
                cv2.imshow('Imagem Processada', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            self.__tcp.close()
        except Exception as e:
            print("Erro ao realizar comunicação com o servidor", e.args)