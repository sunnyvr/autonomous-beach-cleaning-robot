#include<LiquidCrystal.h>

LiquidCrystal lcd(9, 8, 4, 5, 6, 7); // sets the interfacing pins
int d;
int t;
int triggerpin=13;
int echopin=12;
void setup() 
{
 lcd.begin(16, 2);
 lcd.setCursor(0,0);
 pinMode(triggerpin,OUTPUT);
 pinMode(echopin,INPUT); 
 lcd.clear();
 Serial.begin(9600);

}

void loop() 
{
 digitalWrite(triggerpin,LOW);
 delay(50);
 digitalWrite(triggerpin,HIGH);
 delay(50);
 digitalWrite(triggerpin,LOW);
 t=pulseIn(echopin,HIGH);
 d=t*0.034/2;
 lcd.print("Distance = ");
 lcd.setCursor(0,1);
 lcd.print(d);
 lcd.print("cm");
 delay(500);
 lcd.clear();
 Serial.print("distance: ");
 Serial.println(d);
}
 


