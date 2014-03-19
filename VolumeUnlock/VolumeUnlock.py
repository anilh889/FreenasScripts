#!/usr/bin/env python

######################################################################
# VolumeUnlock.py
######################################################################
# FEATURES:
# - Start FreeNAS via wake on lan
# - Unlock an encrypted volume via API
# - Restart CIFS service via API 
# (you can add/change to other services like nfs,afp,..)
#
# PYTHON REQUIREMENTS:
# pip install wakeonlan
# pip install requests
# This script has been tested with python 3.4.0
#
# CONFIGURATION:
# Edit all <fields> according to your data
#
######################################################################
# deinidol@gmail.com
######################################################################

import json
import requests
import time
from wakeonlan import wol

# wake up on lan by sending a magic packet to the specified MAC address
wol.send_magic_packet('<00:..MACaddress>')

# lower this according to your boot time (seconds)
time.sleep(200)

# takes user input you can comment this out and hardcode the values with 'word'
rootpw = input("root pass: ")
decryptkey = input("passphrase to unlock volume: ")

# unlocks the drives
r = requests.post(
        'http://<yourNAS>/api/v1.0/storage/volume/<volumeName>/unlock/',
        auth=('root', rootpw),
        headers={'Content-Type': 'application/json'},
        verify=False,
        data=json.dumps({'passphrase': decryptkey}),
)
print(r.text)

time.sleep(2)

# disables cifs
r = requests.put(
		'http://<yournas>/api/v1.0/services/services/cifs/',
		auth=('root', rootpw),
		headers={'Content-Type': 'application/json'},
		verify=False,
		data=json.dumps({'srv_enable': False}),
)
print(r.text)

time.sleep(2)

# enables cifs
r = requests.put(
		'http://<yournas>/api/v1.0/services/services/cifs/',
		auth=('root', rootpw),
		headers={'Content-Type': 'application/json'},
		verify=False,
		data=json.dumps({'srv_enable': True}),
)
print(r.text)