from banco import Banco

b = Banco()
print("Olá! Você é:")
print("1) Cliente")
print("2) Funcionário")
opc = int(input("Opção: "))
while (opc<1 or opc>2):
    opc = input("Opção inválida, tente outra: ")
if opc == 1:
    b.atendimentoCliente()
elif opc == 2:
    b.atendimentoFuncionario()