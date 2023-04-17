#include <iostream>

using namespace std;

float fatorial (float x){
    int fat = 1;
    for (int j=x; j>1; j--)
        fat = fat*j;
    return fat;
}

float potencia (float x, int e){
    int pot = 1;
    for (int j=e; j>0; j--)
        pot = pot*x;
    return pot;
}

float equacao1 (float x){
    return 5*4*3*2*x*x*x + 4*3*2*x*x + 3*2*x + 2;
}

float equacao2 (float x){
    float result = 0;
    for (int i=3; i>=0; i--){
        result = result + fatorial(i+2)*potencia(x,i);
    }        
    return result;
}

int main()
{
    cout << "Usando o método 1:" << endl;
    cout << "y(3) = " <<equacao1(3) << endl;
    cout << "y(3!) = " << equacao1(fatorial(3)) << endl;
    cout << "y(2^3) = " << equacao1(potencia(2,3)) << endl;
    
    cout << "Usando o método 2:" << endl;
    cout << "y(3) = " << equacao2(3) << endl;
    cout << "y(3!) = " << equacao2(fatorial(3)) << endl;
    cout << "y(2^3) = " << equacao2(potencia(2,3)) << endl;
    return 0;
}

