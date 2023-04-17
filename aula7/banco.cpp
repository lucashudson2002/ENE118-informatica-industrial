#include "banco.h"
#include <iostream>

using namespace std;

Banco::Banco() //O construtor criara 4 contas
{
    this->top = 3;
    this->contas = new Conta[top+1];
    this->senhaFuncionario = 246810;
    this->contas[0] = Conta(1234, 1, "Joao", "Corrente", 300);
    this->contas[1] = {4567, 2, "Jose", "Poupanca", 800};
    this->contas[2] = {7890, 3, "Maria", "Corrente", 1000};
    this->contas[3] = {8956, 4, "Madalena", "Poupanca", 2000};
}

Banco::~Banco()
{
    delete[] this->contas;
}

Conta *Banco::buscaConta(int numero)//Retorna o endereço da conta que possuir o mesmo numero informado
{
    for (int i = 0; i <= top; i++)
    {
        if (numero == this->contas[i].numero)
        {
            return &this->contas[i];
        }
    }

    return nullptr;
}

void Banco::atendimentoCliente() //Realiza o atendimento ao cliente(Função chamada na main)
{
    Conta *contaCliente;
    int numC = 0;
    int senhain;
    bool atendimento = true;

    cout << "Bem vindo ao sistema de atendimento do banco" << endl;
    cout << "Digite o numero da sua conta: ";
    cin >> numC;

    contaCliente = this->buscaConta(numC); //Chama o Metodo buscaConta() do banco para achar o objeto conta que possui o numero numC

    if (contaCliente == nullptr)//Se não achar nenhuma conta que corresponda entra nesse if
    {
        cout << "Conta invalida" << endl;
    }
    else
    {
        cout << "Digite a sua senha: ";
        cin >> senhain;

        if (contaCliente->validaSenha(senhain))
        {
            cout << "Ola " << contaCliente->titular << endl;
            while (atendimento) //Realiza o atendimento
            {
                int op;
                double valor;
                cout << "Qual operacao deseja fazer? (1 - Saque, 2 - Deposito, 3 - Ver Saldo, 4 - Transferencia, 5 - Sair): ";
                cin >> op;
                switch (op)
                {
                case 1:
                    cout << "Digite o valor: ";
                    cin>>valor;
                    contaCliente->saque(senhain,valor);
                    break;
                case 2:
                    cout << "Digite o valor: ";
                    cin>>valor;
                    contaCliente->deposito(valor);
                    break;
                case 3:
                    cout << "Saldo: R$ "<<contaCliente->getSaldo(senhain)<<endl;
                    break;
                case 4:
                    cout << "Digite o valor: ";
                    cin>>valor;
                    int numD;
                    cout << "Digite o número da conta de destino: ";
                    cin >> numD;
                    Conta *cdest;
                    cdest = this->buscaConta(numD);
                    contaCliente->transferencia(valor, senhain, cdest);
                    break;
                case 5:
                    atendimento = false;
                    break;
                }
            }
        }
        else
        {
            cout << "Senha invalida" << endl;
        }
    }
}

void Banco::atendimentoFuncionario(){
    int senhain;
    bool atendimento = true;
    cout << "Bem vindo ao sistema de atendimento do banco ao funcionário" << endl;
    cout << "Digite a sua senha: ";
    cin >> senhain;
    if (this->senhaFuncionario == senhain){
         cout << "Ola funcionário!" << endl;
            while (atendimento)
            {
                int opc;
                cout << "Qual operacao deseja fazer? (1 - Adicionar conta, 2 - Remover conta, 3 - Sair): ";
                cin >> opc;
                switch (opc)
                {
                    case 1:
                    {
                        int senha, numero;
                        std::string titular, tipo;
                        double saldo;
                        cout << "Digite a senha da conta a ser criada: ";
                        cin >> senha;
                        cout << "Digite o número da conta: ";
                        cin >> numero;
                        cout << "Digite o nome do titular: ";
                        cin >> titular;
                        cout << "Digite o tipo da conta (poupança/corrente): ";
                        cin >> tipo;
                        cout << "Digite a quantidade de dinheiro a ser depositada inicialmente na conta: ";
                        cin >> saldo;
                        adicionaConta(senha, numero, titular, tipo, saldo);
                        break;
                    }
                    case 2:
                        int numero;
                        cout << "Digite o número da conta: ";
                        cin >> numero;
                        removeConta(numero);
                        break;
                    case 3:
                        atendimento = false;
                        break;
                }
            }
    }
    else{
        cout << "Senha invalida" << endl;
    }
}

void Banco::adicionaConta(int senha, int numero, std::string titular, std::string tipo, double saldo){
    Conta *novaConta = new Conta(senha, numero, titular, tipo, saldo);
    Conta *contas = new Conta[++top+1];
    for (int i=0; i<top; i++){
        contas[i] = this->contas[i];
    }
    contas[top] = *novaConta;
    delete [] this->contas;
    this->contas = new Conta[top+1];
    this->contas = contas;
    cout << "Conta adicionada." << endl;
}

bool Banco::removeConta(int numero){
    Conta *contaCliente;
    contaCliente = this->buscaConta(numero);
    if (top == -1){
        cout << "Não existem contas" << endl;
    }
    else if (contaCliente == nullptr)
    {
        cout << "Conta invalida" << endl;
    }
    else
    {
        Conta *contas = new Conta[--top + 1];
        int i=0, j=0;
        while (i<=top){
            if (&this->contas[j] != contaCliente){
                contas[i] = this->contas[j];
                i++;
            }
            j++;
        }
        this->contas = contas;
        cout << "Conta removida, restam "<< top+1 << "." << endl;
        return true;
    }
    return false;
}