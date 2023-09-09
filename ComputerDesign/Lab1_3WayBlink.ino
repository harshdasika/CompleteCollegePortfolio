// 1- Harshnandan Dasika - 652855943
// 2- Lab 1 - Get started with Arduino -  blinking lights_ 
// 3- Description - The LED on 13 blinks first, and then the red and green LED's need to blink one after the other with a delay in between.
// 4- No assumptions for this lab
// 5- References - I only used the Arduino documentation provided in the Lab 1 document on Blackboard
// 6- Demo: In-person Demo: Neel Parikh

unsigned long myTime;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  myTime = millis();                 // get runtime from start
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  while (millis() < myTime + 1000) {
    
  }
  myTime = millis() + 1000;
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  while (millis() < myTime) {
    
  }
 
  myTime = millis();                 // get runtime from start
  digitalWrite(12, HIGH);   // turn the LED on (HIGH is the voltage level)
  while (millis() < myTime + 1000) {
    
  }
  myTime = millis() + 1000;
  digitalWrite(12, LOW);    // turn the LED off by making the voltage LOW
  while (millis() < myTime) {
    
  }

  myTime = millis();                 // get runtime from start
  digitalWrite(10, HIGH);   // turn the LED on (HIGH is the voltage level)
  while (millis() < myTime + 1000) {
    
  }
  myTime = millis() + 1000;
  digitalWrite(10, LOW);    // turn the LED off by making the voltage LOW
  while (millis() < myTime) {
    
  }
}
