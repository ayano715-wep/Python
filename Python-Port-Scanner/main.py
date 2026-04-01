import socket

def scan_ports(ip):
    open_ports = []
    for port in range(1, 10024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports
ip_user = str(input("Enter the ip for scan port : "))
target_ip = ip_user.replace(" ", "") 
open_ports = scan_ports(target_ip)
print(f"Open ports on {target_ip}: {open_ports}")
