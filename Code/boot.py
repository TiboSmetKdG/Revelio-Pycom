from network import WLAN
import pycom
import machine
wlan = WLAN(mode=WLAN.STA)
pycom.heartbeat(False)

#wlan.connect(ssid='IoT', auth=(WLAN.WPA2, 'KdGIoT92!'))
wlan.connect(ssid='Pretty fly for a wifi', auth=(WLAN.WPA2, 'discobar'))

while not wlan.isconnected():
    pycom.rgbled(0xFF00FF)
print("WiFi connected succesfully")
pycom.rgbled(0x3B7A57)
print(wlan.ifconfig())
