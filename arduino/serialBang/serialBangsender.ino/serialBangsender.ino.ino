const int bangpin =  13;      // the number of the LED pin
const int bps = 10;  // 12か10
float deltime = 1000 / bps;
int sendByte = 0;         // incoming serial byte


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


void setup() {
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(bangpin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    sendByte = Serial.read();
    sendBang(sendByte);
  }
}
