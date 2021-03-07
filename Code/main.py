import wifi
import lora
import ultrasonic
import adafruit
import time

#   ------------------------------------
# | Uncomment the method you want to use |
#   ------------------------------------

# Connect and send data with LoRa
# lora.connect()
# ultasonic.read_uart()

# while True:
    # ultasonic.read_uart()
    # distance = ultasonic.getDistance()
    # lora.send(distance)
    # print(distance)
    # time.sleep(10)

# Connect and send data with WiFi
wifi.connectHome()
ultasonic.read_uart()

while True:
    ultrasonic.read_uart()
    distance = ultrasonic.getDistance()
    adafruit.sendDataWifi(distance)
    print(distance)
    time.sleep(10)
