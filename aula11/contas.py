class Conta():
    """
    Classe Conta
    """
    _saldo = 0.0
    def __init__(self, numero, titular, senha, saldoi=0.0):
        """
        Construtor da classe Conta
        :param numero: número da conta
        :param titular: nome o titular da conta
        :param senha: senha da conta
        :param saldoi: saldo inicial da conta (padrão = 0.0)
        """
        self.numero = numero
        self.titular = titular
        self.__senha = senha
        self._saldo = saldoi
    
    def getSaldo(self, senha):
        """
        Método para obtenção do saldo mediante validação da senha passada como argumento
        :param senha: senha da conta
        :return: saldo da conta
        """
        if self.__senha == senha:
            return self._saldo

    def setSaldo(self, valor):
        """
        Método para configuração do saldo
        :param valor: valor desejado para o saldo
        """
        self._saldo = valor

    def setSenha(self, novaSenha):
        """
        Método para configuração de uma nova senha na conta
        :param novaSenha: nova senha desejada
        """
        self.__senha = novaSenha

    def saque(self, senha,valor):
        """
        Método para realização de uma saque
        :param senha: senha da conta
        :param valor: valor do saque
        """
        if senha == self.__senha:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f"Saque no valor de R$ {valor} realizado com sucesso")
            else:
                print("Saldo insuficiente")
        else:
            print("Senha inválida")
    
    def deposito(self, valor):
        """
        Método para realização de um depósito
        :param valor: valor do deposito desejado
        """
        if valor > 0:
            self._saldo += valor
        else:
            print("Valor inválido")

    def exibeDados(self, senha):
        """
        Método para exibição das informações da conta
        :param senha: senha da conta
        """
        if self.__senha == senha:
            print("Número: ", self.numero)
            print("Titular: ", self.titular)
            print("Saldo: R$ ", self._saldo)
        else:
            print("Senha inválida")