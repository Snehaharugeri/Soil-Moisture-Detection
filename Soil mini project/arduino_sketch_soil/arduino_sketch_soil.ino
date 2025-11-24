int sensorPin = A0;
int buzzerPin = 8;
int moistureValue = 0;

void setup() {
  Serial.begin(9600);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  moistureValue = analogRead(sensorPin);
  Serial.println(moistureValue);

  if (moistureValue < 120) {
    digitalWrite(buzzerPin, HIGH); // Turn on buzzer
  } else {
    digitalWrite(buzzerPin, LOW); // Turn off buzzer
  }

  delay(1000);
}
