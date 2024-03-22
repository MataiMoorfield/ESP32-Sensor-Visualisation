#include <WiFi.h>
#include <WebServer.h>
#include <ArduinoJson.h>

const char *ssid = "network_name";          // Change with network name
const char *password = "network_password";  // Change with network password

WebServer server(80);

void handleRoot() {
  StaticJsonDocument<200> doc;

  String words[] = {"apple", "banana", "orange", "grape", "kiwi"};
  int numWords = sizeof(words) / sizeof(words[0]);
  
  int randomIndex = random(0, numWords);
  
  float randomValue = random(0, 100); 
  
  String randomWord = words[randomIndex];
  
  Serial.print("Random Word: ");
  Serial.print(randomWord);
  Serial.print(", Random Value: ");
  Serial.println(randomValue); 

  doc["random_word"] = randomWord;
  doc["random_value"] = randomValue;

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
  
  randomSeed(analogRead(0));

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
