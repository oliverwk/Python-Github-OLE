import os
os.system('clear')
from iptcinfo3 import IPTCInfo
info = IPTCInfo('/Users/MWK/Desktop/Tatina_.jpg', force=True)
print(info['keywords'])
info['keywords'] = ['instagram']
info.save()
