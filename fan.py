import time
import subprocess
import os
import smbus

bus = smbus.SMBus(1)

addr = 0x0d
fan_reg = 0x08
temp = 0
sleep_time = 1
fan_speed = 0

while True:
    cmd = os.popen('vcgencmd measure_temp').readline()
    CPU_TEMP = cmd.replace("temp=","").replace("'C\n","")
    temp = float(CPU_TEMP)
    print("CPU Temperature: ", CPU_TEMP)

    print("Adjusting Fan Speed...")
    try:

        if temp <= 45:
            bus.write_byte_data(addr, fan_reg, 0x00)
            sleep_time = 5
            fan_speed = 0
        elif temp <= 47:
            bus.write_byte_data(addr, fan_reg, 0x04)
            sleep_time = 20
            fan_speed = 4
        elif temp <= 49:
            bus.write_byte_data(addr, fan_reg, 0x06)
            sleep_time = 30
            fan_speed = 6
        elif temp <= 51:
            bus.write_byte_data(addr, fan_reg, 0x08)
            sleep_time = 20
            fan_speed = 8
        elif temp <= 53:
            bus.write_byte_data(addr, fan_reg, 0x09)
            sleep_time = 20
            fan_speed = 9
        else:
            bus.write_byte_data(addr, fan_reg, 0x06)
            sleep_time = 60
            fan_speed = 6

        print("Fan run for ", sleep_time, " seconds at Speed: ", fan_speed)
        time.sleep(sleep_time)
    except Exception as ex:
        print("Adjusting Fan Speed Error:", ex)

