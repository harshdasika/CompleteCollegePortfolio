// 1- Harsh Dasika - 652855943
// 2- Lab 8 - Graphing Sensor Data on a PC
// 3- Description - Should display the live Serial values from the potentiometer and photoresistor as graphs using the Processing program.
// 4- Assumptions - No assumptions made.
// 5- References - Only used the links provided in the lab assignment sheet.
// 6- Demo - In-person demonstration, 11/14/2022, 3:20pm, TA: Michael Carnowell

import processing.serial.*;

Serial myPort;        // The serial port

int xPos = 0; 
int xPos1 = 0;
float inByte = 0;
float inByte1 = 0;

void setup () {
  // set the window size:
  size(800, 700);
  
  // open Serial.list()[4].
  myPort = new Serial(this, Serial.list()[4], 9600);

  // don't generate a serialEvent() unless you get a newline character:
  myPort.bufferUntil('\n');

  // set initial background:
  background(0);
}

void draw () {
  // draw the splitting line:
  stroke(255, 255, 255);
  line(0, height/2, width, height/2);
  
  // draw the graphs for both sensors
  stroke(127, 34, 255);
  line(xPos, height/2, xPos, height/2 - inByte);
  stroke(231, 163, 82);
  line(xPos1, height, xPos1, height - inByte1);

  // at the edge of the screen, go back to the beginning:
  if (xPos >= width) {
    xPos = 0;
    xPos1 = 0;
    background(0);
  } else {
    // increment the horizontal position:
    xPos++;
    xPos1++;
  }
}

void serialEvent (Serial myPort) {
  // get the ASCII string:
  String temp = myPort.readStringUntil('\n');
  String[] stringRead = split(temp,',');
  String inString = stringRead[0];
  String inString1 = stringRead[1];
  println(inString);
  println(inString1);
  if (inString != null) {
    // trim off any whitespace:
    inString = trim(inString);
    inByte = float(inString);
    inByte = map(inByte, 0, 1023, 0, height); // map it on the display
  }
  if (inString1 != null){
      // trim off any whitespace
      inString1 = trim(inString1);
      inByte1 = float(inString1);
      inByte1 = map(inByte1, 0, 1023, 0, height/2);  // map it on the display
  }
}
