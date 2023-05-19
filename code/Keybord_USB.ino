
#include <Keyboard.h>

#define BUTTON 3
bool state = false;

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON, INPUT_PULLUP);
  Keyboard.begin();
}

void loop() {
  if(state){
    Keyboard.press('a');
    delay(100);
    Keyboard.releaseAll();
    delay(2000);

    Keyboard.press('b');
    delay(100);
    Keyboard.releaseAll();
    delay(2000);
  }

  if (digitalRead(BUTTON) == LOW && state == false) {
    Alt_Tab();
    state = true;
  }
  if (digitalRead(BUTTON) == HIGH && state == true){
    countdown();
    Alt_Tab();
    state = false;
  }
  delay(100);
}

void Alt_Tab(){
  Keyboard.press(KEY_LEFT_ALT);
  Keyboard.press(KEY_TAB);
  delay(100);
  Keyboard.releaseAll();
}

void countdown(){
    Keyboard.press('3');
    delay(100);
    Keyboard.releaseAll();
    delay(900);

    Keyboard.press('2');
    delay(100);
    Keyboard.releaseAll();
    delay(900);

    Keyboard.press('1');
    delay(100);
    Keyboard.releaseAll();
    delay(900);
}
