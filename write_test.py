
from i2c import ArduinoI2C

if __name__ == "__main__":
    i2c = ArduinoI2C(1, 0x08)
    i2c.write_bytes(0, [0, 1, 2, 3])
