'''
Update hosts

https://raw.githubusercontent.com/racaljk/hosts/master/hosts
'''

import requests

hosts_url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
resp = requests.get(url=hosts_url)

original = '''##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1       localhost
255.255.255.255 broadcasthost
::1             localhost
10.150.20.4     gitlab

'''

with open('/etc/hosts', 'wb') as f:
    f.write(original.encode())
    f.write(resp.content)
