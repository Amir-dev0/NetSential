# this module must scan server's port

# importing the required modules
import nmap

#recieve the begin and end port and IP target
begin = int(input("Enter the begining port: "))
end = int(input("Enter the ending port: "))
target = input("inter the ip target: ")

# instantiate a PortScanner object
scanner = nmap.PortScanner()

is_open = False
opens = []
count = 0
for i in range(begin, end+1):

    #scan teh target port
    res = scanner.scan(target,str(i))
    
    res = res['scan'][target]['tcp'][i]['state']
    
    if res == 'open':
        opens.append(i)
        is_open = True
        count += 1

if not is_open:
    print('all port is closed')      
if count > 0:
    print(f"{count} port is open and these is {opens}")