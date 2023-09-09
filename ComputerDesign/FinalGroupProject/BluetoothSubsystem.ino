//Bluetooth system - Harsh 
//Communicates serially with the LED controller subsystem via a software serial port
#include <SoftwareSerial.h>
char Incoming_value = 0;                //Variable for storing Incoming_value

const int softwareTx = 9;
const int softwareRx = 10; 

SoftwareSerial softwarePort (softwareRx, softwareTx); //instantiate software port

void setup() 
{
  Serial.begin(9600);         
  softwarePort.begin(9600);

  pinMode(softwareTx, OUTPUT);//initialize software pins
  pinMode(softwareRx, INPUT);

}
void loop()
{
  if(Serial.available() > 0)
  {
    Incoming_value = Serial.read();      //Read the incoming data and store it into variable Incoming_value
    Serial.println(Incoming_value);        //Print Value of Incoming_value in Serial monitor
    //Serial.print("\n");        //New line 
    if(Incoming_value == '1')  {          //Checks whether value of Incoming_value is equal to 1 
     // Serial.println("recieved 1, sending on signal to controller");
      softwarePort.write('1');  //If value is 1 then LED turns ON
  }
    else if(Incoming_value == '0') {      //Checks whether value of Incoming_value is equal to 0
      //Serial.println("recieved 0, sending off signal to controller");
      softwarePort.write('0');   //If value is 0 then LED turns OFF
  }
 
}
}
