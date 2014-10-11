# -*- coding: utf-8 -*-

import commands
import sys

opcion = sys.argv[1]

ips = commands.getoutput('cat /var/lib/dhcp/dhcpd.leases|grep ^lease|cut -d " " -f 2').split('\n')

if opcion == '-l':
        print ips

elif opcion in ips:
        print 'La ip está concedida'
else:
        print 'No se encuentra'



