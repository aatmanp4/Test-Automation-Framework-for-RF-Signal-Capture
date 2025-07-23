import serial

def capture_uart(port='/dev/ttyUSB0', baudrate=115200, threshold=0.5, timeout=10):
    ser = serial.Serial(port, baudrate, timeout=1)
    buffer = []
    print("[INFO] Waiting for signal threshold...")

    while True:
        line = ser.readline().decode(errors='ignore').strip()
        if not line:
            continue
        try:
            value = float(line)
            if value > threshold:
                buffer.append(value)
                break
        except ValueError:
            continue

    print("[INFO] Threshold reached, capturing signal...")
    for _ in range(2048):
        try:
            value = float(ser.readline().decode(errors='ignore').strip())
            buffer.append(value)
        except:
            continue
    ser.close()
    return buffer
