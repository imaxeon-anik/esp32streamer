import network
import machine
import usocket as socket
import utime

# Wi-Fi credentials
ssid = "ghostchilli"
password = "coriander23"

# Set up Wi-Fi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    pass

# Print the IP address after connecting to the internet
ip_address = wlan.ifconfig()[0]
print("Connected to WiFi. IP address:", ip_address)

# Set up a socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen(1)

print("Waiting for connection...")

# Accept a connection from a remote client
conn, addr = server.accept()
print("Connected by", addr)

# Main loop
while True:
    try:
        # Receive data from the remote client
        data_from_remote = conn.recv(64)  # adjust buffer size as needed

        # Process the received data (you can modify this part)
        if data_from_remote:
            # Do something with the data, e.g., print it
            print("Received from remote device:", data_from_remote)

            # Assuming you have some response or command output
            response_data = "Response from ESP32: OK"

            # Send the response back to the remote device
            conn.sendall(response_data)
    except Exception as e:
        print("Error:", e)

    # Adjust the interval based on your requirements
    utime.sleep(1)

