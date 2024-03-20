#include <WiFi.h>
#include <WebServer.h>
#include <ArduinoJson.h>
#include <Wire.h>
#include <MPU6050.h>

const char *ssid = "ORBI37";
const char *password = "helpfulshrub878";

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



void setup() {
  Serial.begin(115200);

  Wire.begin();
  mpu.initialize();
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to WiFi");

  server.on("/", handleRoot);

  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}
