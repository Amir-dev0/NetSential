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

        return {
            "target": self.target,
            "port": port,
            "status": state
        }

    def scan_range(self, begin, end):

        results = []

        for port in range(begin, end + 1):

            res = self.scanner.scan(
                self.target,
                str(port)
            )

            state = res['scan'][self.target]['tcp'][port]['state']

            results.append({
                "target": self.target,
                "port": port,
                "status": state
            })

        return results