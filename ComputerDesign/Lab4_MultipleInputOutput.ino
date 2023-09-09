// 1- Harsh Dasika - 652855943
// 2- Lab 4 - Multiple Inputs and Outputs 
// 3- Description - The 4 LED's should become brighter or darker depending on how much light is detected by the photoresistor. 
///                 Simultaneously, the buzzer should work independently and the loudness should be controlled by the potentiometer.
// 4- Assumptions - No assumptions made.
// 5- References - Only used the links provided in the lab assignment sheet.
// 6- Demo - In-person demonstration, 10/10/2022, 10:54 a.m., TA: Michael


// where I've plugged in the various components
const int photoR = A0;
int lightBrightness;
int passiveBuzzer = 10;
int led_1 = 5;
int led_2 = 4;
int led_3 = 3;
int led_4 = 2;


void setup() {
  // put your setup code here, to run once:
  // input device
  pinMode(photoR, INPUT);

  // output devices
  pinMode(passiveBuzzer, OUTPUT);
  pinMode(led_1, OUTPUT);
  pinMode(led_2, OUTPUT);
  pinMode(led_3, OUTPUT);
  pinMode(led_4, OUTPUT);
}



void loop() {
  // put your main code here, to run repeatedly:

  // read the "brightness" and assign to a variable
  lightBrightness = analogRead(photoR);

  if (lightBrightness < 600){   // when darkest, all 4 on
    digitalWrite(led_1, HIGH);
    digitalWrite(led_2, HIGH);
    digitalWrite(led_3, HIGH);
    digitalWrite(led_4, HIGH);
  }
  else if (lightBrightness < 700){   // when slightly brighter, 3 lights on
    digitalWrite(led_1, HIGH);
    digitalWrite(led_2, HIGH);
    digitalWrite(led_3, HIGH);
    digitalWrite(led_4, LOW);
  }
  else if (lightBrightness < 800){  // when slightly more bright, 2 lights on
    digitalWrite(led_1, HIGH);
    digitalWrite(led_2, HIGH);
    digitalWrite(led_3, LOW);
    digitalWrite(led_4, LOW);
  }
  else if (lightBrightness < 900){  // when very bright, 1 light on
    digitalWrite(led_1, HIGH);
    digitalWrite(led_2, LOW);
    digitalWrite(led_3, LOW);
    digitalWrite(led_4, LOW);

  }
  else if (lightBrightness < 1000){  // at brightest, no lights on
    digitalWrite(led_1, LOW);
    digitalWrite(led_2, LOW);
    digitalWrite(led_3, LOW);
    digitalWrite(led_4, LOW);

  }

  delay(400);

  // read the potentiometer
  int buzzerVal = analogRead(A1);
  // between a range from 1-1023 to 0-255
  buzzerVal = map(buzzerVal, 0, 1023, 0, 255);
  // write to what's plugged in at position 10 
  analogWrite(10, buzzerVal);
}
