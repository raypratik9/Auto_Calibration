/*  Connects to the home WiFi network
    Asks some network parameters
    Sends and receives message from the server in every 2 seconds
    Communicates: wifi_server_01.ino
*/
#include <SPI.h>
#include <ESP8266WiFi.h>

byte ledPin = 2;
char ssid[] = "JioFiber-8huUe";           // SSID of your home WiFi
char pass[] = "raypratik1@";            // password of your home WiFi

unsigned long askTimer = 0;

IPAddress server(192, 168, 29, 12);    // the fix IP address of the server
WiFiClient client;
void setup() {
  Serial.begin(9600);               // only for debug
  WiFi.begin(ssid, pass);             // connects to the WiFi router
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.print("connected");
  /*  Serial.println("Connected to wifi");
    Serial.print("Status: "); Serial.println(WiFi.status());    // Network parameters
    Serial.print("IP: ");     Serial.println(WiFi.localIP());
    Serial.print("Subnet: "); Serial.println(WiFi.subnetMask());
    Serial.print("Gateway: "); Serial.println(WiFi.gatewayIP());
    Serial.print("SSID: "); Serial.println(WiFi.SSID());
    Serial.print("Signal: "); Serial.println(WiFi.RSSI());*/
  pinMode(ledPin, OUTPUT);
}

void loop () {
  client.connect(server, 8080);   // Connection to the server
  digitalWrite(ledPin, LOW);    // to show the communication only (inverted logic)
  Serial.println(".");
  //client.println("Hello server! Are you sleeping?\r");  // sends the message to the server
  digitalWrite(ledPin, HIGH);
  while (1) {
    //client.println(2);
    long Data = client.readStringUntil('*').toInt();
    Serial.println(Data);
    digitalWrite(ledPin, HIGH);
    if(Data==1)
    {
      client.print(1);
    }
    yield();
  }
}
