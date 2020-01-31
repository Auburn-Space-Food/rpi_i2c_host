from smbus2 import SMBus, i2c_msg

I2C_RET_OKAY = 0x00
I2C_RET_OUT_OF_BOUNDS = 0x01
I2C_RET_TOO_LARGE = 0x02
I2C_RET_TOO_SMALL = 0x03
I2C_RET_UNSUPPORTED = 0x04
I2C_RET_MALFORMED = 0x05
I2C_RET_NONE_PENDING = 0x06

class ArduinoI2C:
    def __init__(self, bus, i2c_addr):
        self.bus = bus
        self.addr = i2c_addr

    def read_byte(self, register):
        self.read_bytes(register, 1)

    def read_bytes(self, register, count):
        if not isinstance(register, int):
            raise TypeError("ArduinoI2C.read_bytes: register is not an integer")
        
        if not isinstance(register, int):
            raise TypeError("ArduinoI2C.read_bytes: count is not an integer")

        write = i2c_msg.write(self.addr, [register, count])
        read = i2c_msg.read(self.addr, count)
        with SMBus(self.bus) as i2c:
            i2c.i2c_rdwr(write, read)

        return list(read) 

    def write_byte(self, register, data):
        if not isinstance(data, int):
            raise TypeError("ArduinoI2C.write_byte: data is not an integer")

        self.write_bytes(register, [data])

    def write_bytes(self, register, data):
        if not isinstance(register, int):
            raise TypeError("ArduinoI2C.write_bytes: register is not an integer")

        if not isinstance(data, list):
            raise TypeError("ArduinoI2C.write_bytes: data is not a list of integers")

        write_command = i2c_msg.write(self.addr, [register])
        write_data = i2c_msg.write(self.addr, data)
        with SMBus(self.bus) as i2c:
            i2c.i2c_rdwr(write_command, write_data)
