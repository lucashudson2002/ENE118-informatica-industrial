#include <cstdlib>
#include <ctime>
#include <iostream>
#include "mobilerobot.h"

void ExecutaMovimento(MobileRobot *ptr){
    double Xvel = rand()%100;
    double Yvel = rand()%100;
    double Zvel = rand()%100;
    double tempo = rand()%100;
    cout << "Xvel: " << Xvel << endl;
    cout << "Yvel: " << Yvel << endl;
    cout << "Zvel: " << Zvel << endl;
    cout << "Tempo: " << tempo << endl;
    ptr->Mover(Xvel,Yvel,Zvel,tempo);
}

using namespace std;

int main()
{
    srand((unsigned)time(0));
    RoboTerrestre *drone = new RoboTerrestre();
    ExecutaMovimento(drone);
    delete drone;
    return 0;
}

