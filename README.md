# Adafruit VL53L0X Time of Flight Sensor:
Deze sensor kan versnelling meten door gebruikt te maken van een laser en sensor die de laser op vangt.
  # Aansluitingen:
  Power Pins:
  -   Vin: Deze pin vormt de normale 3.3V of 5V en vervormt dit naar 2.8V zodat de chip deze kan gebruiken.
  -   2v8: Dit is een 2.8V output.

  GND: Ground

  I2C pins: 
  -   SCL: I2C Clock pin
  -   SDA: I2C Data pin
  -   STEMMA QT: Deze connector zorgt ervoor dat je verbinding kan maken met een STEMMA QT development board of gelijkaardige accessoires.
 
  Control Pins:
  -   GPIO: Deze pin toont aan wanneer data klaar is voor gebruik.
  -   SHDN: De “shutdown pin” van de sensor, deze staat standaard op high maar als deze op low komt gaat de sensor in shutdown mode.
# Libraries:
Adafruit_CircuitPython_VL53L0X: https://github.com/adafruit/Adafruit_CircuitPython_VL53L0X
