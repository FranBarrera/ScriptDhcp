# -*- coding: utf-8 -*-

import commands
import sys
import os
opcion = sys.argv[1]

ips = commands.getoutput('cat /var/lib/dhcp/dhcpd.leases|grep ^lease|cut -d " " -f 2').split('\n')
ips_res = commands.getoutput('cat /etc/dhcp/dhcpd.conf|grep -v "#" |grep fixed-address|cut -d " " -f 4')
ips_res = ips_res.replace(";","")

if opcion == '-l':
    os.system('clear')
    print 'Direcciones asignadas'
    print ips
    print 'direcciones reservadas'
    print ips_res
elif opcion in ips:
    hardware = commands.getoutput('cat /var/lib/dhcp/dhcpd.leases |grep -A6 "%s" |grep "hardware ethernet"|cut -d " "" -f 5' % sys.argv[1])
    hardware = hardware.replace(";","")
    print 'La ip está concedida'
    print hardware
else:
    print 'No se encuentra'
