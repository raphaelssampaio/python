import nmap
import sys
scanner = nmap.PortScanner()
host = sys.argv[1]
port = sys.argv[3] if sys.argv.__len__() > 3 else '1-1024'
arg = sys.argv[5] if sys.argv.__len__() > 5 else '-v -sV'

print('----------------------------')
print('  Scanning {}'.format(host))
print('----------------------------')

scan = scanner.scan(host, port, arg)

lp = scanner[host]['tcp'].keys()

print('PORT\tSTATE\tSERVICE')
for port in lp:
    state = scanner[host]['tcp'][port]['state']
    service1 = scanner[host]['tcp'][port]['product']
    service2 = scanner[host]['tcp'][port]['version']
    print('{}\t{}\t{} {} '.format(port, state, service1, service2))
