# this module must receive server information including CPU, GPU, RAM, DISK

# importing the required modules
import psutil

#receive CPU information
number_of_cores = psutil.cpu_count()
cpu_percent = psutil.cpu_percent()


#receive RAM information
all_ram = psutil.virtual_memory()
total_ram = str(int(all_ram[0] / 10**9)) + 'Gb'
used_ram = str(int(all_ram[3] / 10**9)) + 'Gb'
free_ram = str(int(all_ram[4] / 10**9)) + 'Gb'
percent_ram_used = str(all_ram[2]) + '%'

all_swap = psutil.swap_memory()
total_swap = str(int(all_swap[0] / 10**9)) + 'Gb'
percent_swap_used = str(all_swap[3]) + '%'


#receive disk information
disk_usage = psutil.disk_usage('/home')
total_disk = str(int(disk_usage[0] / 10**9)) + 'Gb'
used_disk = str(int(disk_usage[1] / 10**9)) + 'Gb'
free_disk = str(int(disk_usage[2] / 10**9)) + 'Gb'
percent_disk_used = str(int(disk_usage[3] / 10**9)) + 'Gb'

#receive temperature
temperature = psutil.sensors_temperatures()
cpu_temperature = temperature['acpitz'][0].current

#receive battery information
battery = psutil.sensors_battery()
percent_battery = battery.percent

print(percent_battery)