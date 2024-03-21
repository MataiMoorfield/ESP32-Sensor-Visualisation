#include <WiFi.h>
#include <WebServer.h>
#include <ArduinoJson.h>
#include <Wire.h>
#include <MPU6050.h>

const char *ssid = "network_name";          // Change with network name
const char *password = "network_password";  // Change with network password

WebServer server(80);

MPU6050 mpu;

void handleRoot() {
  StaticJsonDocument<200> doc;
  
  float ax = mpu.getAccelerationX();
  float ay = mpu.getAccelerationY();
  float az = mpu.getAccelerationZ();
  float gx = mpu.getRotationX();
  float gy = mpu.getRotationY();
  float gz = mpu.getRotationZ();

  Serial.print(ax);
  Serial.print(',');
  Serial.print(ay);
  Serial.print(',');
  Serial.print(az);
  Serial.print(','); 
  Serial.print(gx);
  Serial.print(','); 
  Serial.print(gy);
  Serial.print(','); 
  Serial.println(gz); 

  doc["acceleration_x"] = ax;
  doc["acceleration_y"] = ay;
  doc["acceleration_z"] = az;
  doc["gyroscope_x"] = gx;
  doc["gyroscope_y"] = gy;
  doc["gyroscope_z"] = gz;
  
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

  Wire.begin();
  mpu.initialize();
  
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
