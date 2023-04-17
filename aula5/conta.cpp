#include "conta.h"
#include <iostream>

Conta::Conta()
{
    this->numero = 0;
    this->senha = 1111;
    this->titular = "Nenhum";
    this->saldo = 0;
}

Conta::Conta(int senha, int numero, std::string titular, std::string tipo, double saldo)
{
    this->senha = senha;
    this->numero = numero;
    this->titular = titular;
    this->tipo = tipo;
    if(saldo>0)
    {
        this->saldo = saldo;
    }
    else
    {
        std::cout<<"Saldo inicial invalido"<<std::endl;
    }    
}

Conta::~Conta()
{
}

void Conta::exibeDados()
{
    std::cout<< "Titular: "<<this->titular<<std::endl;
    std::cout<< "Numero: "<<this->numero<<std::endl;
    std::cout<< "Tipo: "<<this->tipo<<std::endl;
}

double Conta::getSaldo(int senha)
{
    if(senha==this->senha)
    {
        return this->saldo;
    }
    else
    {
        std::cout<<"Senha inválida"<<std::endl;
        return -10000000;
    }    

}

void Conta::setSaldo(double valor)
{
    if(valor>0)
        this->saldo = valor;
    else
        std::cout<<"Valor inválido"<<std::endl;
}

void Conta::setSenha(int novaSenha)
{
    this->senha = novaSenha;
}

void Conta::deposito(double valor)
{
    if(valor>0)
    {
        this->saldo+=valor;
    }
    else
    {
        std::cout<<"Valor invalido"<<std::endl;
    }
    
}

bool Conta::saque(int senha, double valor)
{
    if(senha==this->senha)
    {
        if(this->saldo>valor)
        {
            this->saldo-=valor;
            std::cout<<"Saque de R$"<<valor<<" realizado com sucesso."<<std::endl;
            return true;
        }
        else
        {
            std::cout<<"Saldo insuficiente"<<std::endl;
        }    
    }
    else
    {
        std::cout<<"Senha invalida"<<std::endl;
    }
    return false;
}

bool Conta::validaSenha(int senha)
{
    return (this->senha == senha);   
}

bool Conta::transferencia(float valor, int senha, Conta* cdest){
    if (validaSenha(senha)){
        if (saque(senha, valor)){
            cdest->deposito(valor);
            return true;
        }
    }
    return false;
}