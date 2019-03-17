#include <Wire.h>
#include "MMA7660.h"
MMA7660 accelemeter;
void setup()
{
	accelemeter.init();  
	Serial.begin(9600);
}
void loop()
{
	float ax,ay,az;
	accelemeter.getAcceleration(&ax,&ay,&az);
        Serial.println(sqrt( pow(ax, 2) + pow(ay, 2) + pow(az, 2)));
        delay(50);
}


