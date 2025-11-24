import serial
import serial.tools.list_ports

def find_arduino_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # Print detected ports and descriptions
        print(f"Checking port: {port.device}, desc: {port.description}")
        # Look for 'Arduino' or 'CH340' or similar keywords in description
        if 'Arduino' in port.description or 'CH340' in port.description:
            return port.device
    return None

arduino_port = find_arduino_port()

if arduino_port:
    print(f"Arduino found on port: {arduino_port}")
    try:
        ser = serial.Serial(arduino_port, 9600, timeout=1)
        print("Serial connection established.")
        # You can now read/write to the port
        # Example:
        # ser.write(b'Hello\n')
        # print(ser.readline().decode())
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
else:
    print("Arduino not found. Please check the connection.")
