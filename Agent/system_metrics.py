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
        percent_disk_used = str(self.disk_usage[3]) + "%"
        return percent_disk_used
#receive temperature
class temperature():
    def __init__(self):
        self.temperature = psutil.sensors_temperatures()
        
    def cpu_temperature(self):
        if not self.temperature or 'acpitz' not in self.temperature:
            return None
        cpu_temperature = self.temperature['acpitz'][0].current
        return cpu_temperature
    
#receive battery information
class battery():
    def __init__(self):
        self.battery = psutil.sensors_battery()

    def percent_battery(self):
        percent_battery = self.battery.percent
        return percent_battery
    
    def collect_system_metrics():

        cpu_obj = cpu()
        ram_obj = ram()
        disk_obj = disk()
        temp_obj = temperature()
        battery_obj = battery()

        metrics = {

            "cpu_cores": cpu_obj.number_of_core(),
            "cpu_percent": cpu.cpu_percent(),

            "total_ram": ram_obj.total_ram(),
            "used_ram": ram_obj.used_ram(),
            "free_ram": ram_obj.free_ram(),
            "ram_percent": ram_obj.percent_ram_used(),

            "total_disk": disk_obj.total_disk(),
            "used_disk": disk_obj.used_disk(),
            "free_disk": disk_obj.free_disk(),
            "disk_percent": disk_obj.percent_disk_used(),

            "cpu_temperature": temp_obj.cpu_temperature(),

            "battery_percent": battery_obj.percent_battery()
        }

        return metrics
    
import psutil


class SystemMetrics:

    def __init__(self):
        self.ram = psutil.virtual_memory()
        self.swap = psutil.swap_memory()
        self.disk = psutil.disk_usage('/home')
        self.temp = psutil.sensors_temperatures()
        self.battery = psutil.sensors_battery()

    def collect_metrics(self):

        cpu_temperature = None

        if self.temp and 'acpitz' in self.temp:
            cpu_temperature = self.temp['acpitz'][0].current

        metrics = {
            "cpu_cores": psutil.cpu_count(),
            "cpu_percent": psutil.cpu_percent(),

            "total_ram": round(self.ram.total / 10**9, 2),
            "used_ram": round(self.ram.used / 10**9, 2),
            "free_ram": round(self.ram.available / 10**9, 2),
            "ram_percent": self.ram.percent,

            "total_disk": round(self.disk.total / 10**9, 2),
            "used_disk": round(self.disk.used / 10**9, 2),
            "free_disk": round(self.disk.free / 10**9, 2),
            "disk_percent": self.disk.percent,

            "cpu_temperature": cpu_temperature,

            "battery_percent":
                self.battery.percent
                if self.battery else None
        }

        return metrics    