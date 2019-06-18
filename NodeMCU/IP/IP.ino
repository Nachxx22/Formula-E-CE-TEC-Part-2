#include  <ESP8266WiFi.h>

const char* ssid = "Nacho";
const char* password= "21012101";


void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
WiFi.begin(ssid,password);
while (WiFi.status() !=WL_CONNECTED){
  delay(300);
  Serial.print(".");
}
Serial.print("");
Serial.print("WiFi conectado!");
Serial.print(WiFi.localIP());
}

void loop() {
  // put your main code here, to run repeatedly:

}
