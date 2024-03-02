import smbus2
import time

# Define the I2C address of your CO2 sensor
SENSOR_ADDR = 0x68  # Change this to match your sensor's address

# Create an smbus object
bus = smbus2.SMBus(1)  # Use 1 for Raspberry Pi 3 or earlier, use 0 for Raspberry Pi 4

def read_co2():
    # Read 2 bytes from the CO2 sensor
    data = bus.read_i2c_block_data(SENSOR_ADDR, 0x86, 2)  # 0x86 is the command to request CO2 data
    # Convert the bytes to CO2 level (assuming big-endian)
    co2_level = (data[0] << 8) | data[1]
    return co2_level

try:
    while True:
        co2_level = read_co2()
        print("CO2 Level:", co2_level, "ppm")
        time.sleep(1)  # Read CO2 level every second

except KeyboardInterrupt:
    print("Exiting")

