# this module must scan server's port

# importing the required modules
import nmap
class PortScanner:

    def __init__(self, target):
        self.target = target
        self.scanner = nmap.PortScanner()

    def scan_single_port(self, port):
        res = self.scanner.scan(
            self.target,
            str(port)
        )

        state = res['scan'][self.target]['tcp'][port]['state']

        if state == 'open':
            print(f"port {port} is open")
        else:
            print(f"port {port} is closed")

        return state

    def scan_range(self, begin, end):
        
        is_open = False
        open_ports = []

        
        for port in range(begin, end + 1):

            res = self.scanner.scan(
                self.target,
                str(port)
            )

            state = res['scan'][self.target]['tcp'][port]['state']

            if state == "open":
                open_ports.append(port)
                is_open = True

        if not is_open:
            print("all ports are closed")
        else:
            print(f"{len(open_ports)} port(s) are open: {open_ports}")  
  
target = input("Enter your target: ")
scanner = PortScanner(target)
model = int(input("1) single scan port \n 2) range scan port \n ->  "))

if model == 1:
    port = int(input("Enter the port you want to scan: "))
    scanner.scan_single_port(port)
    
elif model == 2:
    begin = int(input("Enter the begining port: "))
    end   = int(input("Enter the ending port: "))

    scanner.scan_range(begin, end)    