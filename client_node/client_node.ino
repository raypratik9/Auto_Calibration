#include <ESP8266WiFi.h>
const char* ssid = "JioFiber-8huUe_5G";    // Enter SSID here
const char* password = "raypratik2@";  //Enter Password here
int z;
const char* server = "192.168.29.12";
WiFiClient server1;
void setup()
{
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
  Serial.println(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
}
void loop() {
   if (! server1.connect(server,1000))
    Serial.println("Failed to connect to server");
  while(1)
  {
    while(server1.available()){
      z = server1.readStringUntil('*').toInt();
    Serial.println(z);
    Serial.println();
    yield();
  }
 }
}
