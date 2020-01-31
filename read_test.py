from i2c import ArduinoI2C

if __name__ == "__main__":
    arduino = ArduinoI2C(1, 0x08)
    registers = arduino.read_bytes(0, 4)
    
    print(registers)
