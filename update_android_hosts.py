'''
Update android hosts

https://raw.githubusercontent.com/racaljk/hosts/master/hosts
'''

import requests
import os

hosts_url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
resp = requests.get(url=hosts_url)

with open('/Users/qiuzhidong/Documents/Scripts/hosts', 'wb') as f:
    f.write(resp.content)

os.system('adb root')
os.system('adb remount')
os.system('adb push /Users/qiuzhidong/Documents/Scripts/hosts '
          '/system/etc/hosts')
os.system('rm /Users/qiuzhidong/Documents/Scripts/hosts')
