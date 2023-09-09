// 1- Harsh Dasika - 652855943
// 2- Lab 8 - Graphing Sensor Data on a PC
// 3- Description - Should display the live Serial values from the potentiometer and photoresistor as graphs using the Processing program.
// 4- Assumptions - No assumptions made.
// 5- References - Only used the links provided in the lab assignment sheet.
// 6- Demo - In-person demonstration, 11/14/2022, 3:20pm, TA: Michael Carnowell

String conc;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(analogRead(A0));  // photoresistor
  Serial.print(",");  // delimiter
  Serial.println(analogRead(A1));  // potentiometer
  delay(100);
}
