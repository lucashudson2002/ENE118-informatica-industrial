#include <iostream>

using namespace std;

int size (char* string){
    int i;
    for (i = 0; string[i]!='\0'; i++){}
    return i;
}

void inverteNome(char* nome){
    int len = size(nome);
    for (int i=0; i<len/2; i++){
        char aux = nome[i];
        nome[i] = nome[len-i-1];
        nome[len-i-1] = aux;
    }
}

int main()
{
    char nome[50];
    cout << "Digite seu nome: ";
    cin >> nome;
    inverteNome(nome);
    cout << nome;
    return 0;
}


