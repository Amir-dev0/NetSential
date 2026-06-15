# this module must scan server's port

# importing the required modules
import socket
class PortScanner:

    def __init__(self, target):
        self.target = target

    def scan_single_port(self, port):

        sock = socket.socket()
        sock.settimeout(1)

        try:
            sock.connect((self.target, port))
        except OSError:
            status = "closed"
        else:
            status = "open"
        finally:
            sock.close()

        return {
            "target": self.target,
            "port": port,
            "status": status
        }

    def scan_range(self, begin, end):

        results = []

        for port in range(begin, end + 1):

            result = self.scan_single_port(port)

            results.append(result)

        return results