//Motion detector subsytem code - Ilyas.
//Communicates serially with the LED controller subsytem when digitalRead from the motion detector goes HIGH
void setup() {
  //setup pin 5 for reading motion detector input
  pinMode(5, INPUT);
  Serial.begin(115200);
}

void loop() {
  //if motion is detected, write to Serial
  if (digitalRead(5) == HIGH) {
    Serial.println('1');
  } else {
    Serial.println('0');
  }
}
