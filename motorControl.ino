int pulseDelay = 2;
int ppr =400;


#define dirPin 2
#define stepPin 3
int intin=0;
int currentPos=0;
String inByte;

void setup() {
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
if (Serial.available() > 0) {
    String inByte = Serial.readStringUntil("/n");
    intin=inByte.toInt();
}

  if(intin > currentPos){
    int setPos = intin;
  int cPos = currentPos;
    digitalWrite(dirPin,1);
  for(int x=cPos;x<setPos;x++){
    for(int y=0;y<ppr;y++){
      digitalWrite(stepPin,1);
      delay(pulseDelay);
      digitalWrite(stepPin,0);
      delay(pulseDelay);
      }
    cPos++;
    }
    currentPos=cPos;
  }

  if(intin < currentPos){
    int setPos = intin;
  int cPos = currentPos;
      digitalWrite(dirPin,0);
  for(int x=cPos;x>setPos;x--){
    for(int y=0;y<ppr;y++){
      digitalWrite(stepPin,1);
      delay(pulseDelay);
      digitalWrite(stepPin,0);
      delay(pulseDelay);
      }
    cPos--;
    }
    currentPos=cPos;
  }


  
      }
