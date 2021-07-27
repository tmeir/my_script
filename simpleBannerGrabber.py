import socket
try:
    ip_add = input("IP Address: ")
    port_num = int(input("Port Number (Numbers only): "))

    s = socket.socket()
    s.connect((ip_add,port_num))
    print("Connection establish")
    recData = s.recv(2048).decode()
    print(f"Server:{recData}")

except Exception as e:
    print(e)