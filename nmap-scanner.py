import nmap
import sys
scanner = nmap.PortScanner()
host = sys.argv[1]
port = sys.argv[3] if sys.argv.__len__() > 3 else '1-1024'
arg = sys.argv[5] if sys.argv.__len__() > 5 else '-sV'

print('----------------------------')
print('  Scanning {}'.format(host))
print('----------------------------')
scanner.scan(host, port, arg)
lp = scanner[host]['tcp'].keys()

print('PORT\tSTATE')
for port in lp:
    print('{}\t{}'.format(port, scanner[host]['tcp'][port]['state']))
