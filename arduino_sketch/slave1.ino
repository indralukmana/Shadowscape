#include <Wire.h>
#include <Stepper.h>

volatile  char what = 0;  // 接收命令 byte
String c;

int mov, sh, dire;
int loca= 5;
boolean movement = false;

const int stepsPerRevolution = 120;
Stepper myStepper(stepsPerRevolution, 12,13);  

const int pwmA = 3;
const int pwmB = 11;
const int brakeA = 9;
const int brakeB = 8;
const int dirA = 12;
const int dirB = 13;

int x = 0;

void setup() {
  Wire.begin(1);// join i2c bus with address #0
  Wire.onReceive (receiveEvent);
  Wire.onRequest(requestEvent); 

  pinMode(pwmA, OUTPUT);
  pinMode(pwmB, OUTPUT);
  pinMode(brakeA, OUTPUT);
  pinMode(brakeB, OUTPUT);
  digitalWrite(pwmA, HIGH);
  digitalWrite(pwmB, HIGH);
  digitalWrite(brakeA, LOW);
  digitalWrite(brakeB, LOW);

  Serial.begin(9600);
  myStepper.setSpeed(100);
}

void loop() {
  while(movement){
    for(;mov;mov--){
        if(dire){myStepper.step(-stepsPerRevolution);}
        else {myStepper.step(stepsPerRevolution);}
    }
  }
  movement = false;
}

void receiveEvent(int howMany){ 
  Serial.print("read");
  while (0 < Wire.available()) { // loop through all
    //Serial.print(Wire.read());
    sh= Wire.read(); 
  }
  if( sh > loca){ mov =(sh - loca); dire = 1;}
  else { mov = (loca - sh); dire = 0;}
  movement = true;
  loca = sh;
}

void requestEvent(){
  Wire.write("ok.");
  Serial.print("ok");
}
