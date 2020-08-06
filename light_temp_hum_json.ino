#include <dht.h>
#include <ArduinoJson.h>

int brightSensorPin = A0;
int brightSensorValue = 0;

dht DHT;
#define DHT11_PIN 5

void setup() {
  Serial.begin(9600);
  Serial.flush();
}

void loop() {
  String output;
  int chk = DHT.read11(DHT11_PIN);
  DynamicJsonDocument doc(128);

  brightSensorValue = analogRead(brightSensorPin);
  
  doc["temperature"] = (int) DHT.temperature; 
  doc["humidity"] = (int) DHT.humidity;
  doc["brightness"] = (int) brightSensorValue;
  
  serializeJson(doc, output);
  Serial.println(output);
  delay(5000);
}
