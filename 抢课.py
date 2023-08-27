import requests
import threading
import time
import urllib3
import requests
from requests.adapters import HTTPAdapter
import random
from bs4 import BeautifulSoup
from requests.packages.urllib3.util import Retry
urllib3.disable_warnings()
 
# 获取cookie

r = random.uniform(0,0.5)

def login(cookie):
    #login = 'https://10.1.20.5/jsxsd/xsxk/xsxk_index?jx0502zbid=FD9B7A571D8B489691A5AEE0F617CED4'
    login = 'https://jwxt.sztu.edu.cn/jsxsd/xsxk/xsxk_index?jx0502zbid=8128578A40424F1C82F584B6007DD8D9'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Referer': 'https://jwxt.sztu.edu.cn/jsxsd/xsxk/xklc_view?jx0502zbid=DF9C96D52DD54869AB0DBB91F41B5E75',
        'cookie':cookie
    }
    logined0 = requests.session()
    logined0.mount('https://', HTTPAdapter(max_retries=Retry(total=1000)))
    #while True:
    logined1 = logined0.get(login, verify=False, headers=header, timeout=0.5)
    # 打印返回的结果
    s=BeautifulSoup(logined1.text,'html.parser')
    print(logined1.text)
    if s.find(class_='current') == None:
        time.sleep(r)
        return ''
    if s.find(class_='current').text.replace('\n', '') == '选课学分情况':
        return 'ok'


    
def qiang(data, cookie):
    ###################################################
    print(data)
    url = f'https://jwxt.sztu.edu.cn/jsxsd/xsxkkc/bxqjhxkOper?kcid=186F617C5DC54402A52B70BB0A289992&cfbs=null&jx0404id={data}&xkzy=&trjf='
    #cookie = 'JSESSIONID=C34D8B379EA6075BC403722C7FF132C5'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Referer': 'https://jwxt.sztu.edu.cn/jsxsd/xsxkkc/comeInBxqjhxk',
        'cookie':cookie
    }
    mes0 = requests.session()
    mes0.mount('https://', HTTPAdapter(max_retries=Retry(total=1000)))
    # 一直抢！
    while True:
        try:
            time.sleep(round(r, 2))
            start = time.time()
            mes = mes0.get(url, verify=False, headers=header, timeout=0.5)
            end = time.time()
            # 打印返回的结果
            print(time.asctime( time.localtime(time.time()) ), str(mes.text))
        except:
            pass

def qiang1(cookie):
    ###################################################
    
    url = f'https://jwxt.sztu.edu.cn/jsxsd/xsxkkc/knjxkOper?kcid=D1DF30AB37E24A37A600E5F98BFD59D5&cfbs=null&jx0404id=202220231831&xkzy=&trjf='
    #cookie = 'JSESSIONID=C34D8B379EA6075BC403722C7FF132C5'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Referer': 'https://jwxt.sztu.edu.cn/jsxsd/xsxkkc/comeInBxqjhxk',
        'cookie':cookie
    }
    mes0 = requests.session()
    mes0.mount('https://', HTTPAdapter(max_retries=Retry(total=1000)))
    # 一直抢！
    while True:
        try:
            time.sleep(round(r, 2))
            start = time.time()
            mes = mes0.get(url, verify=False, headers=header, timeout=0.5)
            end = time.time()
            # 打印返回的结果
            print(time.asctime( time.localtime(time.time()) ), str(mes.text))
        except:
            pass


data = ['202220231630',  '202220231630', '202220231634'] #, '202220231636' '202220231625',

thread_list = []

def main(): 
    cookie = 'JSESSIONID=342965859D6B8D1A7911BE39BCDE92A1; SERVERID=124; JSESSIONID=C80BA3F93AF15C64A3D304B005C1010E'
    while(1):
        if login(cookie) == 'ok':
            break

    for i in data:
        thread_list.append(threading.Thread(target=qiang, args=(i,cookie,)))

    for i in thread_list:
        i.start()
        time.sleep(round(r, 2))

    



main()