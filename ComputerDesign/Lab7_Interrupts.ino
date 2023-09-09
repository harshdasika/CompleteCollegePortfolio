// 1- Harsh Dasika - 652855943
// 2- Lab 7 - Interrupts
// 3- Description - what is this code supposed to do?
// 4- Assumptions - No assumptions made
// 5- References - Only used the links provided in the lab assignment document
// 6- Demo - In-person demonstration, 11/7/2022, 4:14pm, TA: Michael 



// include the library code:
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 7, d5 = 6, d6 = 5, d7 = 4;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

const int button1 = 3;
const int button2 = 2;
int pressbutton = 0;
int value = 0;
int press1 = 0;
int press2 = 0;
unsigned long myTime;
boolean pressed = true;


void setup(){
  Serial.begin(9600);
  lcd.begin(16, 2);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  attachInterrupt(digitalPinToInterrupt(button1), button1_Interrupt, CHANGE);  // interrupt for button 1
  attachInterrupt(digitalPinToInterrupt(button2), button2_Interrupt, CHANGE);  // interrupt for button 2
}

void button1_Interrupt(){
  pressed = false;    // set it to false when pressed
  myTime = 0;     // reset time
  
}

void button2_Interrupt(){
  pressed = true;      // set to opposite of button 1
}


void loop(){
  
  if(!pressed){   // if pressed
    lcd.clear();     // clear screen
    lcd.print("Interrupted! :)");   // print interrupted
  }
  else{
  
    lcd.setCursor(0,0);
  
    lcd.print("Waiting for " + String(myTime++) + "   ");  // time counter

    lcd.setCursor(0,1);
    lcd.print("   seconds");  // just printing seconds on 2nd line
  }

  delay(1000);

}
