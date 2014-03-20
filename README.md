#FreenasScripts

## VolumeUnlock.py

#####FEATURES:
- Start FreeNAS via wake on lan
- Unlock an encrypted volume via API
- Restart CIFS service via API 
(you can add/change to other services like nfs,afp,..)

#####PYTHON REQUIREMENTS:
- pip install wakeonlan
- pip install requests
- This script has been tested with python 3.4.0

#####CONFIGURATION:
- Edit all fields with "<>" according to your data

## TransmissionUnrar.sh

#####FEATURES:
- Transmission unrars into same folder after download is completed

#####REQUIREMENTS: 
- This script requires unrar to be installed within the
FreeNAS Jail of Transmission. A tutorial on how to do this can be
found under: http://www.bytegeist.net/?p=3

#####INSTALLATION: 
- Edit the settings.json of Transmission according to:
"script-torrent-done-enabled": true, 
"script-torrent-done-filename": "/path/to/TransmissionUnrar.sh",

deinidol[at]gmail[dotcom]
