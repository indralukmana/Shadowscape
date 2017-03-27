#include <Wire.h>

char mov;
int shc,shh,shm;
String c;
char shcc;
int dire;
String date = "";

void setup() {
  Wire.begin();
  Serial.println("begin");
  int loca = 0;
  Serial.begin(9600);
}

void loop() {
  //Serial.println("start");
  date="";
  if(Serial.available()){
    while (Serial.available())  {
      date = char(Serial.read());
      Serial.println(date);
      delay(10);     
    }
    Serial.println("hey");
  }
  
  if(date == "0"){
    shc = 5; shh = 2; shm = 1;
    Serial.println("aa");
    Wire.beginTransmission(0);  //準備送信息去給 Slave 0
    Wire.write(shc);
    Wire.endTransmission( );   // 真正開始傳送
    delay(50);
    Serial.println("fi");
    delay(10);
    Wire.beginTransmission(1);  
    Wire.write(shh);
    Wire.endTransmission( );  
    delay(10);
    Wire.beginTransmission(2);  
    Wire.write(shm);
    Wire.endTransmission( );  

    delay(50);
    
   /* Wire.requestFrom(0, 4); // request 4 bytes (max32) from slave device #2
    delay(50);
    while (Wire.available()){
      c += Wire.read();
      Serial.print(c);   
    }*/
  }

  else if(date == "1"){
    shc = 6; shh = 3; shm = 0;
    Wire.beginTransmission(0);  //準備送信息去給 Slave 0
    Wire.write(shc);
    Wire.endTransmission( );   // 真正開始傳送
    delay(10);
    Wire.beginTransmission(1);  
    Wire.write(shh);
    Wire.endTransmission( );  
    delay(10);
    Wire.beginTransmission(2);  
    Wire.write(shm);
    Wire.endTransmission( );  

    delay(50);
  }

  else if(date == "2"){
    shc = 5; shh = 1; shm = 1;
    Wire.beginTransmission(0);  //準備送信息去給 Slave 0
    Wire.write(shc);
    Wire.endTransmission( );   // 真正開始傳送
    delay(10);
    Wire.beginTransmission(1);  
    Wire.write(shh);
    Wire.endTransmission( );  
    delay(10);
    Wire.beginTransmission(2);  
    Wire.write(shm);
    Wire.endTransmission( );  

    delay(50);
  }

    else if(date == "3"){
    shc = 5; shh = 1; shm = 2;
    Wire.beginTransmission(0);  //準備送信息去給 Slave 0
    Wire.write(shc);
    Wire.endTransmission( );   // 真正開始傳送
    delay(10);
    Wire.beginTransmission(1);  
    Wire.write(shh);
    Wire.endTransmission( );  
    delay(10);
    Wire.beginTransmission(2);  
    Wire.write(shm);
    Wire.endTransmission( );  

    delay(50);   
  }

    else if(date == "4"){
    shc = 8; shh = 3; shm = 3;
    Wire.beginTransmission(0);  //準備送信息去給 Slave 0
    Wire.write(shc);
    Wire.endTransmission( );   // 真正開始傳送
    delay(10);
    Wire.beginTransmission(1);  
    Wire.write(shh);
    Wire.endTransmission( );  
    delay(10);
    Wire.beginTransmission(2);  
    Wire.write(shm);
    Wire.endTransmission( );  

    delay(50);
  }

    else if(date == "5"){
    shc = 8; shh = 1; shm = 2;
    Wire.beginTransmission(0);  //準備送信息去給 Slave 0
    Wire.write(shc);
    Wire.endTransmission( );   // 真正開始傳送
    delay(10);
    Wire.beginTransmission(1);  
    Wire.write(shh);
    Wire.endTransmission( );  
    delay(10);
    Wire.beginTransmission(2);  
    Wire.write(shm);
    Wire.endTransmission( );  

    delay(50);
  }
    else if(date == "6"){
    shc = 10; shh = 2; shm = 0;
    Wire.beginTransmission(0);  //準備送信息去給 Slave 0
    Wire.write(shc);
    Wire.endTransmission( );   // 真正開始傳送
    delay(10);
    Wire.beginTransmission(1);  
    Wire.write(shh);
    Wire.endTransmission( );  
    delay(10);
    Wire.beginTransmission(2);  
    Wire.write(shm);
    Wire.endTransmission( );  

    delay(50); 
  }

      else if(date == "7"){
    shc = 0; shh = 0; shm = 0;
    Wire.beginTransmission(0);  //準備送信息去給 Slave 0
    Wire.write(shc);
    Wire.endTransmission( );   // 真正開始傳送
    delay(10);
    Wire.beginTransmission(1);  
    Wire.write(shh);
    Wire.endTransmission( );  
    delay(10);
    Wire.beginTransmission(2);  
    Wire.write(shm);
    Wire.endTransmission( );  

    delay(50); 
  }
  
  delay(500);
  //Serial.println( );
}
