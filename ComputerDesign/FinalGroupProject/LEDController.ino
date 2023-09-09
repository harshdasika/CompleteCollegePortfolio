//
// Name: Tom Roller
//
// This is the code for the LED Controller subsystem. It takes in data from the Bluetooth
// subsystem as well as the Motion Sensor subsystem and turns the LEDs on or off based
// on that data.
//

// Libraries needed
#include <Adafruit_NeoPixel.h>
#include <SoftwareSerial.h>

// Variables
#define PIN 6
#define hardwareTx = 1;
#define hardwareRx = 0;

char readValue = '0';
char bluetoothState = '0';
char motionState = '0';

// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(250, PIN, NEO_GRB + NEO_KHZ800);
SoftwareSerial motionSerial(11, 10); // Rx, Tx

//
// setup()
//
// This function initializes the Serial communication and LED strip.
//
void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  Serial.begin(9600);
  motionSerial.begin(115200);
}

//
// loop()
//
// This function runs over and over in a loop.
// It reads data and updates variables as needed.
//
void loop() {
  if (Serial.available()) {                 // Bluetooth module
    readValue = Serial.read();
    Serial.println(readValue);
    bluetoothState = readValue;
  }
  if (motionSerial.available()) {           // Motion sensor
    readValue = motionSerial.read();
    motionSerial.println(readValue);
    motionState = readValue;
  }
  if (bluetoothState == '1' && motionState == '1') { 
    // Sends theater pixel chase
    theaterChase(strip.Color(127, 127, 127), 50); // White
    theaterChase(strip.Color(127,   0,   0), 50); // Red
    theaterChase(strip.Color(  0,   0, 127), 50); // Blue
  } else {
    strip.show();       // Turns off the LED strip
  }
}

//
// theaterChase
//
// This code creates a theatre-style crawling lights. The lights appear to move
// in a linear fashion and can be changed with color.
//
void theaterChase(uint32_t c, uint8_t wait) {
  for (int j=0; j<10; j++) {  //do 10 cycles of chasing
    for (int q=0; q < 3; q++) {
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, c);    //turn every third pixel on
      }
      strip.show();

      delay(wait);

      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}
