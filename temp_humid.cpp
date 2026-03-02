#include <DHT.h>

// ----- Choose your sensor type -----
#define DHTTYPE DHT11   // Change to DHT22 if you use DHT22
// #define DHTTYPE DHT22

// Pick a digital pin that does NOT conflict with your motor driver.
// D2 is usually safe on robot car kits.
const uint8_t DHTPIN = 2;

DHT dht(DHTPIN, DHTTYPE);

unsigned long lastReadMs = 0;
const unsigned long READ_INTERVAL_MS = 2000; // DHT sensors need ~2s between reads

void setup() {
  Serial.begin(9600);
  while (!Serial) { ; }

  dht.begin();
  Serial.println("DHT temperature/humidity reader started.");
}

void loop() {
  unsigned long now = millis();
  if (now - lastReadMs < READ_INTERVAL_MS) return;
  lastReadMs = now;

  float humidity = dht.readHumidity();
  float tempC = dht.readTemperature();       // Celsius
  float tempF = dht.readTemperature(true);   // Fahrenheit

  // If reading fails, library returns NaN
  if (isnan(humidity) || isnan(tempC) || isnan(tempF)) {
    Serial.println("Failed to read from DHT sensor (check wiring + sensor type).");
    return;
  }

  // Optional: Heat index (feels-like temp)
  float heatIndexC = dht.computeHeatIndex(tempC, humidity, false);

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %  | Temp: ");
  Serial.print(tempC);
  Serial.print(" °C (");
  Serial.print(tempF);
  Serial.print(" °F)  | HeatIndex: ");
  Serial.print(heatIndexC);
  Serial.println(" °C");
}
