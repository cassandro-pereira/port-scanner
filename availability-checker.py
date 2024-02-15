#Python tool to verify Network ports' availability
import nmap
#Menu for options
print("Please type the IP address or domain for network port availability verification: ", end="")
#Getting Ip or domain from prompt
domain = input()
print("Please  type the port range to scan ie. 22-443: ", end="")
#Getting Ip range from prompt
range = input()
nm = nmap.PortScanner()
nm.scan(domain, range)
nm.command_line()
nm.scaninfo()
for host in nm.all_hosts():
     print('----------------------------------------------------')
     print('Host : %s (%s)' % (host, nm[host].hostname()))
     print('State : %s' % nm[host].state())
     for proto in nm[host].all_protocols():
         print('----------')
         print('Protocol : %s' % proto)

         lport = nm[host][proto].keys()
         for port in lport:
             print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
