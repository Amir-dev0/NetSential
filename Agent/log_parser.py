# This module must Read Linux logs, detect important security events, extract useful information, and send it for analysis/alerts

# importing the required modules
import subprocess
class LogParse():
    
    # This function receives and shows the logs momentarily
    @staticmethod
    def realtime_log():
        process = subprocess.Popen(
            ["journalctl", "-f"],
            stdout=subprocess.PIPE,
            text=True
        )

        for line in process.stdout:
            yield line.strip()

    # This function shows error logs
    @staticmethod
    def error_logs():
        try:
            process = subprocess.run(
                ["journalctl", "-p", "err"],
                capture_output=True,
                text=True
            )
            if process.returncode != 0:
                return f"Error: {process.stderr}"

            return process.stdout
        except FileNotFoundError:
            return "journalctl not found -- is this a systemd system ? "

    # This function shows the logs from the time you give it until now
    @staticmethod
    def logs_from(time_input: str):
        process = subprocess.run(
            ["journalctl", "--since", f"{time_input} ago"],
            capture_output=True,
            text=True      
        )
        return process.stdout

    # This function shows the errors in real time
    @staticmethod
    def live_errors():
        process = subprocess.Popen(
            ["journalctl", "-f", "-p", "err"],
            stdout=subprocess.PIPE,
            text=True
            )

        for line in process.stdout:
            yield line.strip()

    # This function shows boot errors
    @staticmethod
    def boot_errors():
        process = subprocess.run(
            ["journalctl", "-b", "-p", "err"],
            capture_output=True,
            text=True
        )

        return process.stdout