import network
import time

ssid = "Faisal"
password = "11111111"

print("Connecting to WiFi", end="")

sta = network.WLAN(network.STA_IF)
sta.active(True)
time.sleep(1)  # Delay after activating

sta.connect(ssid, password)

# Print initial status
print("\nInitial WiFi status:", sta.status())

# Wait for connection
for _ in range(20):  # Increased timeout
    if sta.isconnected():
        break
    print(".", end="")  # Show progress
    time.sleep(1)

# Final connection check
if sta.isconnected():
    print("\nConnected to WiFi!")
    print("IP Address:", sta.ifconfig()[0])
else:
    print("\nFailed to connect. WiFi status:", sta.status())
