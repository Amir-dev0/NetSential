# this module must receive server information including CPU, GPU, RAM, DISK

# importing the required modules
import psutil

#receive CPU information
class cpu():
    def __init__(self):
        pass
    
    @staticmethod
    def number_of_core():
        number_of_cores = psutil.cpu_count()
        return number_of_cores
    
    def cpu_percent():
        cpu_percent = psutil.cpu_percent()
        return cpu_percent

#receive RAM information
class ram():
    def __init__(self):
        self.all_ram = psutil.virtual_memory()
        self.all_swap = psutil.swap_memory()

    def total_ram(self):
        total_ram = str(int(self.all_ram[0] / 10**9)) + 'Gb'
        return total_ram
    
    def used_ram(self):
        used_ram = str(int(self.all_ram[3] / 10**9)) + 'Gb'
        return used_ram

    def free_ram(self):
        free_ram = str(int(self.all_ram[4] / 10**9)) + 'Gb'
        return free_ram
    
    def percent_ram_used(self):
        percent_ram_used = str(self.all_ram[2]) + '%'
        return percent_ram_used

    def total_swap(self):
        total_swap = str(int(self.all_swap[0] / 10**9)) + 'Gb'
        return total_swap
    
    def percent_swap_used(self):
        percent_swap_used = str(self.all_swap[3]) + '%'
        return percent_swap_used

#receive disk information
class disk():
    def __init__(self):
        self.disk_usage = psutil.disk_usage('/home')

    def total_disk(self):
        total_disk = str(int(self.disk_usage[0] / 10**9)) + 'Gb'
        return total_disk
    
    def used_disk(self):
        used_disk = str(int(self.disk_usage[1] / 10**9)) + 'Gb'
        return used_disk
    
    def free_disk(self):
        free_disk = str(int(self.disk_usage[2] / 10**9)) + 'Gb'
        return free_disk

    def percent_disk_used(self):
        percent_disk_used = str(int(self.disk_usage[3] / 10**9)) + 'Gb'
        return percent_disk_used
#receive temperature
class temperature():
    def __init__(self):
        self.temperature = psutil.sensors_temperatures()
        
    def cpu_temperature(self):
        cpu_temperature = self.temperature['acpitz'][0].current
        return cpu_temperature
    
#receive battery information
class battery():
    def __init__(self):
        self.battery = psutil.sensors_battery()

    def percent_battery(self):
        percent_battery = self.battery.percent
        return percent_battery
disk_usage = psutil.disk_usage('/home')
print(disk_usage)
print(str(disk_usage[3]) + "%")    