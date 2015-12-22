'''
Update android hosts

https://raw.githubusercontent.com/racaljk/hosts/master/hosts
'''

import requests
import os

hosts_url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
resp = requests.get(url=hosts_url)

with open('/storage/sdcard0/com.hipipal.qpyplus/scripts3/hosts', 'wb') as f:
    f.write(resp.content)

os.system('su -c "mount -o remount,rw /system"')

os.system('su -c "mv -f /storage/sdcard0/com.hipipal.qpyplus/'
          'scripts3/hosts /system/etc/hosts"')
