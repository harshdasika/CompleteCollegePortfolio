// 1- Harsh Dasika - 652855943
// 2- Lab 3 - LCD 
// 3- Description - The LCD should display a scrolling quote on the top and the user's name on the bottom which does not scroll.
// 4- Assumptions - No assumptions made for this lab.
// 5- References - Only the links provided in the lab assignment sheet were used.
// 6- Demo - In person demonstration, 10/3/2022, 9:47a.m., TA: Neel Parikh

// include the library code:
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);


String nameStr = "Harsh D.";
int counter = 0;

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  lcd.setCursor(4,1);
  char str2[8];
  sprintf(str2, "%s", "Harsh D.");
  lcd.print(str2);
}

void loop() {
  lcd.setCursor(0,0);
  // scroll
  String str1 = "May the Force be with you. ";
  delay(1000);
  for (int x = 0; x < 16; x++) {
    // Will print one character to the right each time.
    // tempVal stores the starting index for the next print on the scroll.
    int tempVal = (counter + x) % str1.length();
    lcd.print(str1[tempVal]);
  }
  counter++;
}
