from machine import Pin, I2C
import ssd1306 
import dht
import time

# ✅ Define hardware pins
DHT_PIN = 4  # DHT22 (or DHT11) data pin
BUTTON_PIN = 0  # Button input pin

# ✅ Initialize DHT sensor (Change DHT22 to DHT11 if needed)
dht_sensor = dht.DHT22(Pin(DHT_PIN))

# ✅ Initialize OLED display
i2c = I2C(scl=Pin(9), sda=Pin(8))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# ✅ Button setup (Polling method)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)  # Active LOW button

# ✅ Track button state manually
oled_state = True  # OLED is initially ON

# ✅ Main loop (Polling-based button check)
while True:
    try:
        # ✅ Read temperature & humidity from DHT sensor
        dht_sensor.measure()
        time.sleep(0.2)  # Small delay for stability
        temp = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        print("Temp:", temp, "C  Humidity:", humidity, "%")

        # ✅ Polling method to check button press (inefficient)
        if button.value() == 0:  # Button pressed (LOW)
            time.sleep(0.2)  # Simple debounce delay
            oled_state = not oled_state  # Toggle OLED state
            
            if oled_state:
                oled.poweron()
            else:
                oled.poweroff()
                
            while button.value() == 0:  # Wait for button release
                time.sleep(0.1)

        # ✅ Display updated values if OLED is ON
        if oled_state:
            oled.fill(0)
            oled.text("Temp: {} C".format(temp), 0, 0)
            oled.text("Humidity: {}%".format(humidity), 0, 16)
            oled.show()

    except Exception as e:
        print("Error reading DHT22 sensor:", e)
    
    time.sleep(1)  # Update every 1 second
