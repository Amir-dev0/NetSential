from Agent.port_scanner import PortScanner
from Backend.database import Database


db = Database()
db.create_table()

target = input("Enter target: ")

scanner = PortScanner(target)

mode = int(input(
    "1) single scan\n"
    "2) range scan\n"
    "-> "
))

if mode == 1:

    port = int(input("Port: "))

    result = scanner.scan_single_port(port)

    db.save_scan(
        result["target"],
        result["port"],
        result["status"]
    )

    print(result)

elif mode == 2:

    begin = int(input("Begin port: "))
    end = int(input("End port: "))

    results = scanner.scan_range(begin, end)

    for result in results:

        db.save_scan(
            result["target"],
            result["port"],
            result["status"]
        )

    print(results)

db.close()