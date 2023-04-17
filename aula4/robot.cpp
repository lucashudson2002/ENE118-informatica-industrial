#include "robot.h"

void Robot::showPos(){
    cout << id << endl;
    cout << "X - " << pos[0] << endl;
    cout << "Y - " << pos[1] << endl;
}

void Robot::move(float t){
    pos[0] += speed[0] * t;
    pos[1] += speed[1] * t;
}

void Robot::changeSpeed(float vx, float vy){
    speed[0] = vx;
    speed[1] = vy;
}