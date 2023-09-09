// 1- Harshnandan Dasika - 652855943
// 2- Lab 2 - Input and Output 
// 3- Description - When a push-button switch is pressed, the Arduino will read the input and light up the lights accordingly, based on the binary number.
// 4- Assumptions - No assumptions
// 5- References - Only used the 3 links given in the prelab of the assignment.
// 6- Demo - In-person demonstration - 09/26/2022, 3:12pm, TA: Neel Parikh


const int b1 =  13;
const int b2 =  12;
const int b3 =  10;
const int b4 =  8;

const int button1 = 4;
const int button2 = 3;

int pressbutton = 0;
int value = 0;
int press1 = 0;
int press2 = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(b1, OUTPUT);
  pinMode(b2, OUTPUT);
  pinMode(b3, OUTPUT);
  pinMode(b4, OUTPUT);
  Serial.begin(9600);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  press1 = digitalRead(button1);
  press2 = digitalRead(button2);
  if (press1 == HIGH){
    pressbutton += 1;
    if (pressbutton > 15){
      pressbutton = 15;
    }
    delay(500);
    while (digitalRead(button1) == HIGH) {
      
    }
    Serial.print(pressbutton);
    
    
  } 
  
  if (press2 == HIGH){
    pressbutton -= 1;
    if (pressbutton < 0){
      pressbutton = 0;
    }
    delay(500);
    while (digitalRead(button2) == HIGH) {
      
    }
    Serial.print(pressbutton);
    
    
  }

  value = pressbutton;
  if (value >= 8) {
    value -= 8;
    digitalWrite(b1, HIGH);
  }
  else {
    digitalWrite(b1, LOW);
  }

  if (value >= 4){
    value -= 4;
    digitalWrite(b2, HIGH);
  }
  else {
    digitalWrite(b2, LOW);
  }

  if (value >= 2){
    value -= 2;
    digitalWrite(b3, HIGH);
  }
  else {
    digitalWrite(b3, LOW);
  }

  if (value >= 1){
    digitalWrite(b4, HIGH);
  }
  else {
    digitalWrite(b4, LOW);
  }
}
