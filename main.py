import serial
import time

ser = serial.Serial(
    port='COM13',           
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

def send_cmd(cmd, expect_response=True):
    ser.write((cmd + '\n').encode())
    if expect_response:
        time.sleep(0.1)
        return ser.readline().decode().strip()
    return None

try:
    idn = send_cmd("*IDN?")
    print(f"Identification: {idn}")

    send_cmd("SYST:REM", expect_response=False)
    send_cmd("SOUR:VOLT 13", expect_response=False)
    send_cmd("SOUR:CURR 10", expect_response=False)
    send_cmd("OUTP ON", expect_response=False)
    time.sleep(1)
  
    voltage = send_cmd("MEAS:VOLT?")
    current = send_cmd("MEAS:CURR?")
    power   = send_cmd("MEAS:POW?")
    print(f"Voltage mesure: {voltage} V")
    print(f"Current mesure: {current} A")
    print(f"Power mesure: {power} W")
    time.sleep(1)

    send_cmd("OUTP OFF", expect_response=False)

except Exception as e:
    print(f"Error: {e}")
finally:
    ser.close()
