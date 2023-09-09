// 1- Harsh Dasika - 652855943
// 2- Lab 6 - Serial Communication 
// 3- Description - pretty much the same as Lab 2, but will be controlled by the software serial and the buttons.
// 4- No assumptions made
// 5- References - Only used the link provided in the lab document
// 6- Demo: In-person demonstration: 10/31/2022, 4:06pm, TA: Amir

#include <SoftwareSerial.h>
const byte rxPin = 10;
const byte txPin = 8;
SoftwareSerial mySerial (rxPin, txPin);

const int b1 = 7;
const int b2 = 6;
const int b3 = 5;
const int b4 = 4;

const int button1 = 11;
const int button2 = 3;

int press1 = 0;
int press2 = 0;
int c1 = 0;
int c2 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  mySerial.begin(9600);
  pinMode(b1, OUTPUT);
  pinMode(b2, OUTPUT);
  pinMode(b3, OUTPUT);
  pinMode(b4, OUTPUT);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
}


void loop() {

  press1 = digitalRead(button1);
  press2 = digitalRead(button2);
  
  // put your main code here, to run repeatedly:
  if (press1 == HIGH){  // button1 pressed
    delay(25);
    while(digitalRead(button1) == HIGH){
      
    }
    delay(25);
    Serial.write('c');  // write to serial
  }
  
  if (press2 == HIGH){  // button2 pressed
    delay(25);
    while(digitalRead(button2) == HIGH){
      
    } 
    delay(25);
    mySerial.write('d');  // write to myserial
  }

  
  if (Serial.available()){  // if serial has received
   char y = Serial.read();  // read what's been received
    if (y == 'd')
    c1++;
    if(c1 >3){
      c1 = 0;
    }
      if (c1 == 1){
        digitalWrite(b3, HIGH);
        digitalWrite(b4, LOW);
      }
      else if (c1 == 2){
        digitalWrite(b3, LOW);
        digitalWrite(b4, HIGH);
      }
      else if (c1 == 3){
        digitalWrite(b3, HIGH);
        digitalWrite(b4, HIGH);
      }
      else{
        digitalWrite(b3, LOW);
        digitalWrite(b4, LOW);
      }
  }

  if (mySerial.available()){  // if myserial has received
    char x = mySerial.read();  // read what's been received
    if (x == 'c')
    c2++;
    if(c2 >3){
      c2 = 0;
    }
      if (c2 == 1){
        digitalWrite(b1, HIGH);
        digitalWrite(b2, LOW);
      }
      else if (c2 == 2){
        digitalWrite(b1, LOW);
        digitalWrite(b2, HIGH);
      }
      else if (c2 == 3){
        digitalWrite(b1, HIGH);
        digitalWrite(b2, HIGH);
      }
      else{
        digitalWrite(b1, LOW);
        digitalWrite(b2, LOW);
      }
  }

    
//  int value1 = c1;
//  if (value1 >= 2){
//    value1 -= 2;
//    digitalWrite(b1, HIGH);
//  }
//  else {
//    digitalWrite(b1, LOW);
//  }
//  if (value1 >= 1){
//    digitalWrite(b2, HIGH);
//  }
//  else {
//    digitalWrite(b2, LOW);
//  }
//
//  int value2 = c2;
//  if (value2 >= 2){
//    value2 -= 2;
//    digitalWrite(b3, HIGH);
//  }
//  else {
//    digitalWrite(b3, LOW);
//  }
//  if (value2 >= 1){
//    digitalWrite(b4, HIGH);
//  }
//  else {
//    digitalWrite(b4, LOW);
//  }
}
