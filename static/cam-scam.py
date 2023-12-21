from scapy.all import ARP, Ether, srp
import socket

def scan_ip_range(ip_range):
    """
    Scan for active hosts in the network
    """
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    active_hosts = []
    for sent, received in answered_list:
        active_hosts.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return active_hosts

def check_camera_ports(ip, ports=[80, 8080, 554]):
    """
    Check for open ports commonly used by cameras
    """
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    return open_ports

ip_range = '<teu ip>/24'
hosts = scan_ip_range(ip_range)

for host in hosts:
    open_ports = check_camera_ports(host['ip'])
    if open_ports:
        print(f"Host {host['ip']} has open ports: {open_ports}")
