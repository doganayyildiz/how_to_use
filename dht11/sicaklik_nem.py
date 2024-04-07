from machine import Pin, I2C 
from ssd1306 import SSD1306_I2C
from dht import DHT11 #dht kütüphanesi ekleme
import framebuf
import time


WIDTH = 128 
HEIGHT = 64 

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c,)

#dht11 tanımlama
pin = Pin(18,Pin.IN,Pin.PULL_UP)
dht11 = DHT11(pin,None,dht11=True)

while True:
    T,H = dht11.read()
    #sıcaklık ve nem değerlerini konsola yazdırmak için aşağıdaki 2 satırı kullanın
    #print("Sıcaklık: ",T)
    #print("Nem: ",H)
    
    #oled ekrana dht11 den gelen verileri yazdırma
    oled.fill(0)
    oled.text("SICAKLIK:",0,0)
    oled.text(str(T),80,0)
    oled.text("NEM:",0,15)
    oled.text(str(H),80,15)
    oled.show()
    time.sleep(1)
