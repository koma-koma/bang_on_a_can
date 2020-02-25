#include <MsTimer2.h>

const int bangpin =  9;      // the number of the LED pin
const int sndSWpin = 8;      // the number of the sound switch pin
const int bps = 12;
float deltime = 1000 / bps;
int sendByte = 0;         // incoming serial byte

int count = 0;
bool bReading = 0;
int t = 0;
int val = 0;


void bang(int pin) {
  digitalWrite(pin, HIGH);
  delay(10);
  digitalWrite(pin, LOW);
  delay(deltime - 10);
}

void sendBang(int sendByte) {
  bang(bangpin);  // start bang
  for (int i = 0; i < 8; i++) {
    if ((sendByte >> i) & 0b1) {
      bang(bangpin);
    } else {
      delay(deltime);
    }
  }
  delay(deltime);  // stop bit
}

void readBit() {
//  Serial.write(!t);
  val += (!t << count);
  count++;
  t = 1;
  if (count == 8) {
    MsTimer2::stop();
    bReading = 0;
  }
}

int receiveBang() {
//  Serial.println("start");
  count = 0;
  val = 0;
  bReading = 1;
  delay(deltime*0.5);
  MsTimer2::start();
  while (bReading) {
    int state = digitalRead(sndSWpin);
//    Serial.print(state);
    if (!state) {
      t = 0;
    }
//    Serial.print(t);
//    Serial.println(" loop");
    delay(1);
  }
//  Serial.println("end");
  return val;
}

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  // initialize the LED pin as an output:
  pinMode(bangpin, OUTPUT);
  pinMode(sndSWpin, INPUT);

  MsTimer2::set(deltime, readBit);
}

void loop() {
  int sndSWstate = digitalRead(sndSWpin);
  delay(1);

  if (!sndSWstate && !bReading) {
    int inByte = receiveBang();
    Serial.write(inByte);
//    Serial.println("");
  }
  
  if (Serial.available() > 0) {
    sendByte = Serial.read();
    sendBang(sendByte);
  }
}
