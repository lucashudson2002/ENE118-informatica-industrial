#ifndef ROBOT_H
#define ROBOT_H

#include <iostream>
using namespace std;

class Robot{
public:
    string id;
    float pos[2];
    float speed[2];
    
    void showPos();
    void move(float);
    void changeSpeed(float, float);
};

#endif