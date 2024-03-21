#include <WiFi.h>
#include <WebServer.h>
#include <ArduinoJson.h>
#include <Wire.h>
#include <DHT.h> 

const char *ssid = "network_name";          // Change with network name
const char *password = "network_password";  // Change with network password

WebServer server(80);

#define DHTPIN 4       // Connect sensor to D4
#define DHTTYPE DHT11  

DHT dht(DHTPIN, DHTTYPE);

void handleRoot() {
  StaticJsonDocument<200> doc;
  
  float temperature = dht.readTemperature(); 
  float humidity = dht.readHumidity();      

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print("°C, Humidity: ");
  Serial.print(humidity);
  Serial.println("%"); 

  doc["temperature"] = temperature;
  doc["humidity"] = humidity;
  
  String json;
  serializeJson(doc, json);
  
  server.send(200, "application/json", json);
}

void printWiFiInfo() {
  Serial.println("");
  Serial.println("WiFi connected!");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(115200);

  dht.begin();
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  
  printWiFiInfo();
  
  server.on("/", handleRoot);
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}
