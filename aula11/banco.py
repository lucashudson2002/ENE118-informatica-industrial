from contas import Conta

class Banco:
    def __init__(self):
        self.__senhaFunc = 123456
        self.__contas = []
        self.__contas.append(Conta(1, "Joao", 1234, 300))
        self.__contas.append(Conta(2, "Jose", 4567, 800))
        self.__contas.append(Conta(3, "Maria", 7890, 1000))
        self.__contas.append(Conta(4, "Madalena", 8956, 2000))
    
    def buscaConta(self, numero):
        for conta in  self.__contas:
            if numero == conta.numero:
                return conta
        return -1
    
    def atendimentoCliente(self):
        print("Bem vindo ao sistema de atendimento do banco ao cliente")
        numC = int(input("Digite o numero da sua conta: "))
        conta = self.buscaConta(numC)
        if conta == -1:
            print("Conta inválida")
        else:
            print(f"Olá {conta.titular}")
            senha = int(input("Digite a senha: "))
            atendimento = True
            while (atendimento):
                op = int(input("Qual operação deseja fazer? (1 - Ver Saldo, 2 - Saque, 3 - Deposito, 4 - Sair): "))
                if op == 1:
                    print(f"Saldo: R$ {conta.getSaldo(senha)}")
                elif op == 2:
                    valor = float(input("Digite o valor: "))
                    conta.saque(senha, valor)
                elif op == 3:
                    valor = float(input("Digite o valor: "))
                    conta.deposito(valor)
                elif op == 4:
                    atendimento = False

    def atendimentoFuncionario(self):
        print("Bem vindo ao sistema de atendimento do banco ao funcionário")
        senha = int(input("Digite a senha de funcionário: "))
        if senha == self.__senhaFunc:
            print("Ola funcionário!")
            atendimento = True
            while (atendimento):
                op = int(input("Qual operação deseja fazer? (1 - Mudar senha, 2 - Cadastrar cliente, 3 - Sair): "))
                if op == 1:
                    self.__senha = int(input("Digite a nova senha: "))
                elif op == 2:
                    numero = int(input("Digite o número da conta: "))
                    conta = self.buscaConta(numero)
                    if conta!=-1:
                        print("Já existe conta com esse número")
                        return
                    titular = input("Digite o nome do titular: ")
                    senha = int(input("Digite a senha da conta: "))
                    saldo = int(input("Digite a quantidade de dinheiro a ser depositada inicialmente na conta: "))
                    self.__contas.append((numero, titular, senha, saldo))
                    print("Conta adicionada com sucesso!")
                elif op == 3:
                    atendimento = False
        else:
            print("Senha inválida")