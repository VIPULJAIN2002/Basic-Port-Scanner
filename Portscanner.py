import socket

def scan (target, ports):
    print('\n' + ' Starting Scan for ' + str(target))
    for port in range (1,ports+1) :
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Open " + str(port))
        sock.close()
    except:
        pass


targets = input("[*] Enter Targets To Scan(Split them by ,): ")
ports = int(input("[*] Enter How Many Ports To Scan: "))
if ',' in targets :
    print("[*] Scanning Multiple Targets ")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
        scan(targets,ports)




