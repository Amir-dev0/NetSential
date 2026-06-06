# This module must Read Linux logs, detect important security events, extract useful information, and send it for analysis/alerts

# importing the required modules
import subprocess

def realtime_log():
    process = subprocess.Popen(
        ["journalctl", "-f"],
        stdout=subprocess.PIPE,
        text=True
    )

    for line in process.stdout:
        print(line.strip())

def error_log():
    process = subprocess.run(
        ["journallctl", ]


    )

def time_log():
    time_input = input("")
    process = subprocess.run(
        ["journalctl", "--since", f"{time_input} ago"],
        capture_output=True,
        text=True      
    )
    return process.stdout

def live_errors():
    process = subprocess.Popen(
        ["journalctl", "-f", "-p", "err"],
        stdout=subprocess.PIPE,
        text=True
    )

    for line in process.stdout:
        print("ERROR >", line.strip())

live_errors()        

