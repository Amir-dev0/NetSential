# This module must Read Linux logs, detect important security events, extract useful information, and send it for analysis/alerts

# importing the required modules
import subprocess
class LogParse():
    def __init__(self):
        pass
    
    # This function receives and shows the logs momentarily
    def realtime_log():
        process = subprocess.Popen(
            ["journalctl", "-f"],
            stdout=subprocess.PIPE,
            text=True
        )

        for line in process.stdout:
            print(line.strip())

    # This function shows error logs
    def error_logs():
        process = subprocess.run(
            ["journalctl", "-p", "err"],
            capture_output=True,
            text=True
        )

        return process.stdout

    # This function shows the logs from the time you give it until now
    def time_log():
        time_input = input("")
        process = subprocess.run(
            ["journalctl", "--since", f"{time_input} ago"],
            capture_output=True,
            text=True      
        )
        return process.stdout

    # This function shows the errors in real time
    def live_errors():
        process = subprocess.Popen(
            ["journalctl", "-f", "-p", "err"],
            stdout=subprocess.PIPE,
            text=True
            )

        for line in process.stdout:
            print("ERROR >", line.strip())

    # This function shows boot errors
    def boot_errors():
        process = subprocess.run(
            ["journalctl", "-b", "-p", "err"],
            capture_output=True,
            text=True
        )

        return process.stdout