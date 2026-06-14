import getpass
from Backend.database import Database
from Agent.port_scanner import PortScanner
from Agent.system_metrics import SystemMetrics
from Agent.login import LoginAgent

db = Database()
db.create_table()
db.create_users_table()

if LoginAgent.authenticate(db):
    
    print("Welcome to NetSential")
    
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


    db.create_metric_table()

    metrics_agent = SystemMetrics()

    metrics = metrics_agent.collect_metrics()

    db.save_system_metrics(metrics)
    db.close()