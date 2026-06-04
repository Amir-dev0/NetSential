# This module must Read Linux logs, detect important security events, extract useful information, and send it for analysis/alerts

# importing the required modules
import subprocess

def read_journal_logs(lines=50, unit=None, priority=None):
    cmd = ["journalctl", "--no-pager", "-n", str(lines), "--output=short-precise"]
    
    if unit:
        cmd += ["-u", unit]
    if priority:
        cmd += ["-p", priority]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

print(read_journal_logs(lines=20))
print(read_journal_logs(unit="sshd.service", lines=10))  
print(read_journal_logs(priority="err"))