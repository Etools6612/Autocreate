import os
import random
import requests
import time
from concurrent.futures import ThreadPoolExecutor
import os
import random
import string
import uuid
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests
import json
import sys
import os
import platform
import re
import os
import uuid
import random
import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import string
import os
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
import sys
import os
import platform
import re
import re
import requests
import random
import string
import requests
import random
import concurrent.futures as thread
import os
import string
import requests
import random
import concurrent.futures as thread
import os
import string
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
import sys
import os
import platform
import re
import requests
import os
import random
import time
import random
import requests
from colorama import init, Fore, Style
import os
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
import sys
import os
import platform
import os
import requests
import uuid
import random
from requests import post as pt
from rich import print as rp
from rich.panel import Panel as pan
import os
import requests
import uuid
import random
from requests import post as pt
from rich import print as rp
from rich.panel import Panel as pan
import platform
import os
import random
import uuid
import os
import requests
import random
import string
import uuid
import random
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import json
import time
import uuid
import base64
import re
from concurrent.futures import ThreadPoolExecutor
import re
import requests
import random
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import os, sys, requests, threading
import sys
import requests
import threading
from time import sleep
from datetime import datetime
import faker
import hashlib
from faker import Faker
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from time import sleep,strftime
from requests import session
from bs4 import BeautifulSoup
import itertools
import threading
import time
import signal
import shutil
import getuseragent
from getuseragent import UserAgent
from rich.panel import Panel
luc    = "\033[1;32m"  # Bright Green
trang  = "\033[1;37m"  # Bright White
do     = "\033[1;31m"  # Bright Red
vang   = "\033[0;93m"  # Bright Yellow
hong   = "\033[1;35m"  # Bright Magenta (Pink)
xduong = "\033[1;34m"  # Bright Blue
xnhac  = "\033[1;36m"  # Bright Cyan
purple = "\033[1;35m"
blue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
white = "\033[1;37m"
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
gh ="\x1b[38;5;196m"
gh2 = "\x1b[38;5;197m"
gh3 = "\x1b[38;5;198m"
gh4 = "\x1b[38;5;199m"
gh5  = "\x1b[38;5;200m"
gh6 = "\x1b[38;5;201m"
rb = "\x1b[38;5;154m"
rb2 = "\x1b[38;5;155m"
rb3 = "\x1b[38;5;156m"
rb4 = "\x1b[38;5;157m"
rb5 = "\x1b[38;5;158m"
rb6 = "\x1b[38;5;159m"
C = "\x1b[38;5;51m"
C1 = "\x1b[38;5;206m"
C3 = "\x1b[38;5;251m"
C4 = "\x1b[38;5;205m"
C5 = "\x1b[38;5;206m"
C6 = "\x1b[38;5;207m"
Q = "\x1b[38;5;118m"
Q2 = "\x1b[38;5;119m"
Q3 = "\x1b[38;5;120m"
Q4 = "\x1b[38;5;121m"
Q5 = "\x1b[38;5;122m"
Q6 = "\x1b[38;5;123m"
Q7 = "\x1b[38;5;165m"
W= "\x1b[38;5;255m"
BG ="\x1b[47;100m"
BG1 ="\x1b[40;1;37m"
RW= "\x1b[0;95m"
Z1 ="\x1b[38;5;46m"
B = "\x1b[38;5;34m"
B2 = "\x1b[38;5;35m"
B3 = "\x1b[38;5;36m"
B4 = "\x1b[38;5;37m"
B5= "\x1b[38;5;38m"
AA = "\x1b[38;5;39m"
F = "\x1b[38;5;255m"
F1 = "\x1b[38;5;m"
F2 = "\x1b[38;5;27m"
F3 = "\x1b[38;5;196m"
F4 = "\x1b[38;5;228m"
F5  = "\x1b[38;5;205m"
F6 = "\x1b[38;5;30m"
DD = "\x1b[38;5;9m"
WW = "\x1b[42;255;20m"
WWS = "\x1b[41;255;20m"
YY = "\x1b[38;5;223m"
CQ = "\x1b[38;5;230m"



def clear_screen():
    if 'termux' in platform.system().lower():
        os.system('clear')
    elif platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
        

   

COLOR_DEFAULT = Style.RESET_ALL
COLOR_BLUE = Fore.BLUE
COLOR_MAGENTA = Fore.MAGENTA
COLOR_CYAN = Fore.CYAN
COLOR_GREEN = Fore.GREEN
COLOR_RED = Fore.RED
COLOR_YELLOW = Fore.YELLOW
ICON = '➤ '
ARRAY_ANIMATION = [f'{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON}{COLOR_MAGENTA}{ICON}{COLOR_BLUE}{ICON}  ', f'   {COLOR_MAGENTA}{ICON}{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON} ', f'    {COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_RED}{ICON}{COLOR_YELLOW}{ICON}{COLOR_MAGENTA}{ICON}']
end='\033[0m'
     
import sys
import time
import itertools
from colorama import Fore, Style, init

# I-enable ang kulay sa terminal
init(autoreset=True)

# Listahan ng kulay para sa animation
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

spinner = itertools.cycle(['|', '/', '-', '\\'])

def colorful_loading(duration=5):
    print(f"{Fore.WHITE}🔄 Loading Please Wait ...\n")
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        color = colors[i % len(colors)]
        sys.stdout.write(f"\r{color}Loading {next(spinner)}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print(f"\r{Fore.GREEN}✅ Loading complete!{Style.RESET_ALL}")

# Tawagin ang function
colorful_loading(2)  # 6 seconds loading


    
    
def get_combined_data(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'cache-control': "max-age=0",
        'dpr': "2",
        'viewport-width': "980",
        'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Linux\"",
        'sec-ch-ua-platform-version': "\"\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-full-version-list': "\"Google Chrome\";v=\"131.0.6778.104\", \"Chromium\";v=\"131.0.6778.104\", \"Not_A Brand\";v=\"24.0.0.0\"",
        'sec-ch-prefers-color-scheme': "light",
        'upgrade-insecure-requests': "1",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'accept-language': "en-US,en;q=0.9",
        'priority': "u=0, i",
        'Cookie': "sb=fuZTZ8Zyl9dXj5TFodlxDrGD; dpr=2; wd=980x1628; datr=fuZTZxL-gtbBjTkfeBq-VVDZ"
    }
    try:
        response = requests.get(url, headers=headers).text
        actrs_match = re.search(r'"actrs\\":\\"(\d+)\\"', response)
        actrs_number = actrs_match.group(1) if actrs_match else None
        post_id_match = response.split('"post_id":"')[1].split('"')[0] if '"post_id":"' in response else None
        if actrs_number and post_id_match:
            return f"{actrs_number}_{post_id_match}"
        elif not actrs_number:
            return "actrs number not found!"
        elif not post_id_match:
            return "post_id not found!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_combined_data(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'cache-control': "max-age=0",
        'dpr': "2",
        'viewport-width': "980",
        'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Linux\"",
        'sec-ch-ua-platform-version': "\"\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-full-version-list': "\"Google Chrome\";v=\"131.0.6778.104\", \"Chromium\";v=\"131.0.6778.104\", \"Not_A Brand\";v=\"24.0.0.0\"",
        'sec-ch-prefers-color-scheme': "light",
        'upgrade-insecure-requests': "1",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'accept-language': "en-US,en;q=0.9",
        'priority': "u=0, i",
        'Cookie': "sb=fuZTZ8Zyl9dXj5TFodlxDrGD; dpr=2; wd=980x1628; datr=fuZTZxL-gtbBjTkfeBq-VVDZ"
    }
    try:
        response = requests.get(url, headers=headers).text
        actrs_match = re.search(r'"actrs\\":\\"(\d+)\\"', response)
        actrs_number = actrs_match.group(1) if actrs_match else None
        post_id_match = response.split('"post_id":"')[1].split('"')[0] if '"post_id":"' in response else None
        if actrs_number and post_id_match:
            return f"{actrs_number}_{post_id_match}"
        elif not actrs_number:
            return "actrs number not found!"
        elif not post_id_match:
            return "post_id not found!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def extract_facebook_video_id(url):
    pattern = r'facebook\.com/(\d+)/videos/(\d+)/'
    match = re.search(pattern, url)
    if match:
        user_id, video_id = match.groups()
        return f"{user_id}_{video_id}"
    else:
        return None

def extract_ids(url):
    group_pattern = r'groups/(\d+)/permalink/(\d+)/'
    post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'
    group_match = re.search(group_pattern, url)
    post_match = re.search(post_pattern, url)
    photo_match = re.search(photo_pattern, url)
    if group_match:
        group_id, post_id = group_match.groups()
        return f"{group_id}_{post_id}"
    elif post_match:
        group_id, post_id = post_match.groups()
        return f"{group_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    else:
        return None 

list_id_name_page = []
count = 0
dem = 0
oks=[]
user_id=[]
import requests
import platform

#!/usr/bin/env python3
# boost_ui.py

import os
import socket
import platform
from datetime import datetime

# optional public IP
def get_ip():
    try:
        import requests
        ip = requests.get("https://api.ipify.org?format=text", timeout=3).text.strip()
        return ip
    except Exception:
        # fallback: local IP
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"

def get_device():
    sys = platform.system()
    node = platform.node()
    machine = platform.machine()
    if "ANDROID_ROOT" in os.environ:
        return f"Android (Termux) — {node} {machine}"
    return f"{sys} — {node} {machine}"

def get_time():
    return datetime.now().strftime("%H:%M:%S")

def get_date():
    return datetime.now().strftime("%B %d, %Y")  # October 28, 2025

def boost_header():
    os.system("clear")
    print("╔═══════════════════════════════════════╗")
    print("║             ＢＯＯＳＴ TOOL           ║")
    print("╚═══════════════════════════════════════╝")

    # info section below logo
    print(f"📡  IP Address : \033[92m{get_ip()}\033[0m")
    print(f"🕒  Time       : \033[93m{get_time()}\033[0m")
    print(f"📅  Date       : \033[95m{get_date()}\033[0m")
    print("─────────────────────────────────────────\n")
    
def ethan():
   	
    print(f"""
              {YY}  ██████╗  ██████╗  ██████╗ ███████╗████████╗
                ██╔══██╗██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝
                ██████╔╝██║   ██║██║   ██║███████╗   ██║   
                ██╔══██╗██║   ██║██║   ██║╚════██║   ██║   
                ██████╔╝╚██████╔╝╚██████╔╝███████║   ██║   
                ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝    """)
    print(f"╔═══════════════════════════════════════════════════════════════╗ ")
    print(f"║{YY} IP Address : {C} {get_ip()}  {white}                               ║  ")
    print(f"║{YY} Time       : {C} {get_time()}        {white}                                ║     ")
    print(f"║{YY} Date       : {C} {get_date()}{white}                                ║    ")
    print(f"║{YY} User info  : {C} KRISTEL MAE      {white}                               ║      ")
    print(f"║{YY} Uses       :  {C}Boosting         {white}                               ║     ")
    print(f"╚═══════════════════════════════════════════════════════════════╝")
    print(f"╔═══════════════════════════════════════════════════════════════╗ ")
    print(f"║{YY} Tools info    : {C} Premium  Paid {white}                               ║  ")
    print(f"║{YY} Network       : {C} Data or Wifi        {white}                         ║     ")
    print(f"║{YY} vpn           : {C} Warp 1.1.1.1 {white}                                ║    ")
    print(f"║{YY} Updated date  : {C} Jan 2026 {white}                                    ║      ")
    print(f"║{YY} Tools         :  {C}PAIDED         {white}                              ║     ")
    print(f"╚══════┳════════════════════════════════════════════════════════╝")
    print(f"       ┃ ")
    print(f"  ┏━━━━┸━━━━━━━━━━━━━━┓")
    print(f"  ┃ ACCOUNT OVERVIEWS ┃")
    print(f"  ┗━━━━━━━━━━━━━━━━━━━┛")
def load_proxies():
    proxy_url = ["https://raw.githubusercontent.com/ERRORDEATH-403/PROXY/main/http.txt","https://raw.githubusercontent.com/ERRORDEATH-403/PROXY/main/http_proxies.txt"]
    try:
        response = requests.get(proxy_url)
        if response.status_code == 200:
            return [proxy.strip() for proxy in response.text.splitlines()]
    except requests.exceptions.RequestException:
        pass
    return []

proxies_list = load_proxies()

def get_random_proxy():
    if proxies_list:
        return {"http": random.choice(proxies_list)}
    return None

proxies = get_random_proxy()

def W_ueragnt():
    chrome_version = random.randint(80, 99)
    webkit_version = random.randint(500, 599)
    safari_version = random.randint(400, 499)
    windows_version = random.randint(8, 10)
    is_win64 = random.choice([True,False])
    if is_win64:
        if not 'WOW64;':
            user_agent = f'''Mozilla/5.0 (Windows NT {windows_version}.{''}Win64; x64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'''
            return user_agent

def W_ueragent():
    chrome_versions = [(80, 3987, 163), (90, 4430, 212), (100, 4896, 127)]
    webkit_versions = [(537, 36), (537, 36), (537, 36)]
    safari_versions = [500, 600]
    windows_versions = [(10, 0), (10, 1), (11, 0)]
    chrome_version = random.choice(chrome_versions)
    webkit_version = random.choice(webkit_versions)
    safari_version = random.choice(safari_versions)
    windows_version = random.choice(windows_versions)
    is_win64 = random.choice([True, False])
    win64_str = 'Win64; x64' if is_win64 else 'WOW64'
    user_agent = (
        f'Mozilla/5.0 (Windows NT {windows_version[0]}.{windows_version[1]}; {win64_str}) '
        f'AppleWebKit/{webkit_version[0]}.{webkit_version[1]} (KHTML, like Gecko) '
        f'Chrome/{chrome_version[0]}.{chrome_version[1]}.{chrome_version[2]} Safari/{safari_version}'
    )
    return user_agent

def generate_user_agent():
    fbav = f"{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    device = random.choice(["HUAWEI MAR-LX1M", "Samsung SM-G960F", "OnePlus GM1913"])
    fbav_version = str(random.randint(49, 150))
    fbbv_version = str(random.randint(11111111, 77777777))
    carrier = random.choice(["Ooredoo TN", "Orange", "Vodafone", "T-Mobile"])
    ua_bgraph = f'[FBAN/FB4A;FBAV/{fbav_version}.0.0.{random.randrange(20, 49)}.{random.randint(11, 99)};FBBV/{fbbv_version};' \
                f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density=3.0,width=1080,height=2107}};FBLC/fr_FR;' \
                f'FBRV/{fbrv};FBCR/{carrier};FBMF/{device.split(" ")[0]};FBBD/{device.split(" ")[0]};' \
                f'FBPN/com.facebook.katana;FBDV/{device};FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
    return ua_bgraph

ua_bgraph = generate_user_agent()

fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'
fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
fbbv = str(random.randint(111111111, 999999999))
fbrv = '0'
random_seed = random.Random()
adid = ''.join(random_seed.choices(string.hexdigits, k=16))
ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:]'

def user_agint():
    fbcr_values = ["AT&T", "Orange France", "Telia Sweden","Vodafone Italy", "Sky Mobile","Proximus Belgium", "Movistar Spain", "Tele2 Netherlands", "Vodafone Spain", "Telekom Deutschland","Eir Ireland", "KPN Netherlands", "Three Ireland", "Telekom Austria", "Telia Sweden","Vodafone Italy", "Sky Mobile", "Proximus Belgium", "Movistar Spain", "Tele2 Netherlands","Vodafone Spain", "Telekom Deutschland", "Eir Ireland", "KPN Netherlands", "Three Ireland","Telekom Austria", "Telia Sweden", "Vodafone Italy", "Sky Mobile", "Proximus Belgium","Movistar Spain", "Tele2 Netherlands","Vodafone Spain", "Telekom Deutschland", "Eir Ireland","KPN Netherlands", "Three Ireland", "Telekom Austria", "China Mobile", "NTT Docomo", "KT Corporation", "Singtel","AIS Thailand", "Viettel", "Smart Communications", "PTCL Pakistan", "Grameenphone Bangladesh","Nepal Telecom", "MTN Nigeria", "T-Mobile USA", "Verizon Wireless", "Rogers Canada","O2 United Kingdom", "Telstra Australia", "TIM Brazil", "Vivo India", "Telenor Norway","Mobilink Pakistan", "Bell Canada", "Etisalat UAE", "Claro Mexico", "Orange Spain","Vodafone Portugal", "Telkomsel Indonesia","Beeline Russia", "MTS Russia", "Optus Australia","SK Telecom South Korea", "Entel Chile", "MTNL India", "Tigo Ghana", "Idea India","DTAC Thailand", "Zong Pakistan", "Orange Romania", "EE United Kingdom", "Digi Malaysia","Koodo Canada", "Yoigo Spain", "Airtel Nigeria", "Airtel Kenya", "Telekom Malaysia","Cosmote Greece", "Digicel Jamaica", "LIME Caribbean", "Telus Canada", "Sprint USA","Movistar Mexico", "Vodafone Germany", "Optus Australia","Vivo Brazil", "Singtel Singapore", "Airtel India", "Ncell Nepal", "Telenor Sweden","MEO Portugal", "Claro Argentina", "EE Estonia", "Telkom South Africa", "Telenor Norway","Yoigo Spain", "Giffgaff United Kingdom", "Lycamobile France", "A1 Telekom Austria", "Telenor Hungary","Vodafone Greece", "Cosmote Romania", "Telenor Serbia", "Vodafone New Zealand", "Telekom Croatia","Orange Belgium", "Telkomsel Indonesia", "Vivacom Bulgaria", "Orange Poland", "Rogers Canada","Telkom South Africa", "Lycamobile Germany", "M1 Singapore", "DT Mobile Austria", "Claro Colombia","Telkomsel Indonesia", "Tele2 Norway", "Telia Estonia", "Telenor Denmark","Rakuten Mobile Japan","Ooredoo Qatar","Movistar Argentina", "T-Mobile Netherlands", "Telekom Hungary", "Vodafone Romania","NOS Portugal", "Digicel Haiti", "Three Hong Kong", "Airtel Bangladesh", "Telcel Mexico","Orange Moldova", "Telkomsel Indonesia", "Telenor Bulgaria","Vodafone Ukraine", "Cosmote Greece","T-Mobile Czech Republic", "NetOne Zimbabwe", "Glo Nigeria", "MTS Belarus", "Cell C South Africa","Maxis Malaysia", "Fido Canada", "Zain Saudi Arabia", "Telenor Serbia", "Beeline Uzbekistan","A1 Telekom Austria", "Zong Pakistan", "Jazz Pakistan", "Vodafone Portugal", "Telstra Australia","Vodafone Ireland", "Orange Slovakia", "Claro Peru", "Vivo Brazil", "Vodafone Czech Republic","Telenor Montenegro", "Digi Malaysia", "Etisalat Egypt", "Tigo Rwanda", "Robi Bangladesh","MTC Namibia", "AIS Thailand", "Vodafone Greece", "Orange Romania", "T-Mobile Poland","Telenor Hungary", "Telia Latvia", "Ooredoo Oman", "Optus Australia", "Orange Belgium","Telenor Norway", "Lycamobile France", "EE Estonia", "Yoigo Spain", "Giffgaff United Kingdom","Sprint USA", "Telus Canada", "Vodafone Germany", "Movistar Mexico", "Telkomsel Indonesia","Vivo India", "Airtel India", "Ncell Nepal", "Telenor Sweden", "MEO Portugal","Claro Argentina", "Telekom Croatia", "Cosmote Romania", "Orange Poland", "Telenor Serbia","Vodafone New Zealand", "Vivacom Bulgaria", "Telenor Denmark", "T-Mobile Netherlands", "NOS Portugal","Telkomsel Indonesia", "Tele2 Norway", "Telia Estonia", "Telenor Denmark", "Rakuten Mobile Japan","Ooredoo Qatar", "Movistar Argentina", "T-Mobile Netherlands", "Telekom Hungary", "Vodafone Romania","Digicel Haiti", "Three Hong Kong", "Airtel Bangladesh", "Telcel Mexico", "Orange Moldova","Telkomsel Indonesia", "O2 Germany", "Airtel Nigeria", "Orange Kenya","Digicel Jamaica","Unitel Angola", "MobiFone Vietnam", "TMN Portugal", "Grameenphone Bangladesh", "Movitel Mozambique","Telkom South Africa", "Globacom Nigeria", "Nawras Oman", "Vodafone Ghana", "Telenor Pakistan","Yoigo Spain", "SFR France", "Tigo Colombia", "Vodafone Qatar", "Etisalat UAE","Telenor Norway", "Telia Finland", "LIME Caribbean", "EE United Kingdom", "Koodo Canada","TIM Italy", "Telekom Romania", "Jio India", "Ooredoo Kuwait", "Orange Switzerland","Bouygues Telecom France", "Entel Bolivia", "A1 Telekom Austria", "MTN South Africa", "Vodafone Hungary","Zain Jordan", "Ncell Nepal", "Zain Kuwait", "Djezzy Algeria", "Smart Philippines","Telenor Bulgaria", "Cosmote Greece", "Vodafone Portugal", "Telstra Australia", "Three Ireland","Rogers Canada", "Safaricom Kenya", "Orange Luxembourg", "Elisa Finland", "Vodafone Netherlands","KPN Netherlands", "Telia Lithuania", "Vodafone Iceland", "Tigo Ghana", "Idea India","Tata Docomo India", "Aircel India", "Claro Chile", "Movistar Peru", "T-Mobile Croatia","Telkomsel Indonesia", "O2 Czech Republic", "Smartfren Indonesia", "Axiata Malaysia", "Digicel Caribbean","Beeline Kazakhstan", "Moldcell Moldova", "Djezzy Algeria", "Tigo Rwanda", "Vodafone Egypt","COSMOTE Cyprus", "Bell Mobility Canada", "Telenor Sweden", "3 Sweden", "DNA Finland","Zain Bahrain", "Ooredoo Tunisia", "Orange Morocco", "Vivacom Bulgaria", "VIPnet Croatia","Vodafone Greece", "Orange Romania", "T-Mobile Poland", "Telenor Hungary", "AIS Thailand","TrueMove Thailand", "Vodafone Czech Republic", "Digi Malaysia", "XL Axiata Indonesia", "Dialog Sri Lanka","MTN Uganda", "Airtel Bangladesh", "Viva Kuwait", "Wind Italy", "LMT Latvia","Yoigo Spain", "Maroc Telecom Morocco", "Orange Ivory Coast", "Airtel Malawi", "Airtel Zambia", "DITO", "Globe", "GOMO", "TNT", "TM"]
    fbmf_fbdv_dict = {
    "asus": ["ZenFone 8", "ROG Phone 5", "ZenFone 7", "ROG Phone 3", "ZenFone 6", "ROG Phone II", "ZenFone 5Z", "ZenFone 5", "ZenFone 4 Pro", "ZenFone 4", "ZenFone 3 Deluxe", "ZenFone 3", "ZenFone 2 Laser", "ZenFone 2", "ZenFone", "ZenFone 6Z", "ZenFone Max Pro (M2)", "ZenFone Max Pro (M1)", "ZenFone 6Z", "ZenFone Max Plus (M2)", "ZenFone Max (M2)", "ZenFone Max (M1)", "ZenFone Live", "ZenFone Zoom", "ZenFone Selfie", "ASUS_Z01RD", "ASUS_Z01QD", "ASUS_I01WD", "ASUS_I01BD", "ASUS_I01HDA"],
    "lenovo": ["Legion Phone Duel 2", "Legion Phone Duel", "K12 Note", "K10 Note", "Z6 Pro", "Z5 Pro", "Lenovo Z6 Pro", "Lenovo Z6 Youth", "Lenovo Z5s", "Lenovo Z5 Pro GT", "Lenovo Z5 Pro", "Lenovo Z5", "Lenovo K9", "Lenovo A5", "Lenovo K320t", "Lenovo K8 Note", "Lenovo K6 Note", "Lenovo Vibe K5 Note", "Lenovo Vibe K5", "Lenovo Vibe P1", "Lenovo Vibe X3", "Lenovo Vibe Z2 Pro", "Lenovo Vibe Z2", "Lenovo Vibe Z","A6000", "A6000 Plus", "A7000", "A7000 Turbo", "A2010", "A2010-a", "K3 Note", "Vibe K4 Note", "Vibe K5 Note", "Vibe K5 Plus", "Vibe K5", "Vibe K5 Lite", "Vibe K5 Power", "Vibe K5 S", "Vibe X2", "Vibe X3", "Vibe Z2 Pro", "K6 Power", "K6 Note", "K6", "K6 Plus", "K6 Turbo", "Vibe C", "Vibe C2", "Vibe C2 Power", "Vibe C2 K10a40", "Vibe C2 K10a40C", "Vibe B", "Vibe B A2016a40", "Vibe B A2016b30", "Vibe B A2016b31", "Vibe B A2016b31C", "Vibe B A2016b30A", "Vibe B A2016b30B", "Vibe B A2016b30C", "Vibe B A2016b30D", "Vibe B A2016b30E", "Vibe B A2016b30G", "Vibe B A2016b30J", "Vibe B A2016b30K", "Vibe B A2016b30L", "Vibe B A2016b30M", "Vibe B A2016b30N", "Vibe B A2016b30O", "Vibe B A2016b30Q", "Vibe B A2016b30R", "Vibe B A2016b30T", "Vibe B A2016b30W", "Vibe B A2016b30Y", "Vibe B A2016b31A", "Vibe B A2016b31B", "Vibe B A2016b31C", "Vibe B A2016b31E", "Vibe B A2016b31F", "Vibe B A2016b31G", "Vibe B A2016b31H", "Vibe B A2016b31K", "Vibe B A2016b31L", "Vibe B A2016b31M", "Vibe B A2016b31N", "Vibe B A2016b31O", "Vibe B A2016b31P", "Vibe B A2016b31Q", "Vibe B A2016b31R", "Vibe B A2016b31S", "Vibe B A2016b31T", "Vibe B A2016b31U", "Vibe B A2016b31V", "Vibe B A2016b31W", "Vibe B A2016b31X", "Vibe B A2016b31Y", "Vibe B A2016b31Z", "Vibe B A2016b31AA", "Vibe B A2016b31AB", "Vibe B A2016b31AC", "Vibe B A2016b31AD", "Vibe B A2016b31AE", "Vibe B A2016b31AF", "Vibe B A2016b31AG", "Vibe B A2016b31AH", "Vibe B A2016b31AI", "Vibe B A2016b31AJ", "Vibe B A2016b31AK", "Vibe B A2016b31AL", "Vibe B A2016b31AM", "Vibe B A2016b31AN", "Vibe B A2016b31AO", "Vibe B A2016b31AP", "Vibe B A2016b31AQ", "Vibe B A2016b31AR", "Vibe B A2016b31AS", "Vibe B A2016b31AT", "Vibe B A2016b31AU", "Vibe B A2016b31AV", "Vibe B A2016b31AW", "Vibe B A2016b31AX", "Vibe B A2016b31AY", "Vibe B A2016b31AZ", "Vibe B A2016b31BA", "Vibe B A2016b31BB", "Vibe B A2016b31BC", "Vibe B A2016b31BD", "Vibe B A2016b31BE", "Vibe B A2016b31BF", "Vibe B A2016b31BG", "Vibe B A2016b31BH", "Vibe B A2016b31BI", "Vibe B A2016b31BJ", "Vibe B A2016b31BK", "Vibe B A2016b31BL", "Vibe B A2016b31BM", "Vibe B A2016b31BN", "Vibe B A2016b31BO", "Vibe B A2016b31BP", "Vibe B A2016b31BQ", "Vibe B A2016b31BR", "Vibe B A2016b31BS"],
    "sony": ["Xperia 5 III", "Xperia 10 II", "Xperia 1 II", "Xperia 10 Plus", "Xperia 1", "Xperia XZ3", "Xperia 1 III", "Xperia 1 II", "Xperia 1", "Xperia 5 III", "Xperia 5 II", "Xperia 5", "Xperia 10 III", "Xperia 10 II", "Xperia 10", "Xperia Pro", "Xperia L4", "Xperia L3", "Xperia XZ3", "Xperia XZ2 Premium", "Xperia XZ2", "Xperia XZ1 Compact", "Xperia XZ1", "Xperia XZ Premium", "Xperia XZ", "Xperia XA2 Ultra", "Xperia XA2", "Xperia XA1 Ultra", "Xperia XA1 Plus", "Xperia XA1", "Xperia X Compact","C6603", "D6503", "F5121", "F8331", "G3116", "H3113", "J9210", "XQ-AS52", "XQ-AD52", "XQ-BT52", "XQ-BS52", "XQ-AT51", "XQ-AT52", "XQ-AD52", "XQ-AT52", "XQ-AT42", "XQ-AT41", "XQ-AD51", "XQ-BT51", "XQ-BS41", "XQ-BS52", "XQ-BT52", "XQ-AD51", "XQ-BT51", "XQ-BS41", "XQ-AT41", "XQ-BS52", "XQ-BT52", "XQ-AS42", "XQ-BS42", "XQ-AT42", "XQ-BS41", "XQ-AT51", "XQ-AD51", "XQ-AD42", "XQ-AS41", "XQ-BT41", "XQ-BT51", "XQ-BS51", "XQ-BS42", "XQ-AS52", "XQ-AS41", "XQ-BS42", "XQ-BT41", "XQ-AS42", "XQ-AT42", "XQ-AD42", "XQ-BS41", "XQ-AT41", "XQ-BS51", "XQ-BT51", "XQ-AT51", "XQ-AD51", "F8131", "F8132", "G3121", "G3112", "G3123", "G3125", "G8141", "G8142", "G8341", "G8342", "H8216", "H8266", "H8296", "H8416", "H9436", "H9461", "H9436", "H9461", "H9436", "H9493", "H8541", "H8526", "H8116", "H8166", "I4213", "I4293", "I4293", "I4312", "I4332", "I4332", "I4113", "I4193", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4312", "I4332", "I4293", "I4293", "I4213", "I4312", "I4332", "I4293", "I4293", "I4213"],
    "htc": ["Wildfire E3", "Desire 21 Pro", "U20 5G", "Desire 20 Pro", "Desire 19+", "U12 Life","HTC U20", "HTC U12+", "HTC U11", "HTC U12+", "HTC U12 Life", "HTC U11+", "HTC U11 Life", "HTC U11", "HTC U Ultra", "HTC 10", "HTC One M9", "HTC One M8", "HTC One (M7)", "HTC Desire 820", "HTC Desire 816", "HTC Desire 610", "HTC Desire 510", "HTC Butterfly S", "HTC One Max", "HTC One Mini", "HTC Desire 600", "HTC First", "HTC One X+","HTC One M8", "HTC One M9", "HTC 10", "HTC U11", "HTC U12+", "HTC U Ultra", "HTC U Play", "HTC Desire 626", "HTC Desire 816", "HTC Desire 610", "HTC Desire 510", "HTC Desire 820", "HTC Desire 626G+", "HTC One X", "HTC One X+", "HTC One S", "HTC One V", "HTC One Mini", "HTC One Mini 2", "HTC One Max", "HTC One E8", "HTC One E9", "HTC One A9", "HTC One E9+", "HTC One M8s", "HTC Desire Eye", "HTC Desire 820s", "HTC Desire 816G", "HTC Desire 626s", "HTC Desire 530", "HTC Desire 828", "HTC 10 Lifestyle", "HTC U11 Life", "HTC U11 Eyes", "HTC U11+"],
    "apple": ["iPhone 13 Pro", "iPhone 13", "iPhone 13 mini", "iPhone 12 Pro", "iPhone 12", "iPhone SE (3rd Gen)", "iPhone 13 Pro Max", "iPhone 13 Pro", "iPhone 13", "iPhone 13 mini", "iPhone 12 Pro Max", "iPhone 12 Pro", "iPhone 12", "iPhone 12 mini", "iPhone SE (2nd generation)", "iPhone 11 Pro Max", "iPhone 11 Pro", "iPhone 11", "iPhone XR", "iPhone XS Max", "iPhone XS", "iPhone X", "iPhone 8 Plus", "iPhone 8", "iPhone 7 Plus", "iPhone 7", "iPhone SE (1st generation)", "iPhone 6s Plus", "iPhone 6s", "iPhone 6 Plus", "iPhone 6", "iPhone 5s", "iPhone 5c", "iPhone 5", "iPhone 4s", "iPhone 4", "iPhone 3GS", "iPhone 3G", "iPhone","A1549", "A1522", "A1586", "A1633", "A1688", "A1699", "A1700", "A1660", "A1778", "A1661", "A1784", "A1863", "A1901", "A1865", "A1902", "A1920", "A1921", "A2101", "A2102", "A2104", "A1984", "A2103", "A1920", "A1921", "A2160", "A2161", "A2215", "A2217", "A2218", "A2220", "A2221", "A2223", "A2111", "A2229", "A2112", "A2131", "A2106", "A2107", "A2108", "A2162", "A2047", "A2048", "A2049", "A2105", "A2014", "A2015", "A2016", "A1867", "A1868", "A1897", "A1898", "A1899", "A1900", "A1903", "A1923", "A2212", "A2200", "A2202", "A2201", "A2301", "A2223", "A2215", "A1866", "A1993", "A1990", "A2013", "A2012", "A1983", "A1954", "A1953", "A2100", "A2005", "A2114", "A2116", "A2110", "A1920", "A1921", "A1985", "A2115", "A2117", "A2118", "A2003", "A2004", "A2160", "A2161", "A2202", "A2298", "A2299", "A2162", "A2270", "A2271", "A2229", "A2272", "A2273", "A2301", "A2304", "A2324", "A2325", "A2340", "A2341", "A2342", "A2375", "A2376", "A2377", "A2378", "A2406", "A2407", "A2408", "A2451", "A2452", "A2453", "A2600", "A2594", "A2503", "A2571", "A2570", "A2410", "A2402", "A2412", "A2399", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602", "A2604", "A2610", "A2612", "A2626", "A2628", "A2633", "A2634", "A2616", "A2617", "A2630", "A2631", "A2632", "A2624", "A2649", "A2646", "A2647", "A2653", "A2656", "A2654", "A2655", "A2657", "A2658", "A2398", "A2399", "A2403", "A2404", "A2405", "A2406", "A2399", "A2407", "A2408", "A2400", "A2466", "A2478", "A2479", "A2480", "A2522", "A2523", "A2524", "A2602"],
    "oppo": ["Reno 7 Pro", "Reno 7", "Reno 6 Pro+", "A95", "A96", "A93", "Oppo Find X3 Pro", "Oppo Find X2 Pro", "Oppo Find X2", "Oppo Reno 6 Pro+", "Oppo Reno 6 Pro", "Oppo Reno 6", "Oppo Reno 5 Pro+", "Oppo Reno 5 Pro", "Oppo Reno 5", "Oppo A94", "Oppo A74", "Oppo F19 Pro+", "Oppo F19 Pro", "Oppo F19", "Oppo A93", "Oppo A53", "Oppo A33", "Oppo A32", "Oppo A72", "Oppo A52", "Oppo A92", "Oppo A12", "Oppo Reno 3 Pro", "Oppo Reno 3", "Oppo Reno 2", "Oppo Reno", "Oppo K7x", "Oppo K7", "Oppo A9 (2020)", "Oppo A5 (2020)", "CPH1903", "CPH1803", "CPH1859", "CPH1969", "CPH1989", "CPH1919", "CPH1941", "CPH1983", "CPH1963", "CPH1879", "CPH1831", "CPH2035", "CPH2069", "CPH1987", "CPH2071", "CPH2083", "CPH2015", "CPH2019", "CPH2173", "CPH2089", "CPH2067", "CPH2017", "CPH2087", "CPH2205", "CPH2251", "CPH2197", "CPH2235", "CPH2347", "CPH2295", "CPH2249", "CPH2243", "CPH2349", "CPH2359", "CPH2383", "CPH2381", "CPH2239", "CPH2213", "CPH2129", "CPH2195", "CPH2227", "CPH2316", "CPH2353", "CPH2261", "CPH2225", "CPH2269", "CPH2073", "CPH2185", "CPH1877", "CPH2013", "CPH2061", "CPH1955", "CPH1871", "CPH1801", "CPH1873", "CPH1901", "CPH1809", "CPH1853", "CPH1923", "CPH1981", "CPH1833", "CPH1917", "CPH1967", "CPH1937", "CPH1893", "CPH1931", "CPH1921", "CPH1823", "CPH2023", "CPH2021", "CPH2103", "CPH2220", "CPH2127", "CPH2059", "CPH2139", "CPH2253", "CPH2267", "CPH2263", "CPH2247", "CPH2241", "CPH2297", "CPH2357", "CPH2255", "CPH2345", "CPH2329", "CPH2209", "CPH2191", "CPH2199", "CPH2289", "CPH2319", "CPH2343", "CPH2363", "CPH2161", "CPH2163", "CPH1979", "CPH1977", "CPH1973", "CPH1965", "CPH1959", "CPH1951", "CPH1913", "CPH1909", "CPH1905", "CPH1861", "CPH1863", "CPH1967", "CPH1933", "CPH1937", "CPH1921", "CPH1923", "CPH1987", "CPH1919", "CPH1897", "CPH1875", "CPH1874", "CPH1872", "CPH1865", "CPH1863", "CPH1862", "CPH1853", "CPH1852", "CPH1851", "CPH1843", "CPH1841", "CPH1835", "CPH1833", "CPH1832", "CPH1831", "CPH1825", "CPH1823", "CPH1821", "CPH1819", "CPH1813", "CPH1812", "CPH1811", "CPH1809", "CPH1808", "CPH1807", "CPH1805", "CPH1803", "CPH1801"],
    "realme": ["Realme GT Master Edition", "Realme 8i", "Realme 8s", "Narzo 30", "Narzo 20", "Realme 7i", "Realme 8", "Realme 7 Pro", "Realme X50 Pro","Realme GT Master Explorer Edition", "Realme GT Master Edition", "Realme GT", "Realme 8 Pro", "Realme 8", "Realme Narzo 30 Pro", "Realme Narzo 30A", "Realme X7 Pro", "Realme X7", "Realme 7 Pro", "Realme 7", "Realme C21", "Realme C20", "Realme C15", "Realme C12", "Realme C11", "Realme 6 Pro", "Realme 6", "Realme X2 Pro", "Realme XT", "Realme 5 Pro", "Realme 5", "Realme 3 Pro", "Realme 3", "Realme 2 Pro", "Realme 2", "Realme 1","RMX2111", "RMX3092", "RMX3161", "RMX3142", "RMX3185", "RMX3186", "RMX3281", "RMX3274", "RMX3361", "RMX3165", "RMX3243", "RMX3242", "RMX3294", "RMX3162", "RMX3241", "RMX3290", "RMX3289", "RMX3270", "RMX3267", "RMX3266", "RMX3263", "RMX3260", "RMX3240", "RMX3280", "RMX3276", "RMX3244", "RMX3121", "RMX3063", "RMX3061", "RMX3090", "RMX3091", "RMX3080", "RMX3211", "RMX3334", "RMX3221", "RMX3295", "RMX3292", "RMX3331", "RMX3383", "RMX3350", "RMX3332", "RMX3300", "RMX3310", "RMX3311", "RMX3385", "RMX3336", "RMX3337", "RMX3338", "RMX3235", "RMX3225", "RMX3124", "RMX3065", "RMX3143", "RMX3201", "RMX3070", "RMX3250", "RMX3246", "RMX3261", "RMX3071", "RMX3150", "RMX3164", "RMX3141", "RMX3063", "RMX3060", "RMX3357", "RMX3223", "RMX3330", "RMX3284", "RMX3362", "RMX3236", "RMX3193", "RMX3191", "RMX3358", "RMX3384", "RMX3262", "RMX3248", "RMX3339", "RMX3283", "RMX3195", "RMX3093", "RMX3098", "RMX3245", "RMX3095", "RMX3064", "RMX3341", "RMX3340", "RMX3365", "RMX3363", "RMX3364", "RMX3366", "RMX3367", "RMX3368", "RMX3369", "RMX3370", "RMX3371", "RMX3372", "RMX3373", "RMX3374", "RMX3375", "RMX3376", "RMX3377", "RMX3378", "RMX3379", "RMX3380", "RMX3381", "RMX3382", "RMX3312", "RMX3249", "RMX3094", "RMX3116", "RMX3187", "RMX3096", "RMX3097", "RMX3171", "RMX3152", "RMX3115", "RMX3081", "RMX3272", "RMX3273", "RMX3264", "RMX3265", "RMX3269", "RMX3268", "RMX3082", "RMX3083", "RMX3084", "RMX3085", "RMX3086", "RMX3087", "RMX3088", "RMX3089", "RMX3099", "RMX309A", "RMX309B", "RMX309C", "RMX309D", "RMX309E", "RMX309F", "RMX309G", "RMX309H", "RMX309I", "RMX309J", "RMX309K", "RMX309L", "RMX309M", "RMX309N", "RMX309O", "RMX309P", "RMX309Q", "RMX309R", "RMX309S", "RMX309T", "RMX309U", "RMX309V", "RMX309W", "RMX309X", "RMX309Y", "RMX309Z", "RMX31ZM", "RMX31ZN", "RMX31ZS", "RMX31ZT", "RMX31ZW", "RMX31ZV", "RMX31ZR", "RMX31ZQ", "RMX31ZP", "RMX31ZO", "RMX31ZN", "RMX31ZM", "RMX31ZL", "RMX31ZK", "RMX31ZJ", "RMX31ZI", "RMX31ZH", "RMX31ZG", "RMX31ZF", "RMX31ZE", "RMX31ZD", "RMX31ZC"],
    "motorola": ["Moto G100", "Moto G60", "Moto G40 Fusion", "Moto G30", "Moto G9 Power", "Moto G8", "Moto G Power 2022", "Moto G7", "Moto G Stylus 2022", "Motorola Edge 20 Pro", "Motorola Edge 20", "Motorola Edge 20 Lite", "Motorola Moto G Stylus (2021)", "Motorola Moto G Power (2021)", "Motorola Moto G Play (2021)", "Motorola Moto G9 Plus", "Motorola Moto G9", "Motorola Moto G8 Plus", "Motorola Moto G8 Power", "Motorola Moto G8", "Motorola Moto G7 Plus", "Motorola Moto G7 Power", "Motorola Moto G7 Play", "Motorola Moto G7", "Motorola Moto G6 Plus", "Motorola Moto G6", "Motorola Moto G5S Plus", "Motorola Moto G5 Plus", "Motorola Moto G5", "Motorola Moto G4 Plus", "Motorola Moto G4", "Motorola Moto X4", "Motorola Moto X (2nd Gen)", "Motorola Moto X", "Motorola Moto Z3 Play", "Motorola Moto Z2 Play", "Motorola Moto Z", "Motorola Moto E7 Plus", "Motorola Moto E6 Plus", "Motorola Moto E5 Plus", "Motorola Moto E4 Plus", "Motorola Moto E (2nd Gen)", "Motorola Moto E", "XT2127-2", "XT2127-4", "XT2127-5", "XT2127-6", "XT2127-7", "XT2127-8", "XT2127-10", "XT2127-11", "XT2127-12", "XT2127-13", "XT2127-14", "XT2127-15", "XT2127-16", "XT2127-17", "XT2127-18", "XT2127-19", "XT2127-20", "XT2127-21", "XT2127-22", "XT2127-23", "XT2127-24", "XT2127-25", "XT2127-26", "XT2127-27", "XT2127-28", "XT2127-29", "XT2127-30", "XT2127-31", "XT2127-32", "XT2127-33", "XT2127-34", "XT2127-35", "XT2127-36", "XT2127-37", "XT2127-38", "XT2127-39", "XT2127-40", "XT2127-41", "XT2127-42", "XT2127-43", "XT2127-44", "XT2127-45", "XT2127-46", "XT2127-47", "XT2127-48", "XT2127-49", "XT2127-50", "XT2127-51", "XT2127-52", "XT2127-53", "XT2127-54", "XT2127-55", "XT2127-56", "XT2127-57", "XT2127-58", "XT2127-59", "XT2127-60", "XT2127-61", "XT2127-62", "XT2127-63", "XT2127-64", "XT2127-65", "XT2127-66", "XT2127-67", "XT2127-68", "XT2127-69", "XT2127-70", "XT2127-71", "XT2127-72", "XT2127-73", "XT2127-74", "XT2127-75", "XT2127-76", "XT2127-77", "XT2127-78", "XT2127-79", "XT2127-80", "XT2127-81", "XT2127-82", "XT2127-83", "XT2127-84", "XT2127-85", "XT2127-86", "XT2127-87", "XT2127-88", "XT2127-89", "XT2127-90", "XT2127-91", "XT2127-92", "XT2127-93", "XT2127-94", "XT2127-95", "XT2127-96", "XT2127-97", "XT2127-98", "XT2127-99", "XT2127-100", "XT2127-101", "XT2127-102", "XT2127-103", "XT2127-104", "XT2127-105", "XT2127-106", "XT2127-107", "XT2127-108", "XT2127-109", "XT2127-110", "XT2127-111", "XT2127-112", "XT2127-113", "XT2127-114", "XT2127-115", "XT2127-116", "XT2127-117", "XT2127-118", "XT2127-119", "XT2127-120", "XT2127-121", "XT2127-122", "XT2127-123", "XT2127-124", "XT2127-125", "XT2127-126", "XT2127-127", "XT2127-128", "XT2127-129", "XT2127-130", "XT2127-131", "XT2127-132", "XT2127-133", "XT2127-134", "XT2127-135", "XT2127-136", "XT2127-137", "XT2127-138", "XT2127-139", "XT2127-140", "XT2127-141", "XT2127-142", "XT2127-143", "XT2127-144", "XT2127-145", "XT2127-146", "XT2127-147", "XT2127-148", "XT2127-149", "XT2127-150", "XT2127-151", "XT2127-152", "XT2127-153"],
    "nokia": ["Nokia X20", "Nokia X10", "Nokia G20", "Nokia G10", "Nokia 8.3 5G", "Nokia 5.4", "Nokia 3.4", "Nokia 2.4", "Nokia 8.1", "Nokia 7.2", "Nokia 6.2", "Nokia 4.2", "Nokia 3.2", "Nokia 2.2", "Nokia 9 PureView", "Nokia 8 Sirocco", "Nokia 8", "Nokia 7 Plus", "Nokia 7.1", "Nokia 6.1 Plus", "Nokia 6.1", "Nokia 5.1 Plus", "Nokia 5.1", "Nokia 4.1", "Nokia 3.1 Plus", "Nokia 3.1", "Nokia 2.1", "Nokia 1", "TA-1337", "TA-1380", "TA-1395", "TA-1208", "TA-1208", "TA-1334", "TA-1336", "TA-1230", "TA-1239", "TA-1283", "TA-1335", "TA-1234", "TA-1347", "TA-1353", "TA-1340", "TA-1233", "TA-1338", "TA-1386", "TA-1307", "TA-1296", "TA-1281", "TA-1333", "TA-1244", "TA-1235", "TA-1357", "TA-1236", "TA-1339", "TA-1316", "TA-1329", "TA-1343", "TA-1354", "TA-1300", "TA-1303", "TA-1289", "TA-1315", "TA-1287", "TA-1342", "TA-1351", "TA-1331", "TA-1325", "TA-1295", "TA-1240", "TA-1286", "TA-1328", "TA-1284", "TA-1293", "TA-1341", "TA-1292", "TA-1327", "TA-1298", "TA-1323", "TA-1238", "TA-1291", "TA-1345", "TA-1309", "TA-1344", "TA-1324", "TA-1346", "TA-1326", "TA-1304", "TA-1320", "TA-1348", "TA-1318", "TA-1330", "TA-1280", "TA-1246", "TA-1248", "TA-1317", "TA-1299", "TA-1310", "TA-1350", "TA-1332", "TA-1242", "TA-1206", "TA-1294", "TA-1313", "TA-1249", "TA-1241", "TA-1216", "TA-1297", "TA-1285", "TA-1319", "TA-1243", "TA-1356"],
    "xiaomi": ["Mi 11", "Mi 10 Pro", "Mi 9T","M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2012K11C","Redmi 6A","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4","Redmi Note 5", "Redmi 4X","Redmi Note 8","Redmi Note 8 Pro","Xiaomi Mi 11 Ultra", "Xiaomi Mi 11 Pro", "Xiaomi Mi 11", "Xiaomi Mi 10 Ultra", "Xiaomi Mi 10 Pro", "Xiaomi Mi 10", "Xiaomi Mi 10T Pro", "Xiaomi Mi 10T", "Xiaomi Mi 9T Pro", "Xiaomi Mi 9T", "Xiaomi Mi 9 Pro 5G", "Xiaomi Mi 9", "Xiaomi Mi 8 Pro", "Xiaomi Mi 8", "Xiaomi Mi 8 Lite", "Xiaomi Mi 8 SE", "Xiaomi Mi Mix 3", "Xiaomi Mi Mix 2S", "Xiaomi Mi Mix 2", "Xiaomi Mi Mix", "Xiaomi Redmi Note 11 Pro+", "Xiaomi Redmi Note 11 Pro", "Xiaomi Redmi Note 11", "Xiaomi Redmi Note 10 Pro", "Xiaomi Redmi Note 10", "Xiaomi Redmi Note 9 Pro", "Xiaomi Redmi Note 9", "Xiaomi Redmi Note 8 Pro", "Xiaomi Redmi Note 8", "Xiaomi Redmi Note 7 Pro", "Xiaomi Redmi Note 7", "Xiaomi Redmi K40 Pro", "Xiaomi Redmi K40", "Xiaomi Redmi K30 Pro", "Xiaomi Redmi K30", "Xiaomi Redmi K20 Pro", "Xiaomi Redmi K20", "Xiaomi Poco X3 Pro", "Xiaomi Poco X3", "Xiaomi Poco X2", "Xiaomi Poco F3", "Xiaomi Poco F2 Pro", "Xiaomi Poco F1"],
    "samsung": ["Galaxy S21", "Galaxy A52", "Galaxy S20","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935F","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820","SPH-L720","SM-S906E", "Samsung Galaxy S21 Ultra", "Samsung Galaxy S21+", "Samsung Galaxy S21", "Samsung Galaxy Note 20 Ultra", "Samsung Galaxy Note 20", "Samsung Galaxy S20 Ultra", "Samsung Galaxy S20+", "Samsung Galaxy S20", "Samsung Galaxy Note 10+", "Samsung Galaxy Note 10", "Samsung Galaxy S10+", "Samsung Galaxy S10", "Samsung Galaxy Note 9", "Samsung Galaxy S9+", "Samsung Galaxy S9", "Samsung Galaxy Note 8", "Samsung Galaxy S8+", "Samsung Galaxy S8", "Samsung Galaxy Note 7", "Samsung Galaxy S7 Edge", "Samsung Galaxy S7", "Samsung Galaxy Note 5", "Samsung Galaxy S6 Edge+", "Samsung Galaxy S6 Edge", "Samsung Galaxy S6", "Samsung Galaxy Note 4", "Samsung Galaxy S5", "Samsung Galaxy S4", "Samsung Galaxy S3", "Samsung Galaxy Note 3", "SM-G991", "SM-G981", "SM-G973", "SM-G960", "SM-G950", "SM-G930", "SM-G920", "SM-G900", "GT-I9500", "GT-I9300", "GT-I9100", "GT-I9000", "SM-N981", "SM-N970", "SM-N960", "SM-N950", "SM-N920", "SM-N910", "SM-N900", "GT-N7100", "GT-N7000", "SM-G991", "SM-G981", "SM-G973", "SM-G960", "SM-G950", "SM-G930", "SM-G920", "SM-G900", "GT-I9500", "GT-I9300", "GT-I9100", "GT-I9000", "SM-N981", "SM-N970", "SM-N960", "SM-N950", "SM-N920", "SM-N910", "SM-N900", "GT-N7100", "GT-N7000", "SM-A526B", "SM-A516B", "SM-A516N", "SM-A526U", "SM-A716U", "SM-A716V", "SM-A5260", "SM-A526W", "SM-A126U", "SM-A126V", "SM-A016G", "SM-A016B", "SM-A016M", "SM-A025M", "SM-A025F", "SM-A217F", "SM-A217M", "SM-A207F", "SM-A207M", "SM-A102U", "SM-A102U1", "SM-A102W", "SM-A102N", "SM-A1020", "SM-A105F", "SM-A105G", "SM-A105M", "SM-A202F", "SM-A202G", "SM-A202M", "SM-A125U", "SM-A125V", "SM-A022G", "SM-A022M", "SM-A027G", "SM-A027M", "SM-A2170", "SM-A115M", "SM-A107M", "SM-A107F", "SM-A107M", "SM-A0220", "SM-A115F", "SM-A102F", "SM-A1050"],
    "vivo": ["Vivo_X60_Pro", "Vivo_X50_Pro", "Vivo_X30_Pro", "Vivo_X27", "Vivo_X23", "Vivo_X21", "Vivo_V21", "Vivo_V17", "Vivo_V15", "Vivo_V11", "Vivo_V9", "Vivo_Y95", "Vivo_Y91", "Vivo_Y81", "Vivo_Y71", "Vivo_S1", "V2056", "V2112A", "V2112", "V2122A", "V2120A", "V2120", "V2116A", "V2114A", "V2112A", "V2010A", "V2019A", "V2010", "V2003A", "V2002A", "V2002", "V1932A", "V1932T", "V1932", "V1929A", "V1928A", "V1928T", "V1928", "V1927A", "V1926A", "V1925A", "V1925", "V1924A", "V1922A", "V1921A", "V1921", "V1920A", "V1919A", "V1916A", "V1916", "V1912A", "V1911A", "V1910A", "V1910", "V1909A", "V1907A", "V1905", "V1903A", "V1901A", "V1901T", "V1901", "V1836", "V1824A", "V1824T", "V1824", "V1818A", "V1818T", "V1813A", "V1813T", "V1813", "V1812A", "V1811A", "V1811T", "V1811", "V1808A", "V1808T", "V1808", "V1801A", "V1801T", "V1801", "V1730T", "V1730F", "V1730A", "V1730", "V1724A", "V1723A", "V1723", "V1721A", "V1720A", "V1720T", "V1720", "V1716A", "V1715A", "V1715", "V1713A", "V1713", "V1712A", "V1712", "V1711T", "V1711A", "V1711", "V1709A", "V1709T", "V1709", "V1708A", "V1708T", "V1707A", "V1707T", "V1706T", "V1706", "V1703A", "V1701A", "V1701", "V1624A", "V1623A", "V1622A", "V1622", "V1621A", "V1619", "V1618A", "V1617A", "V1616", "V1615T", "V1614T", "V1613", "V1611T", "V1611", "V1608A", "V1609", "V1605", "V1604", "V1603", "V1601", "V1570", "V1562", "V1561", "V1550", "V1548", "V1546", "V1543", "V1542", "V1540", "V1530", "V1520", "V1510", "V1500", "V1420", "V1400", "V1310", "V1320"],
    "zte": ["ZTE_Axon_10_Pro", "ZTE_Axon_9", "ZTE_Axon_7", "ZTE_Axon_7_Mini", "ZTE_Blade_20", "ZTE_Blade_10", "ZTE_Blade_V10", "ZTE_Blade_V9", "ZTE_Blade_X", "ZTE_Blade_A7", "ZTE_Nubia_Red_Magic", "ZTE_Nubia_Z20", "ZTE_Nubia_X", "ZTE_Nubia_Z18", "ZTE_Nubia_Z17","Axon_10_Pro", "Axon_9", "Axon_7", "Axon_7_Mini", "Blade_20", "Blade_10", "Blade_V10", "Blade_V9", "Blade_X", "Blade_A7", "Nubia_Red_Magic", "Nubia_Z20", "Nubia_X", "Nubia_Z18", "Nubia_Z17"],
    "lg": ["LG_G8", "LG_V50", "LG_V40", "LG_G7", "LG_V30", "LG_G6", "LG_V20", "LG_G5", "LG_V10", "LG_G4", "LG_G3", "LG_G2", "LG_G_Flex"],
    "huawei": ["Huawei_P40", "Huawei_P30", "Huawei_P20", "Huawei_Mate_30", "Huawei_Mate_20", "Huawei_Mate_10", "Huawei_Nova_5", "Huawei_Nova_4", "Huawei_Nova_3", "Huawei_P10", "Huawei_P9", "Huawei_Honor_9", "Huawei_Honor_8", "Huawei_Y9", "Huawei_Y8"],
    "oneplus": ["OnePlus_9_Pro", "OnePlus_9", "OnePlus_8T", "OnePlus_8_Pro", "OnePlus_8", "OnePlus_7T_Pro", "OnePlus_7T", "OnePlus_7_Pro", "OnePlus_7", "OnePlus_6T", "OnePlus_6", "OnePlus_5T", "OnePlus_5", "OnePlus_3T", "OnePlus_3"]}
    fbcr = random.choice(fbcr_values)
    fbmf = random.choice(list(fbmf_fbdv_dict.keys()))
    fbdv = random.choice(fbmf_fbdv_dict[fbmf])
    user_agent = f"[FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(0,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/en_US;FBRV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBCR/"+fbcr+";FBMF/"+fbmf+";FBBD/"+fbmf+";FBPN/com.facebook.katana;FBDV/"+fbdv+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:]"
    return user_agent

def user_agent():
    devices = [
        "[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 9 Pro;FBSV/10]",
        "[FBAN/FB4A;FBAV/316.0.0.54.116;FBBV/287519012;FBDM/{density=2.75,width=1080,height=2134};FBLC/cs_CZ;FBRV/289140577;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/10]",
        "[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401209;FBDM/{density=2.0,width=720,height=1456};FBLC/it_IT;FBRV/273474118;FBCR/I TIM;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1931;FBSV/10]",
        "[FBAN/FB4A;FBAV/435.0.0.42.112;FBBV/523162189;FBDM/{density=3.0,width=1080,height=2165};FBLC/it_IT;FBRV/526139383;FBCR/TIM;FBMF/OnePlus;FBBD/OnePlus;FBDV/LE2113;FBSV/13]",
        "[FBAN/FB4A;FBAV/221.0.0.48.102;FBBV/154683427;FBDM/{density=2.75,width=1080,height=2030};FBLC/en_GB;FBRV/155327069;FBCR/Banglalink;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 5;FBSV/8.1.0]"
    ]
    prefix = "[FBAN/FB4A;FBAV/" + str(random.randint(11, 80)) + ".0.0." + str(random.randint(9, 49)) + "." + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(11111111,99999999)) + ";"
    ua = prefix + random.choice(devices)
    return ua

def bgraph(uid, pw, path_file, extract_type, success_count, existing_uids):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw,
        'access_token': accessToken
    }
    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
    try:
        response = requests.post(url, data=data).json()
        if 'access_token' in response:
            token = response['access_token']
            with open(path_file, 'a') as f:
                f.write(f"{uid}|{token}\n")
            print(f" {green}    SUCCESSFULLY TO EXTRACTED ACCOUNT ─────> {uid}.")
            success_count.append(uid)
        else:
            print(f" {red}    FAILED TO EXTRACT ACCOUNT ─────> {uid}.")
    except Exception as e:
        pass

def proz(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_uids = set()
    if os.path.exists(token_output_path):
        with open(token_output_path, 'r') as f:
            existing_uids = {line.split('|')[0] for line in f.readlines()}
    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()
        accounts = [line.strip() for line in accounts if '|' in line.strip()]
        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return
        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph, uid, pw, token_output_path, extract_type, success_count, existing_uids)
                       for uid, pw in [account.split('|') for account in accounts]]
            for future in futures:
                future.result()
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print(f" {green}    SUCCESSFULLY EXTRACTED ACCOUNT ─────> {len(success_count)}.")
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
        return

def load_existing_tokens(path_file):
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return {line.split('|')[0] for line in f.readlines()}
    return set()

def bgraph_page(uid, pw, path_file, extract_type, success_count, existing_tokens):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw,
        'access_token': accessToken
    }
    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
    try:
        response = requests.post(url, data=data).json()
        if 'access_token' in response:
            token = response['access_token']
            pages = extract_fb_pages(token)
            if pages:
                for page in pages:
                    page_id = page['id']
                    if page_id not in existing_tokens:
                        with open(path_file, 'a') as f:
                            f.write(f"{page_id}|{page['accessToken']}\n")
                        print(f" {white}{uid}  ─────> {green}PAGE ID: {red}{page_id} {yellow}EXTRACTED SUCCESSFULLY")
                        existing_tokens.add(page_id)
                    else:
                        print(f" {white}ID:  {page_id} ─────> {green}ALREADY EXISTS ! ")
            else:
                print(f" {white}{uid} ─────> {red}DOESN'T HAVE PAGES !")
            success_count.append(uid)
        else:
            print(f" {white}{uid}  ─────> {red}FAILED TO EXTRACT ! ")
    except Exception as e:
        pass

def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    pages_data = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f'Error: {response.text}')
            return None
        data = response.json()
        for page in data.get('data', []):
            pages_data.append({
                'id': page.get('id'),
                'accessToken': page.get('access_token')
            })
        url = data.get('paging', {}).get('next')
    return pages_data

def prozc(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_tokens = load_existing_tokens(token_output_path)    
    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()
        accounts = [line.strip() for line in accounts if '|' in line.strip()]
        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return
        with thread.ThreadPoolExecutor(max_workers=30) as executor:
            futures = [executor.submit(bgraph_page, uid, pw, token_output_path, extract_type, success_count, existing_tokens)
                       for uid, pw in [account.split('|') for account in accounts]]
            for future in futures:
                future.result()
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print(f" {green}    SUCCESSFULLY EXTRACTED ACCOUNT PAGE ─────> {len(success_count)}.")
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except FileNotFoundError:
        print(f"File not found: {accounts_file}")

def axl2():
    clear_screen()
    ethan()
    colorful_loading()
    folder_path = "/sdcard/boostphere"  
    print(f"     {yellow}[01] {blue}FRA EXTRACT ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA EXTRACT PAGES")
    print(f"     {yellow}[03] {blue}RPW EXTRACT ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW EXTRACT PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"{white} CHOOSE : ").strip()
    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {yellow}THE FORMAT SHOULD BE {red}uid|pass")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f" {yellow}PUT FILE PATH: ").strip()
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    prozc(file_path, account_file, extract_type)

def axl1():
    clear_screen()
    ethan()
    colorful_loading()
    folder_path = "/sdcard/boostphere"
    print(f"     {yellow}[01] {blue}FRA EXTRACT ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA EXTRACT PAGES")
    print(f"     {yellow}[03] {blue}RPW EXTRACT ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW EXTRACT PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"{white} CHOOSE : ").strip()
    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {yellow}THE FORMAT SHOULD BE {red}uid|pass")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f" {yellow}PUT FILE PATH: ").strip()
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    token_output_path = account_file
    proz(file_path, token_output_path, extract_type)

folder_name = "/sdcard/boostphere"
file_names = ["FRAACCOUNT.txt", "FRAPAGES.txt", "RPWACCOUNT.txt", "RPWPAGES.txt","generated_code.txt"]
if not os.path.exists(folder_name):
    try:
          os.makedirs(folder_name)
    except Exception:
              pass
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        if not os.path.exists(file_path):
            try:
                with open(file_path, 'w') as file:
                    pass  
            except Exception:
                pass  

def count_tokens(accounts_file, pages_file):
    total_accounts = 0
    total_pages = 0
    try:
        with open(accounts_file, 'r') as af:
            total_accounts = sum(1 for line in af if line.strip())  # Count non-empty lines
    except FileNotFoundError:
        print(f"Account file not found: {accounts_file}")
    try:
        with open(pages_file, 'r') as pf:
            total_pages = sum(1 for line in pf if line.strip())  # Count non-empty lines
    except FileNotFoundError:
        print(f"Page file not found: {pages_file}")
    return total_accounts, total_pages

def remove_duplicates():
    file_paths = {
        "1": "/sdcard/boostphere/FRAACCOUNT.txt",
        "2": "/sdcard/boostphere/FRAPAGES.txt",
        "3": "/sdcard/boostphere/RPWACCOUNT.txt",
        "4": "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[1]  {blue}FRA ACCOUNT")
    print(f"     {yellow}[2]  {blue}FRA PAGES")
    print(f"     {yellow}[3]  {blue}RPW ACCOUNT")
    print(f"     {yellow}[4]  {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"{white} CHOOSE : ").strip()
    if choice not in file_paths:
        print("Invalid choice. Please try again.")
        return
    file_path = file_paths[choice]
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        seen_uids = set()
        unique_lines = []
        for line in lines:
            if '|' in line:
                uid, password = line.split('|', 1)
                if uid not in seen_uids:
                    unique_lines.append(line)
                    seen_uids.add(uid)
        with open(file_path, 'w') as file:
            file.writelines(unique_lines)
        print(f" {green}SUCCESSFULLY REMOVED DUPLICATES FROM: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

def perform_reaction_vid(token, uid_url, reaction_type, reactions_count):
    access_token = token.split('|')[1]
    auto_react_url = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    try:
        response = requests.post(auto_react_url)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def clear_text_files():
    file_paths = {
        "1": "/sdcard/boostphere/FRAACCOUNT.txt",
        "2": "/sdcard/boostphere/FRAPAGES.txt",
        "3": "/sdcard/boostphere/RPWACCOUNT.txt",
        "4": "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[01]  {blue}FRA ACCOUNT")
    print(f"     {yellow}[02]  {blue}FRA PAGES")
    print(f"     {yellow}[03]  {blue}RPW ACCOUNT")
    print(f"     {yellow}[04]  {blue}RPW PAGES")
    print(f"     {yellow}[05]  {blue}ALL FILES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    user_choice = input(f"{white} CHOOSE : ").strip()
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    if user_choice == '5':
        for file_path in file_paths.values():
            try:
                with open(file_path, 'w') as file:
                    file.truncate(0)
                print(f" {green}SUCCESSFULLY CLEARED: {file_path}")
            except Exception as e:
                print(f"Error clearing {file_path}: {str(e)}")
        return
    selected_file = file_paths.get(user_choice)
    if selected_file:
        try:
            with open(selected_file, 'w') as file:
                file.truncate(0)
            print(f" {green}SUCCESSFULLY CLEARED: {selected_file}")
        except Exception as e:
            print(f"Error clearing {selected_file}: {str(e)}")
    else:
        print("Invalid choice. Please enter a valid number.")

def perform_reaction_fast_vid():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {white}FORMAT : {red}https://www.facebook.com/100078043222260/videos/539673715119122/?mibextid=rS40aB7S9Ucbxw6v")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    post_link = input(f" {white}ENTER THE POST LINK OR ID: ")
    uid_url = extract_facebook_video_id(post_link)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f"     {yellow}[01] {blue}LIKE")
    print(f"     {yellow}[02] {blue}LOVE")
    print(f"     {yellow}[03] {blue}WOW")
    print(f"     {yellow}[04] {blue}SAD")
    print(f"     {yellow}[05] {blue}ANGRY")
    print(f"     {yellow}[06] {blue}HAHA")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        reaction_choice = int(input(f"{white} CHOOSE : ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        num_reactions = int(input(f" {yellow}ENTER THE NUMBER OF REACTIONS: "))
    except ValueError:
        print(f"Please enter a valid number for reactions.")
        return
    if num_reactions > len(tokens):
        print(f" {red}ENTER AGAIN NOT EXCEEDING {len(tokens)}")
        return
    reactions_count = 0
    max_workers = 15
    while reactions_count < num_reactions and tokens:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction_vid, token, uid_url, reaction_type): token for token in tokens}            
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        print(f"   {green}[SUCCESS] SUCCESSFULLY REACTED TO {white}───────> {red}{uid_url}")
                        if reactions_count >= num_reactions:
                            break
                    else:
                        print(f"   {green}[FAILED] FAILED TO SEND REACTION  {white}───────> {red}{uid_url}")
                except Exception as e:
                    print(f"Error processing token {token}: {str(e)}")
        tokens = tokens[len(future_to_token):]
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}REACTIONS COMPLETE! {reactions_count} REACTIONS WERE SUCCESSFULLY SENT.")
    print(f" {green}TOTAL REACTIONS SENT: {reactions_count} OUT OF {num_reactions}")

def fetch_account_info(file_options):
    clear_screen()
    ethan()
    print(f"     {yellow}CHOOSE WHICH FILE YOU WANT TO CHECK:")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    for key, value in file_options.items():
        print(f"     {red}[{key}] {yellow}{value.split('/')[-1]}")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    file_choice = int(int(input(f"{white} CHOOSE : ").strip()))
    accounts_file = file_options.get(file_choice)
    if accounts_file is None:
        print("Invalid choice. Exiting.")
        return
    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()
        for account in accounts:
            uid, token = account.strip().split('|')
            account_info = get_account_info(token)
            if account_info:
                account_name = account_info.get('name', 'No name available')
                print(f"     {yellow}ACCOUNT NAME {red}: {green}{account_name}")
                pages = extract_fb_pages(token)
                if pages:
                    print()
                    print(f"          {yellow}PAGES ASSOCIATED WITH {white}: {red}{account_name}")
                    for page in pages:
                        print()
                        print(f"       👉 {yellow}{page['name']} {white}= {green}PAGE ID: {red}{page['id']}")
                else:
                    print(f"     {red}NO PAGES ASSOCIATED WITH THIS ACCOUNT ! .")
            else:
                print(f"     {yellow}FAILED TO FETCH ACCOUNT INFORMATION ! {white}= {red}{uid}")
    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
    except Exception as e:
        pass

def get_account_info(token):
    url = 'https://graph.facebook.com/v18.0/me'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            pass
            return None
    except Exception as e:
        pass
        return None

def extract_fb_pages(token):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    pages_data = []
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for page in data.get('data', []):
                pages_data.append({
                    'id': page.get('id'),
                    'name': page.get('name'),
                    'accessToken': page.get('access_token')
                })
            return pages_data
        else:
            print(f"Failed to fetch pages: {response.text}")
            return None
    except Exception as e:
        pass
        return None

file_options = {
    1: "/sdcard/boostphere/FRAACCOUNT.txt",
    2: "/sdcard/boostphere/FRAPAGES.txt",
    3: "/sdcard/boostphere/RPWACCOUNT.txt",
    4: "/sdcard/boostphere/RPWPAGES.txt"
}

def perform_reaction(token, uid_url, reaction_type):
    access_token = token.split('|')[1]
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()
    }
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def perform_reaction_fast():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return        
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    print(f" {white}FORMAT : {red}https://www.facebook.com/100078043222260/posts/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    z = input(f" {white}ENTER THE POST LINK OR ID: ")
    post_id = extract_ids(z)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id
    print(f"     {yellow}[01] {blue}LIKE")
    print(f"     {yellow}[02] {blue}LOVE")
    print(f"     {yellow}[03] {blue}WOW")
    print(f"     {yellow}[04] {blue}SAD")
    print(f"     {yellow}[05] {blue}ANGRY")
    print(f"     {yellow}[06] {blue}HAHA")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        reaction_choice = int(input(f"{white} CHOOSE : ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_reactions = int(input(f" {yellow}ENTER THE NUMBER OF REACTIONS: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return
    max_workers = 15
    reactions_count = 0
    total_successful_reactions = 0
    results = []
    tokens_used = 0
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}FAILED TO REACT!")
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}TOTAL SUCCESSFULLY REACTIONS: {total_successful_reactions}")

def perform_reaction(token, uid_url, reaction_type):
    access_token = token.split('|')[1]
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()
    }
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def live_react():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    print(f" {white}FORMAT : {red}https://www.facebook.com/100078043222260/video/110105688267538/")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    z = input(f" {white}ENTER THE POST LINK OR ID: ")
    post_id = get_combined_data(z)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id
    print(f"     {yellow}[01] {blue}LIKE")
    print(f"     {yellow}[02] {blue}LOVE")
    print(f"     {yellow}[03] {blue}WOW")
    print(f"     {yellow}[04] {blue}SAD")
    print(f"     {yellow}[05] {blue}ANGRY")
    print(f"     {yellow}[06] {blue}HAHA")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        reaction_choice = int(input(f"{white} CHOOSE : ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_reactions = int(input(f" {yellow}ENTER THE NUMBER OF REACTIONS: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return
    max_workers = 10
    reactions_count = 0
    total_successful_reactions = 0
    results = []
    tokens_used = 0
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        pass
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}TOTAL SUCCESSFULLY REACTIONS : {total_successful_reactions}")

def vid():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]  # Ensure no empty lines
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    print(f" {white}FORMAT : {red}https://www.facebook.com/100078043222260/video/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    z = input(f" {white}ENTER THE POST LINK OR ID: ")
    post_id = get_combined_data(z)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id
    print(f"     {yellow}[01] {blue}LIKE")
    print(f"     {yellow}[02] {blue}LOVE")
    print(f"     {yellow}[03] {blue}WOW")
    print(f"     {yellow}[04] {blue}SAD")
    print(f"     {yellow}[05] {blue}ANGRY")
    print(f"     {yellow}[06] {blue}HAHA")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        reaction_choice = int(input(f"{white} CHOOSE : ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_reactions = int(input(f" {yellow}ENTER THE NUMBER OF REACTIONS: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return
    max_workers = 10
    reactions_count = 0
    total_successful_reactions = 0
    results = []
    tokens_used = 0
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        pass
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}TOTAL SUCCESSFULLY REACTIONS : {total_successful_reactions}")

def extract_reel_id(link):
    pattern = r'/reel/(\d+)'
    match = re.search(pattern, link)
    if match:
        return match.group(1)
    else:
        return None

def react_comment(token, uid_url, reaction_type, reactions_count):
    access_token = token.split('|')[1]
    url = f'https://graph.facebook.com/v18.0/{uid_url}/reactions'
    params = {
        'access_token': access_token,
        'type': reaction_type
    }
    headers_ = {
        'User-Agent': W_ueragnt()
    }
    try:
        response = requests.post(url, params=params, headers=headers_)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def comment_react():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    print(f" {white}FORMAT : {red}https://www.facebook.com/100078043222260/posts/541319968479439/?mibextid=rS40aB7S9Ucbxw6v")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    post_id = input(f" {white}ENTER THE POST LINK OR ID: ")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    comment_id = input(f" {white}COMMENT ID: ")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    uid_url = f"{post_id}_{comment_id}"
    print(f"     {yellow}[01] {blue}LIKE")
    print(f"     {yellow}[02] {blue}LOVE")
    print(f"     {yellow}[03] {blue}WOW")
    print(f"     {yellow}[04] {blue}SAD")
    print(f"     {yellow}[05] {blue}ANGRY")
    print(f"     {yellow}[06] {blue}HAHA")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        reaction_choice = int(input(f"{white} CHOOSE : ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_reactions = int(input(f" {yellow}ENTER THE NUMBER OF REACTIONS: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return
    if num_reactions > len(tokens):
        print(f" {red}ENTER AGAIN NOT EXCEEDING {len(tokens)}")
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        return
    reactions_count = 0
    failed_reactions = 0
    target_reactions = num_reactions
    remaining_tokens = tokens[:num_reactions]
    max_workers = 20
    results = []
    while reactions_count < target_reactions and remaining_tokens:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(react_comment, token, uid_url, reaction_type, reactions_count): token for token in remaining_tokens}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED TO COMMENT!")
                    else:
                        failed_reactions += 1
                        pass
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
        remaining_tokens = [token for token in remaining_tokens if token not in future_to_token]
        if failed_reactions > 0:
            print(f" {red}Retrying failed reactions...{blue}")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}TOTAL SUCCESSFULLY REACTED: {reactions_count}")

def perform_reaction(token, uid_url, reaction_type):
    access_token = token.split('|')[1]
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()
    }
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def perform_reaction_fast():
	   
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    print(f" {white}FORMAT : {red}https://www.facebook.com/100078043222260/posts/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    z = input(f" {white}ENTER THE POST LINK OR ID: ")
    post_id = get_combined_data(z)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id
    print(f"     {yellow}[01] {blue}LIKE")
    print(f"     {yellow}[02] {blue}LOVE")
    print(f"     {yellow}[03] {blue}WOW")
    print(f"     {yellow}[04] {blue}SAD")
    print(f"     {yellow}[05] {blue}ANGRY")
    print(f"     {yellow}[06] {blue}HAHA")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        reaction_choice = int(input(f"{white} CHOOSE : ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_reactions = int(input(f" {yellow}ENTER THE NUMBER OF REACTIONS: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return
    max_workers = 10
    reactions_count = 0
    total_successful_reactions = 0
    results = []
    tokens_used = 0
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        pass
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}TOTAL SUCCESSFULLY REACTIONS : {total_successful_reactions}")

def perform_reaction(token, uid_url, reaction_type):
    access_token = token.split('|')[1]
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()
    }
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def reels():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    print(f" {white}FORMAT : {red}https://www.facebook.com/reel/26674343208847358?mibextid=rS40aB7S9Ucbxw6v")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    z = input(f" {white}ENTER THE POST LINK OR ID: ")
    post_id = get_combined_data(z)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id
    print(f"     {yellow}[01] {blue}LIKE")
    print(f"     {yellow}[02] {blue}LOVE")
    print(f"     {yellow}[03] {blue}WOW")
    print(f"     {yellow}[04] {blue}SAD")
    print(f"     {yellow}[05] {blue}ANGRY")
    print(f"     {yellow}[06] {blue}HAHA")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        reaction_choice = int(input(f"{white} CHOOSE : ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_reactions = int(input(f" {yellow}ENTER THE NUMBER OF REACTIONS: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return
    max_workers = 10
    reactions_count = 0
    total_successful_reactions = 0
    results = []
    tokens_used = 0
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        pass
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}TOTAL SUCCESSFULLY REACTIONS : {total_successful_reactions}")

def extract_user_id_prof(url):
    pattern = r'id=(\d+)|profile\.php\?id=(\d+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1) or match.group(2)
    return None

def follow_account(page_access_token, account_id):
    headers_ = {
        'User-Agent': W_ueragnt()
    }
    headers = {
        'Authorization': f'Bearer {page_access_token}',
        **headers_ 
    }
    try:
        response = requests.post(
            f'https://graph.facebook.com/v18.0/{account_id}/subscribers',
            headers=headers
        )
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Request failed for token {page_access_token}: {e}")
        return False

def auto_follow_fast():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    file_choice = int(input(f"{white} CHOOSE : ").strip())
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    file_path = file_options.get(file_choice)
    if not file_path:
        print("Invalid choice.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    if len(tokens) == 0:
        print("No tokens found in the selected file.")
        return
    start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {tokens}{red}]: "))
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    tokens = tokens[start_line - 1:]
    account_id = extract_user_id_prof(input(f" {white}ENTER THE TARGET ACCOUNT URL: "))
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    if not account_id:
        print(f"Invalid account ID.")
        return
    try:
        follow_limit = int(input(f' {yellow}LIMIT: '))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print("Invalid number for follow limit.")
        return
    follow_count = 0
    failed_count = 0
    current_index = 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        while follow_count < follow_limit and current_index < len(tokens):
            token = tokens[current_index]
            page_access_token = token.split('|')[1]
            uid = token.split('|')[0]
            future = executor.submit(follow_account, page_access_token, account_id)
            success = future.result()
            if success:
                follow_count += 1
                print(f"     {green}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY FOLLOWED!")
            else:
                failed_count += 1
                print(f"   {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}FAILED TO FOLLOW!")
            current_index += 1
            if current_index >= len(tokens) and follow_count < follow_limit:
                pass
                current_index = 0
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f' {green}TOTAL SUCCESSFULLY FOLLOW : {follow_count}')

def extract_fbid_dp(url):
    pattern = r'fbid=(\d+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None  

def perform_reaction(token, uid_url, reaction_type):
    access_token = token.split('|')[1]
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    try:
        response = requests.post(auto_react)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def perform_reaction_fast_dp():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]  
    print(f" {white}FORMAT : {red}https://www.facebook.com/photo.php?fbid=541361691808600")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    z = input(f" {white}ENTER THE POST LINK OR ID: ")
    post_id = get_combined_data(z)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id
    print(f"     {yellow}[01] {blue}LIKE")
    print(f"     {yellow}[02] {blue}LOVE")
    print(f"     {yellow}[03] {blue}WOW")
    print(f"     {yellow}[04] {blue}SAD")
    print(f"     {yellow}[05] {blue}ANGRY")
    print(f"     {yellow}[06] {blue}HAHA")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        reaction_choice = int(input(f"{white} CHOOSE : ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_reactions = int(input(f" {yellow}ENTER THE NUMBER OF REACTIONS: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return
    if num_reactions > len(tokens):
        print(f" {red}ENTER AGAIN NOT EXCEEDING {len(tokens)}")
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        return
    reactions_count = 0
    max_workers = 10
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens[:num_reactions]}
        while reactions_count < num_reactions:
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        pass
                    if reactions_count >= num_reactions:
                        print(f" {green}SUCCESSFULLY REACHED {reactions_count} REACTIONS! EXITING...")
                        return
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
            remaining_tokens = tokens[num_reactions: num_reactions + 5]
            if remaining_tokens:
                future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in remaining_tokens}
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}TOTAL SUCCESSFULLY REACTIONS : {reactions_count}")

def rep(post_id, comment, access_token):
    if '|' in access_token:
        _, access_token = access_token.split('|', 1)
    if not access_token.startswith(("EA", "EAA")):
        return f"Invalid token: {access_token}"
    try:
        converted_link = post_id
        auto_comment_url = f'https://graph.facebook.com/v13.0/{converted_link}/comments'
        params = {
            'message': comment,
            'access_token': access_token
        }
        time.sleep(1)
        headers = {
            'user-agent': W_ueragnt()
        }
        response = requests.post(auto_comment_url, params=params, headers=headers)
        if response.status_code == 200:
            return f"\033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY COMMENTED: {green}{comment}\033[1;32m"
        else:
            return f"\033[1;31m[FAILED]\033[1;31m FAILED TO COMMENT: {green}{comment} "
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"

def reply():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    a = input(f" {white}ENTER THE POST ID: ")
    b = input(f" {white}ENTER THE COMMENT ID: ")
    result = f"{a}_{b}"
    post_id = result
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_comments = int(input(f" {red}ENTER THE NUMBER OF COMMENTS: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if num_comments <= 0:
            print("Number of comments must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    comments_list = []
    for i in range(num_comments):
        comment = input(f" {white}ENTER COMMENT {i + 1}: ")
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        comments_list.append(comment)
    try:
        num_accounts = int(input(f" {yellow}ENTER THE NUMBER OF ACCOUNTS TO USE FOR COMMENTING {red}[1 to {len(tokens)}{red}]: "))
        if num_accounts > len(tokens) or num_accounts <= 0:
            print(f"Please enter a valid number between 1 and {len(tokens)}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    results = []
    comments_count = 0
    max_workers = 10
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {}
        for i, token in enumerate(tokens[:num_accounts]):
            comment = random.choice(comments_list)
            future = executor.submit(rep, post_id, comment, token)
            future_to_token[future] = token
        for future in as_completed(future_to_token):
            try:
                result = future.result()
                print(result)
                if "SUCCESSFULLY" in result:
                    comments_count += 1
            except Exception as e:
                print(f"Error processing token: {e}")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}TOTAL COMMENTS MADE: {comments_count}")

def comment_with_token(post_id, comment, access_token):
    if '|' in access_token:
        _, access_token = access_token.split('|', 1)
    if not access_token.startswith(("EA", "EAA")):
        return f"Invalid token: {access_token}"
    try:
        converted_link = post_id
        auto_comment_url = f'https://graph.facebook.com/v13.0/{converted_link}/comments'
        params = {
            'message': comment,
            'access_token': access_token
        }
        time.sleep(1)
        headers = {
            'user-agent': W_ueragnt()
        }
        response = requests.post(auto_comment_url, params=params, headers=headers)
        pass
        if response.status_code == 200:
            return f"\033[1;31m[SUCCESS]\033[1;31m \033[1;32mSUCCESSFULLY COMMENTED: {green}{comment}\033[1;32m"
        else:
            pass
    except requests.exceptions.RequestException as e:
        pass

def perform_comment_fast():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        pass
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    a = input(f" {white}ENTER THE POST ID: ")
    post_id = get_combined_data(a)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_comments = int(input(f" {red}ENTER THE NUMBER OF COMMENTS: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if num_comments <= 0:
            print("Number of comments must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    comments_list = []
    for i in range(num_comments):
        comment = input(f" {white}ENTER COMMENT {i + 1}: ")
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        comments_list.append(comment)
    try:
        num_accounts = int(input(f" {white}ENTER THE NUMBER OF ACCOUNTS TO SUCCESSFULLY COMMENT {red}[1 to {len(tokens)}{red}]: "))
        if num_accounts > len(tokens) or num_accounts <= 0:
            print(f"Please enter a valid number between 1 and {len(tokens)}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    successful_comments = 0
    max_workers =  2
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        while successful_comments < num_accounts and tokens:
            token = tokens.pop(0)
            comment = random.choice(comments_list)
            future = executor.submit(comment_with_token, post_id, comment, token)
            try:
                result = future.result()
                print(result)
                if "SUCCESSFULLY" in result:
                    successful_comments += 1
                    print(f"{successful_comments}/{num_accounts} COMMENTS SUCCESSFULLY.")
            except Exception as e:
                pass
    if successful_comments == num_accounts:
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print(f" {green}ALL {num_accounts} COMMENTS WERE SUCCESSFULLY MADE!")
    else:
        print(f"ONLY {successful_comments}/{num_accounts} COMMENTS WERE SUCCESSFULLY. NO MORE TOKENS AVAILABLE.")

def live_comment():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    a = input(f" {white}ENTER THE POST ID: ")
    post_id = get_combined_data(a)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_comments = int(input(f" {red}ENTER THE NUMBER OF COMMENTS: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if num_comments <= 0:
            print("Number of comments must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    comments_list = []
    for i in range(num_comments):
        comment = input(f" {white}ENTER COMMENT {i + 1}: ")
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        comments_list.append(comment)
    try:
        num_accounts = int(input(f" {yellow}ENTER THE NUMBER OF ACCOUNTS TO USE FOR COMMENTING {red}[1 TO {len(tokens)}{red}]: "))
        if num_accounts > len(tokens) or num_accounts <= 0:
            print(f"Please enter a valid number between 1 and {len(tokens)}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    results = []
    comments_count = 0
    max_workers = 2
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {}
        for i, token in enumerate(tokens[:num_accounts]):
            comment = random.choice(comments_list)
            future = executor.submit(comment_with_token, post_id, comment, token)
            future_to_token[future] = token
        for future in as_completed(future_to_token):
            try:
                result = future.result()
                print(result)
                if "SUCCESSFULLY" in result:
                    comments_count += 1
            except Exception as e:
                print(f"Error processing token: {e}")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}TOTAL COMMENTS MADE: {comments_count}")

def load_tokens(file_path):
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
        return tokens
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return []

def follow_and_like_facebook_page(uid, access_token):
    follow_url = f"https://graph.facebook.com/v20.0/{uid}/subscribers"
    headers = {'Authorization': f'Bearer {access_token}'}
    follow_response = make_http_request('POST', follow_url, headers=headers)
    if follow_response and 'error' in follow_response:
        print(f"Error following page with UID {uid}: {follow_response['error']['message']}")
    elif follow_response:
        print(f"\033[1;32m[SUCCESSFULLY] FOLLOWED the page/profile with UID {uid}\033[0m")
    like_url = f"https://graph.facebook.com/v20.0/{uid}/likes"
    like_response = make_http_request('POST', like_url, headers=headers)
    if like_response and 'error' in like_response:
        print(f"Error liking page with UID {uid}: {like_response['error']['message']}")
    else:
        print(f"\033[1;32m[SUCCESSFULLY] LIKED the page/profile with UID {uid}\033[0m")

def make_http_request(method, url, headers=None, data=None):
    try:
        if method.upper() == 'POST':
            response = requests.post(url, headers=headers, data=data)
        elif method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        else:
            print(f"Unsupported HTTP method: {method}")
            return None
        if response.status_code == 200:
            return response.json()
        else:
            print(f"HTTP request failed with status code: {response.status_code}")
            return response.json()
    except Exception as e:
        print(f"An error occurred during the HTTP request: {str(e)}")
        return None

def perform_actions_from_file():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = load_tokens(file_path)
    total_tokens = len(tokens)
    if total_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {total_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > total_tokens:
            print(f"Please enter a valid line number between 1 and {total_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    uid = input(f" {white}ENTER THE PAGE/PROFILE UID: ").strip()
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    if not uid.isdigit():
        print("Invalid UID. Please ensure you entered a correct numeric UID.")
        return
    try:
        num_actions = int(input(f" {yellow}LIMIT {red}NOT EXCEEDING {total_tokens}{red}]: ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if num_actions > total_tokens:
            print(f"It exceeds the limit of {total_tokens}.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number for the actions.")
        return
    action_count = 0
    tasks = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        for token in tokens[:num_actions]:
            future = executor.submit(follow_and_like_facebook_page, uid, token.split('|')[1])
            tasks.append(future)
            action_count += 1
        for task in as_completed(tasks):
            y = token.split('|')[0]
            try:
                task.result()
            except Exception as e:
                print(f"An error occurred during execution: {str(e)}")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}ID : {y} | SUCCESSFULLY FOLLOWED AND LIKED | ID:", uid)
    print(f" {green}COMPLETED {action_count} REQUESTED ACTIONS.")

gome_token = []

def tokz(input_cookies):
    for cookie in input_cookies:
        header_ = {
            'authority': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        try:
            home_business = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = home_business.split('EAAG')[1].split('","')[0]
            cookie_token = f'{cookie}|EAAG{token}'
            gome_token.append(cookie_token)
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie = tach.split('|')[0]
    token = tach.split('|')[1]
    he = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'cookie': cookie,
        'host': 'graph.facebook.com'
    }
    try:
        requests.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}', headers=he).json()
    except:
        pass

def get_file_path():
    clear_screen()
    ethan()
    return input(f" {white}[ENTER PATH TO FILE WITH EMAIL AND PASSWORD]: ")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")

def get_cookie_storage_path():
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    return input(f" {white}[ENTER PATH TO STORE COOKIES]: ")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")

def read_credentials(file_path):
    credentials = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip()
            if '|' in line:
                uid, password = line.split('|', 1)
                credentials.append((uid.strip(), password.strip()))
            elif line:
                print(f"Warning: Skipping invalid line format: {line}")
    except FileNotFoundError as e:
        print(f"Error: File not found {file_path}: {str(e)}")
    return credentials

def cuser(user, passw):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'cpl': 'true',
        'family_device_id': str(uuid.uuid4()),
        'credentials_type': 'device_based_login_password',
        'email': user,
        'password': passw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'method': 'auth.login',
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
    }
    response = pt("https://b-graph.facebook.com/auth/login", headers=headers, data=data, allow_redirects=False)
    return response.json()

def runing():
    clear_screen()
    ethan()
    file_path = get_file_path()
    storage_path = get_cookie_storage_path()
    credentials = read_credentials(file_path)
    if not credentials:
        print(f" {red}NO CREDENTIALS FOUND IN THE FILE.")
        return
    print(f" {red}FOUND {len(credentials)} {green}CREDENTIALS !...")
    for user, passw in credentials:
        response = cuser(user, passw)
        if "session_key" in response:
            cookie_str = '; '.join(f'{i["name"]}={i["value"]}' for i in response.get('session_cookies', []))
            print(f" {white}COOKIE : {green}{cookie_str}")
            with open(storage_path, 'a') as f:
                f.write(cookie_str + '\n')
        else:
            print(f" {red}INVALID/CHECKPOINT FOR USER ID: {user}")
    print(f" {green}PROCESSING COMPLETE ALL CREDENTIALS HAVE BEEN PROCESSED.")

def bitz():
    clear_screen()
    ethan()
    print(f"     {yellow}[1] {blue}GET COOKIE")
    print(f"     {yellow}[2] {blue}AUTO CREATE PAGE")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    choice = int(input(f"{white} CHOOSE : ").strip())
    if choice == '1':
        runing()
    if choice == '2':
        hackezr()

init()

class RegPro5:
    def __init__(self, cookies) -> None:
        self.cookies = cookies
        self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'cookie': self.cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
        }
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        profile = requests.get(url_profile, headers=headers).text
        self.fb_dtsg = None
        patterns = [
            '{"name":"fb_dtsg","value":"',
            ',"f":"',
        ]
        for pattern in patterns:
            try:
                self.fb_dtsg = profile.split(pattern)[1].split('"},')[0]
                break
            except IndexError:
                continue
        if not self.fb_dtsg:
            kolor("Error: fb_dtsg not found in profile data.", 'red')

def get_token_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        tokens = [line.strip().split('|')[1] for line in lines if '|' in line]
    return random.choice(tokens)

class FacebookPoster:
    def __init__(self, link):
        self.link = link

    def share_post(self, token):
        url = "https://graph.facebook.com/v13.0/me/feed"
        payload = {
            'link': self.link,
            'published': '0',
            'privacy': '{"value":"SELF"}',
            'access_token': token
        }
        try:
            response = requests.post(url, data=payload)
            uid = response.json().get('id')
            if response.status_code == 200:
                print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY SHARED!")
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return False

def share_in_threads(link, file_path, num_shares):
    start_all = time.time()
    
    def worker():
        success = False
        while not success:
            token = get_token_from_file(file_path)
            fb_poster = FacebookPoster(link)
            success = fb_poster.share_post(token)
    max_workers = 40
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for _ in range(num_shares):
            executor.submit(worker)
    end_all = time.time()
    duration = end_all - start_all
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {yellow}SHARING STARTED: {start_all}")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {yellow}SHARING ENDED: {end_all}")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {yellow}TOTAL DURATION: {duration:.2f} SECONDS\033[0m")

def count_tokens(accounts_file, pages_file):
    total_accounts = 0
    total_pages = 0
    try:
        with open(accounts_file, 'r') as af:
            total_accounts = sum(1 for line in af if line.strip())  # Count non-empty lines
    except FileNotFoundError:
        print(f"Account file not found: {accounts_file}")
    try:
        with open(pages_file, 'r') as pf:
            total_pages = sum(1 for line in pf if line.strip())  # Count non-empty lines
    except FileNotFoundError:
        print(f"Page file not found: {pages_file}")
    return total_accounts, total_pages

def share():
    clear_screen()
    ethan()
    colorful_loading()
    file_map = {
        '1': '/sdcard/boostphere/FRAACCOUNT.txt',
        '2': '/sdcard/boostphere/FRAPAGES.txt',
        '3': '/sdcard/boostphere/RPWACCOUNT.txt',
        '4': '/sdcard/boostphere/RPWACCOUNT.txt'
    }
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"{white} CHOOSE : ").strip()
    file_path = file_map.get(choice)
    if not file_path:
        print("Invalid choice. Exiting.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    post_id = input(f" {white}ENTER THE POST ID TO SHARE: ")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    num_shares = int(input(f" {yellow}LIMIT: "))
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    link = f"https://www.facebook.com/{post_id}"
    share_in_threads(link, file_path, num_shares)

def main2(): 
    fraaccounts_file = '/sdcard/boostphere/FRAACCOUNT.txt'
    frapages_file = '/sdcard/boostphere/FRAPAGES.txt'
    rpwaccounts = '/sdcard/boostphere/RPWACCOUNT.txt'
    rpwpages = '/sdcard/boostphere/RPWPAGES.txt'
    total_accounts, total_pages = count_tokens(fraaccounts_file, frapages_file)
    total_account_rpw, total_pages_rpw = count_tokens(rpwaccounts,rpwpages)
    clear_screen()
    ethan()
    print(f"""               {Q7}CHOOSE HERE
 {Q7}─────────────────────────────────────────────────────────────────\033[0m
                            {Q7}FRA ACCOUNT{yellow} : {green}{total_accounts}
                            {Q7}FRA PAGES  {yellow} : {green}{total_pages}
                            {Q7}RPW ACCOUNT{yellow} : {green}{total_account_rpw}
                            {Q7}RPW PAGES  {yellow} : {green}{total_pages_rpw}
 {Q7}─────────────────────────────────────────────────────────────────\033[0m""")
    print(f"     {yellow}[1] {blue}EXTRACT ACCOUNT")
    print(f"     {yellow}[2] {blue}AUTO SHARE")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"{white} CHOOSE : ").strip()
    if choice == '1': 
        extraction()
    if choice == '2': 
        share()

    def reg(self, name):
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }
        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            '__a': '1',
            '__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo',
            '__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u',
            '__req': 't',
            '__hs': '19296.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1006496476',
            '__s': '1gapab:y4xv3f:2hb4os',
            '__hsi': '7160573037096492689',
            '__comet_req': '15',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': '25404',
            'lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
            '__aaid': '800444344545377',
            '__spin_r': '1006496476',
            '__spin_b': 'trunk',
            '__spin_t': '1667200829',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
            'variables': '{"input":{"bio":"","categories":["181475575221097"],"creation_source":"comet","name":"' + name + '","page_referrer":"launch_point","actor_id":"' + self.id_acc + '","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825',
        }
        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
        try:
            result = response.json()
            if 'id' in result:
                page_id = result['id']
                self.set_profile_picture(page_id)
            return result
        except:
            return response.text

    def set_profile_picture(self, page_id):
        picture_path = "/home/spade/Desktop/load data/Profile.jpeg"  # Replace with your actual path to the profile picture
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': f'https://www.facebook.com/{page_id}',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'ProfilePicUpload',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }
        files = {
            'source': (os.path.basename(picture_path), open(picture_path, 'rb'), 'image/jpeg')
        }
        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            'profile_id': page_id,
            'fb_dtsg': self.fb_dtsg,
            'photo_source': '4',
            'composer_entry_time': '0',
            'composer_session_id': 'abc',
            'ref': 'timeline',
            'upload_id': 'profile_pic',
            'upload_type': 'profile',
        }
        response = requests.post('https://www.facebook.com/photos/upload', headers=headers, files=files, data=data)
        try:
            return response.json()
        except:
            return response.text

def kolor(text, color):
    if color == 'green':
        print(Fore.GREEN + text + Style.RESET_ALL)
    elif color == 'red':
        print(Fore.RED + text + Style.RESET_ALL)
    else:
        print(text)

def get_cookies_file_path():
    clear_screen()
    ethan()
    colorful_loading()
    return input(" ENTER THE PATH TO THE COOKIES.TXT FILE: ")

def hackezr():
    cookies_file = get_cookies_file_path()
    try:
        with open(cookies_file, 'r') as f:
            cookies_list = f.readlines()
    except FileNotFoundError:
        kolor("Error: File not found. Please check the path.", 'red')
        return
    for cookie_line in cookies_list:
        cookie_line = cookie_line.strip()
        cookies = cookie_line
        vietnamese_names = [
"MrsTexasUNIVERSE Dr.MeenakshiRavi",
"Melanii",
"Israt Jahan",
"Md Rubel Kahan",
"Mariya Akthr Sathi",
"Israt Xahan Esha",
"Younietha Wasilah",
"Nusaiba Islam Eva",
"Lx Zoya",
"Tasnia Rahman",
"Mehedi Hasan",
"Roja Islam",
"Esme Johnston",
"Riya Jahan",
"Sinthiya Chowdhury",
"Jannatul Ferdos",
"Aysha Jannat",
"Moinul Islam Shanto",
"Tanveer Rahman",
"Rosabel Mercado Oaing",
"Bnegali Basi",
"Ashlie Allaisa",
"Rapk Miah",
"Saima Akter",
"Md Minar",
"Tahmina Jannat Mim",
"Humaryra Bin Allbihi",
"Sadiya Akter",
"MD Naeem",
"Foysol Khan",
"Md Robiul Sheikh",
"Md Sohel",
"Alex Hels Afridy",
"Ocena Manus",
"Shohag Sheikh",
"Gojo Saturo",
"Shaddat Khan",
"MD Mithun",
"Rakib Ahmmed Foysal",
"Md Oliull Sheikh",
"Md Sabbir Shaike",
"Sk Tushar",
"Vagne Dev",
"MB �m�m",
"Limon Sehk Limon Sehk",
"Md Milan",
"Reyad Islam",
"Md Shobuzpra",
"Md Masum Islam",
"Tanzim Rabby",
"R�bin Here",
"MD Sumon MD Sumon",
"Asif Khan",
"Mis Afia",
"���m�l H�q��",
"Md Shakib Mridha",
"Urzzal Mia",
"Samuel Ramirez",
"Shaddat Khan",
"Shaheen Kanaipur",
"MD Salman Sak",
"MD Amirol",
"Mahedi Islam",
"MD Alhassan Hawlder",
"Anis Osim",
"Raihan Islam",
"Hamida Forid Pur",
"MD Sohel Sheikh",
"Md Emram",
"Md Nijam Uddin Sheikh",
"MD Biplob",
"Md Moyazzem",
"Md Azad",
"BA DH ON",
"Md Rezaul Rezaul",
"Tanjin Molla",
"Md Sumon",
"Obaidul Krim",
"Rabby Khan",
"Jahangir Gazi",
"Md. Tamim",
"Najir Sheikh",
"Abu Bakar Khan",
"Md Alamin",
"Sgush Rsuhe",
"Rabby Sheikh",
        ]
        random_name = random.choice(vietnamese_names)
        reg_instance = RegPro5(cookies)
        result = reg_instance.reg(random_name)
        if 'error' not in result:
            kolor(f"     {green}[SUCCESS] {red}Created Page", 'green')
        else:
            kolor(f"     {red}[UNSUCCESSFUL] {green}Created Page", 'red')

class Color:
    END = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    
def pzl(username, passwords):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
    for password in passwords:
        data = {
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
            'email': username,
            'password': password,
            'access_token': accessToken
        }
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            responses = response.json()
            if 'access_token' in responses:
                return responses['access_token'], True
            else:
                error_msg = responses.get('error_msg', 'Unknown error')
                print(f"{Color.RED}Error for {username}: {error_msg}{Color.END}")
        except requests.exceptions.RequestException as e:
            print(f"{Color.RED}Error for {username}: {str(e)}{Color.END}")
    return None, False

def sav(tokens_array, token_file_path):
    with open(token_file_path, 'w') as file:
        for token_info in tokens_array:
            uid = token_info['email']
            access_token = token_info['access_token']
            file.write(f"{uid}|{access_token}\n")

def prz(file_path, tokens_array):
    if not os.path.isfile(file_path):
        print(f" {Color.BOLD}File {file_path} does not exist.{Color.END}")
        return
    print(f" {Color.BOLD}Processing file: {file_path}{Color.END}")
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if not lines:
        print(f" {Color.BOLD}File {file_path} is empty.{Color.END}")
        return
    account_pairs = [line.strip() for line in lines if '|' in line]
    if not account_pairs:
        print(f" {Color.BOLD}No valid uid|pass pairs found in {file_path}.{Color.END}")
        return
    for account in account_pairs:
        uid, password = account.split('|')
        pass
        token, success = pzl(uid, [password])
        if success:
            tokens_array.append({"email": uid, "access_token": token})
            print(f" {Color.GREEN}SUCCESSFULLY EXTRACTED TOKEN FOR {uid}{Color.END}")
        else:
            print(f" {Color.BOLD}FAILED TO GET TOKEN FOR {uid}.{Color.END}")

def maz():
    clear_screen()
    ethan()
    colorful_loading()
    file_path = input(f" {Color.YELLOW}ENTER THE PATH OF THE TEXT FILE WITH ACCOUNTS AND PASSWORDS: {Color.END}").strip()
    token_file_path = input(f" {Color.YELLOW}ENTER THE PATH OF THE FILE WHERE TOKENS SHOULD BE STORED: {Color.END}").strip()
    tokens_array = []
    prz(file_path, tokens_array)
    if tokens_array:
        pass
        for token_info in tokens_array:
            pass
        sav(tokens_array, token_file_path)
    else:
        print(f" {Color.BOLD}NO TOKENS COLLECTED.{Color.END}")
    print(f" {Color.BLUE}EXITING THE PROGRAM...{Color.END}")

def start():
    clear_screen()
    ethan()
    colorful_loading()
    token_file_path = input("ENTER THE PATH TO THE FILE CONTAINING THE TOKENS: ").strip()
    tokens = rad(token_file_path)
    if not tokens:
        print("No tokens found. Exiting.")
        return
    if not os.path.exists(DIRECTORY):
        print(f"Error: Directory '{DIRECTORY}' does not exist.")
        return
    files_in_directory = os.listdir(DIRECTORY)
    if not files_in_directory:
        print(f"Error: No files found in directory '{DIRECTORY}'.")
        return
    for user_token in tokens:
        pages = pigzs(user_token)
        if not pages:
            print(f"No pages found for token {user_token}. Skipping.")
            continue
        for page in pages:
            pass
            page_id = page['id']
            page_access_token = page.get('access_token')
            if not page_access_token:
                print(f"No access token found for page {page_id}. Skipping.")
                continue
            if pec(page_id):
                pass
                continue
            file_name = random.choice(files_in_directory)
            file_path = os.path.join(DIRECTORY, file_name)
            result = plod(page_id, page_access_token, file_path)
            print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
            print(f" {green}SUCCESSFULLY UPLOADED PROFILE PICTURE {page['name']} ──────> {page['id']} ")
            print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
            time.sleep(2)
            
BASE_URL = 'https://graph.facebook.com/v18.0'
DIRECTORY = 'Picture'

def pigzs(access_token):
    url = f'{BASE_URL}/me/accounts'
    params = {
        'access_token': access_token
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Error getting pages for token {access_token}: {str(e)}")
        return []

def pec(page_id):
    url = f'{BASE_URL}/{page_id}?fields=picture'
    try:
        response = requests.get(url)
        response.raise_for_status()
        picture_data = response.json().get('picture', {})
        return 'data' in picture_data and 'url' in picture_data['data']
    except requests.exceptions.RequestException as e:
        print(f"Error checking profile picture for page {page_id}: {str(e)}")
        return False

def plod(page_id, page_access_token, file_path):
    try:
        with open(file_path, 'rb') as file:
            files = {
                'source': file
            }
            data = {
                'access_token': page_access_token
            }
            url = f'{BASE_URL}/{page_id}/picture'
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error uploading profile picture to page {page_id}: {str(e)}")
        return {'error': str(e)}
    except FileNotFoundError as e:
        print(f"Error: File not found {file_path}: {str(e)}")
        return {'error': str(e)}

def rad(file_path):
    tokens = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if '|' in line:
                    uid, token = line.split('|', 1)
                    tokens.append((uid.strip(), token.strip()))
    except FileNotFoundError as e:
        print(f"Error: Tokens file not found {file_path}: {str(e)}")
    return tokens

def mainzsa():
    clear_screen()
    ethan()
    print(f"     {yellow}[1] {blue}GET TOKEN")
    print(f"     {yellow}[2] {blue}SET PFP")
    print("\033[1;37m───────────────────────────────────────────────────────────────\033")
    choice = input(f"{white} CHOOSE : ").strip()
    if choice == '1':
        maz()
    if choice == '2':
        start()
    else: 
        print("invalid po")

CODE_FILE = '/sdcard/boostphere/generated_code.txt'  # File to store the generated code

def ensure_file_exists():
    open(CODE_FILE, 'a').write('')

def generate_code():
    prefix = "KLEINBOOSTING"
    number_part = ''.join(random.choices(string.digits, k=3))
    letters_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    code = f"{prefix}-{number_part}-{letters_part}"
    return code

def save_code(code):
    with open(CODE_FILE, 'w') as file:
        file.write(code)

def load_code():
    if os.path.exists(CODE_FILE):
        with open(CODE_FILE, 'r') as file:
            return file.read().strip()
    return None

def is_code_approved(code):
    try:
        response = requests.get("https://raw.githubusercontent.com/ETHANHUILEN/BOOSTINGAPPROVAL/refs/heads/main/Approval.txt")
        response.raise_for_status()
        approved_codes = response.text.splitlines()
        approved_codes = [line.split('#')[0].strip() for line in approved_codes if line]
        return code in approved_codes
    except requests.RequestException as e:
        print(f"Error fetching the approval list: {e}")
        return False

def generate_and_check_code():
    ensure_file_exists()
    code = load_code()
    if code is None or code == '':
        code = generate_code()
        save_code(code)
        clear_screen()
        ethan()
        print(f" {green}YOUR GENERATED CODE: {code}")
    else:
        clear_screen()
        ethan()
        print(f" {green}YOUR CODE : {code}")
    if is_code_approved(code):
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print(f" {green}YOUR KEY HAS BEEN APPROVED !!!")
        time.sleep(3)
        main()
    else:
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print(f" {red}CODE IS NOT APPROVED !")

def get_profile_id(access_token):
    try:
        url = 'https://graph.facebook.com/me'
        params = {'access_token': access_token}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get('id')
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def join_group(group_id, profile_id, access_token):
    try:
        url = f'https://graph.facebook.com/{group_id}/members/{profile_id}'
        params = {'access_token': access_token}
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def val(token):
    validation_url = f"https://graph.facebook.com/debug_token?input_token={token}&access_token={token}"
    response = requests.get(validation_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

token = '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'
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}
file_options = {
    1: "/sdcard/boostphere/FRAACCOUNT.txt",
    2: "/sdcard/boostphere/FRAPAGES.txt",
    3: "/sdcard/boostphere/RPWACCOUNT.txt",
    4: "/sdcard/boostphere/RPWPAGES.txt"
}

def git(repo_owner, repo_name, file_path):
    file_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
    response = requests.get(file_url, headers=headers)
    if response.status_code == 200:
        content = response.json()
        file_sha = content['sha']
        file_content = base64.b64decode(content['content']).decode('utf-8')
        return file_content, file_sha
    elif response.status_code == 404:
        print(f" {red}FAILED")
        return None, None
    else:
        print(f" {red}FAILED")
        return None, None

def contint(repo_owner, repo_name, file_path, file_sha):
    file_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
    empty_content = base64.b64encode(''.encode('utf-8')).decode('utf-8')
    commit_message = f"Clear {file_path}"
    data = {
        "message": commit_message,
        "content": empty_content,
        "sha": file_sha
    }
    response = requests.put(file_url, json=data, headers=headers)
    if response.status_code == 200:
        pass
    else:
        pass

def choose_file_path():
    clear_screen()
    ethan()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    choice = int(input(f"{white} CHOOSE : ").strip())
    if choice == 0:
        print("Exiting the program.")
        exit()
    elif choice in file_options:
        return file_options[choice]
    else:
        print("Invalid choice. Please try again.")
        return choose_file_path()

def cynt(content):
    tokens = content.splitlines()
    return len(tokens)

def count_cookies(cookies_content):
    cookies = cookies_content.splitlines()
    return len(cookies)

def githubtoks():
    clear_screen()
    ethan()
    colorful_loading()
    repo_owner = 'boostphere'
    repo_name = input(f" {yellow}CODE: ")
    tokens_content, tokens_sha = git(repo_owner, repo_name, 'Tokens')
    if tokens_content:
        token_count = cynt(tokens_content)
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print(f" {red}{token_count} {green}TOKENS FOUND !")
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        storage_path = choose_file_path()
        with open(storage_path, 'a') as file:
           file.write(tokens_content + '\n')
        contint(repo_owner, repo_name, 'Tokens', tokens_sha)
    cookies_content, cookies_sha = git(repo_owner, repo_name, 'Cookies')
    if cookies_content:
        cookie_count = count_cookies(cookies_content)
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print(f" {red}{cookie_count} {green}COOKIES FOUND !")
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        cookie_path = input("PATH TO SAVE COOKIES: ")
        with open(cookie_path, 'a') as cookie_file:
            cookie_file.write(cookies_content + '\n')
        contint(repo_owner, repo_name, 'Cookies', cookies_sha)
    else:
        pass

def check():
    clear_screen()
    ethan()
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    choice = int(input(f"{white} CHOOSE : ").strip())
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    if choice in file_options:
        file_path = file_options[choice]
    elif choice == 0:
        print("Exiting...")
        return
    else:
        print("Invalid choice. Exiting...")
        return
    with open(file_path, 'r') as file:
        lines = file.readlines()
    valid_tokens = []
    for line in lines:
        uid, token = line.strip().split('|')
        if val(token):
            valid_tokens.append(line.strip())
            print(f" {green}ACCOUNT ─────> {blue}{uid} {white}= {yellow} IS VALID")
        else:
            print(f" {red}ACCOUNT ─────> {blue}{uid} {white}= {yellow} IS NOT VALID AND WILL BE REMOVED")
    with open(file_path, 'w') as file:
        for valid_token in valid_tokens:
            file.write(valid_token + '\n')

def perform_group_join():
    clear_screen()
    ethan()
    colorful_loading()
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    group_id = input(f" {white}ENTER THE GROUP ID: ")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_tokens = int(input(f" {yellow}LIMIT: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print("Please enter a valid number for tokens.")
        return
    if num_tokens > len(tokens):
        print(f" {red}ERROR: Number exceeds available tokens ({len(tokens)}).")
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        return
    join_count = 0
    failed_count = 0
    retries_left = num_tokens
    max_workers = 10
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {}
        while join_count < num_tokens and retries_left > 0:
            for token in tokens[:retries_left]:
                access_token = token.split('|')[1]
                profile_id = get_profile_id(access_token)
                if profile_id:
                    future = executor.submit(join_group, group_id, profile_id, access_token)
                    future_to_token[future] = token
                else:
                    print(f"\033[1;31m[FAILED] \033[1;37mFailed to retrieve profile ID for token \033[1;33m{token}\033[0m")
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                try:
                    success = future.result()
                    if success:
                        join_count += 1
                        print(f" {green}[SUCCESS] {green}SUCCESSFULLY JOINED GROUP {group_id}")
                    else:
                        failed_count += 1
                        print(f" {red}[UNSUCCESS] {red}FAILED JOINED GROUP {group_id}")
                    if join_count >= num_tokens:
                        break
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
            retries_left = num_tokens - join_count
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print(f"{green}TOTAL SUCCESSFULLY : {join_count}\033[0m")

def live(url):
    parts = url.split('/')
    if len(parts) > 4:
        user_id = parts[3]
        video_id = parts[5]
        return f"{user_id}_{video_id}"
    else:
        return None

def extract_fbid_cover(url):
    pattern = r'fbid=(\d+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None  

def perform_reaction(token, uid_url, reaction_type):
    access_token = token.split('|')[1]
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    try:
        response = requests.post(auto_react)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def perform_reaction_fast_cover():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]  
    print(f" {white}FORMAT : {red}https://www.facebook.com/photo.php?fbid=541361691808600")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    z = input(f" {white}ENTER THE POST LINK OR ID: ")
    post_id = get_combined_data(z)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id
    print(f"     {yellow}[01] {blue}LIKE")
    print(f"     {yellow}[02] {blue}LOVE")
    print(f"     {yellow}[03] {blue}WOW")
    print(f"     {yellow}[04] {blue}SAD")
    print(f"     {yellow}[05] {blue}ANGRY")
    print(f"     {yellow}[06] {blue}HAHA")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        reaction_choice = int(input(f"{white} CHOOSE : ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_reactions = int(input(f" {yellow}ENTER THE NUMBER OF REACTIONS: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return
    if num_reactions > len(tokens):
        print(f" {red}ENTER AGAIN NOT EXCEEDING {len(tokens)}")
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        return
    reactions_count = 0
    max_workers = 10
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens[:num_reactions]}
        while reactions_count < num_reactions:
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                    else:
                        pass
                    if reactions_count >= num_reactions:
                        print(f" {green}SUCCESSFULLY REACHED {reactions_count} REACTIONS! EXITING...")
                        return
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
            remaining_tokens = tokens[num_reactions: num_reactions + 5]
            if remaining_tokens:
                future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in remaining_tokens}
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}TOTAL SUCCESSFULLY REACTIONS : {reactions_count}")

def perform_reaction(token, uid_url, reaction_type):
    access_token = token.split('|')[1]
    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    headers_ = {
        'User-Agent': W_ueragnt()
    }
    try:
        response = requests.post(auto_react, headers=headers_)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def perform_reaction_fastt():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        file_choice = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return
    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return
    try:
        start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {available_tokens}{red}]: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tokens = tokens[start_line - 1:]
    print(f" {white}FORMAT : {red}https://www.facebook.com/100078043222260/posts/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    z = input(f" {white}ENTER THE POST LINK OR ID: ")
    post_id = get_combined_data(z)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    uid_url = post_id
    print(f"     {yellow}[01] {blue}LIKE")
    print(f"     {yellow}[02] {blue}LOVE")
    print(f"     {yellow}[03] {blue}WOW")
    print(f"     {yellow}[04] {blue}SAD")
    print(f"     {yellow}[05] {blue}ANGRY")
    print(f"     {yellow}[06] {blue}HAHA")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        reaction_choice = int(input(f"{white} CHOOSE : ").strip())
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    try:
        num_reactions = int(input(f" {yellow}ENTER THE NUMBER OF REACTIONS: "))
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return
    max_workers = 10
    reactions_count = 0
    total_successful_reactions = 0
    results = []
    tokens_used = 0
    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(perform_reaction, token, uid_url, reaction_type): token for token in tokens_batch}
            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
                    else:
                        pass
                except Exception as e:
                    print(f"Error processing token {token}: {e}")
        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f" {green}TOTAL SUCCESSFULLY REACTIONS : {total_successful_reactions}")

def AutoReact():
    def Reaction(actor_id: str, post_id: str, react: str, token: str):
        rui = requests.Session()
        feedback_id = str(base64.b64encode(('feedback:{}'.format(post_id)).encode('utf-8')).decode('utf-8'))
        var = {
            "input": {
                "feedback_referrer": "native_newsfeed",
                "tracking": [None],
                "feedback_id": feedback_id,
                "client_mutation_id": str(uuid.uuid4()),
                "nectar_module": "newsfeed_ufi",
                "feedback_source": "native_newsfeed",
                "feedback_reaction_id": react,
                "actor_id": actor_id,
                "action_timestamp": str(time.time())[:10]
            }
        }
        data = {
            'access_token': token,
            'method': 'post',
            'pretty': False,
            'format': 'json',
            'server_timestamps': True,
            'locale': 'id_ID',
            'fb_api_req_friendly_name': 'ViewerReactionsMutation',
            'fb_api_caller_class': 'graphservice',
            'client_doc_id': '2857784093518205785115255697',
            'variables': json.dumps(var),
            'fb_api_analytics_tags': ["GraphServices"],
            'client_trace_id': str(uuid.uuid4())
        }
        pos = rui.post('https://graph.facebook.com/graphql', data=data).json()
        try:
            if react == '0':
                print(f"     {red}[REACTOR] {yellow}{actor_id}  {blue}───────> {green}SUCCESSFULLY REMOVED REACTED!")
                return True
            elif react in str(pos):
                print(f"     {red}[REACTOR] {yellow}{actor_id}  {blue}───────> {green}SUCCESSFULLY REACTED!")
                return True
            else:
                print(f"     {red}[REACTOR] {yellow}{actor_id}  {blue}───────> {red}FAILED TO REACT!")
                return False
        except Exception:
            pass
            return False

    def linktradio(post_link: str) -> str:
        patterns = [
            r'/posts/(\w+)',
            r'/videos/(\w+)',
            r'/groups/(\d+)/permalink/(\d+)',
            r'/reels/(\w+)',
            r'/live/(\w+)',
            r'/photos/(\w+)',
            r'/permalink/(\w+)',
            r'story_fbid=(\w+)',
            r'fbid=(\d+)'
        ]
        for pattern in patterns:
            match = re.search(pattern, post_link)
            if match:
                if pattern == r'/groups/(\d+)/permalink/(\d+)':
                    return match.group(2)
                return match.group(1)
        print("Invalid post link or format")
        return None

    def get_ids_tokens(file_path):
        with open(file_path, 'r') as file:
            data = [line.strip().split('|') for line in file]
        return data

    def choose_reaction():
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print(f"     {yellow}[01] {blue}LIKE")
        print(f"     {yellow}[02] {blue}LOVE")
        print(f"     {yellow}[03] {blue}CARE")
        print(f"     {yellow}[04] {blue}WOW")
        print(f"     {yellow}[05] {blue}SAD")
        print(f"     {yellow}[06] {blue}ANGRY")
        print(f"     {yellow}[07] {blue}HAHA")
        print(f"     {yellow}[08] {red}REMOVE REACTION")
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        rec = int(input(f"{white} CHOOSE : ").strip())
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        reaction_ids = {
            1: "1635855486666999",
            2: "1678524932434102",
            3: "613557422527858",
            4: "478547315650144",
            5: "908563459236466",
            6: "444813342392137",
            7: "115940658764963",
            8: "0",
        }
        return reaction_ids.get(rec)
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    ethan()
    colorful_loading()
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    file_choice = int(input(f"{white} CHOOSE : ").strip())
    file_path = file_options.get(file_choice)
    tokens_data = get_ids_tokens(file_path)
    total_tokens = len(tokens_data)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    start_line = int(input(f" {white}ENTER THE STARTING LINE {red}[1 TO {total_tokens}{red}]: "))
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    post_link = input(f" {white}ENTER THE POST LINK OR ID: ")
    post_id = get_combined_data(post_link)
    if not post_id:
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    react_count = int(input(f" {yellow}ENTER THE NUMBER OF REACTIONS: "))
    react = choose_reaction()
    if react == '0':
        remove_count = min(react_count, total_tokens - (start_line - 1))
        reactions_removed = 0
        for actor_id, token in tokens_data[start_line - 1:start_line - 1 + remove_count]:
            success = Reaction(actor_id=actor_id, post_id=post_id, react='0', token=token)
            if success:
                reactions_removed += 1
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print(f" {green}ALL REACTIONS HAVE BEEN SUCCESSFULLY REMOVED! YOU'RE AWESOME {reactions_removed}!")
    elif react:
        send_count = min(react_count, total_tokens - (start_line - 1))
        reactions_sent = 0
        for actor_id, token in tokens_data[start_line - 1:start_line - 1 + send_count]:
            success = Reaction(actor_id=actor_id, post_id=post_id, react=react, token=token)
            if success:
                reactions_sent += 1
        print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
        print(f" {green}ALL REACTIONS HAVE BEEN SUCCESSFULLY SENT! YOU'RE AWESOME {reactions_sent}!")
    else:
        print('Invalid reaction option.')

def buffview(x, thanhphan9, url_str, cookie, fb_dtsg, jazoest):
    time_now = datetime.now().strftime("%H:%M:%S")
    uid_page = list_id_name_page[x].split('|')[0]
    name_page = list_id_name_page[x].split('|')[1]
    list1 = f'i_user={uid_page};'
    cookie9 = f'{cookie}{list1}'
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'origin': 'https://www.facebook.com',
        'referer': url_str,
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'viewport-width': '1186',
        'x-fb-friendly-name': 'storiesUpdateSeenStateMutation',
        'x-fb-lsd': 'YCCQAywyZyd74odVp6QBrw',
        'cookie': cookie9,
    }
    data = {
        'av': uid_page,
        '__user': uid_page,
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'storiesUpdateSeenStateMutation',
        'variables': '{"input":{"bucket_id":"259253279258515","story_id":"'+str(thanhphan9)+'","actor_id":"'+uid_page+'","client_mutation_id":"1"},"scale":1}',
        'server_timestamps': 'true',
        'doc_id': '5127393270671537',
    }
    try:
        requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
        print(f' [{x+1}] | {time_now} | {name_page}')
    except Exception as e:
        pass

def perform_viewfb_fast():
    global list_id_name_page
    list_id_name_page = []
    clear_screen()
    ethan()
    colorful_loading()
    cookie = input(f' {white}COOKIE POLICY PAGE: ')
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    headers = {
        'authority': 'www.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'vi',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'viewport-width': '1366',
        'cookie': cookie,
    }
    try:
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        getdatainfo = requests.get(url_profile, headers=headers).text
    except:
        print(f'{red} COOKIE DIE, PLEASE CHECK AGAIN!')
        return
    try:
        fb_dtsg = getdatainfo.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
        jazoest = getdatainfo.split('{"name":"jazoest","value":"')[1].split('"},')[0]
    except:
        print(f'{red} COOKIE DIE, PLEASE CHECK AGAIN!')
        return
    data = {
        'fb_dtsg': fb_dtsg,
        'jazoest': jazoest,
        'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
        'doc_id': '5300338636681652'
    }
    try:
        res = requests.post('https://www.facebook.com/api/graphql/', headers={'cookie': cookie}, data=data)
        pages = res.json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
        for page in pages:
            uid_page = page['profile']['id']
            name_page = page['profile']['name']
            list_id_name_page.append(f'{uid_page}|{name_page}')
    except Exception as e:
        print(f'{red} Failed to fetch pages: {e}')
        return
    print(f' FOUND {len(list_id_name_page)} PAGES')
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    url_str = input(' {white}ENTER PUBLIC STORY URL: ')
    try:
        thanhphan9 = url_str.split('/')[5].split('/?')[0]
    except:
        print(f"{red} Invalid story URL format.")
        return
    for x in range(len(list_id_name_page)):
        threading.Thread(target=buffview, args=(x, thanhphan9, url_str, cookie, fb_dtsg, jazoest)).start()

def gettokesz(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [line.strip().split('|')[1] for line in lines if '|' in line]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_token():
    clear_screen()
    ethan()
    colorful_loading()
    cookie = input(" ENTER COOKIE ACCOUNT NEED TO GET TOKEN: ")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    session = requests.Session()
    session.cookies.update({'cookie': cookie})
    get_data = session.get("https://www.facebook.com/v2.3/dialog/oauth", params={'redirect_uri': 'fbconnect://success','scope': 'email,publish_actions,publish_pages,user_about_me,user_actions.books,user_actions.music,user_actions.news,user_actions.video,user_activities,user_birthday,user_education_history,user_events,user_games_activity,user_groups,user_hometown,user_interests,user_likes,user_location,user_notes,user_photos,user_questions,user_relationship_details,user_relationships,user_religion_politics,user_status,user_subscriptions,user_videos,user_website,user_work_history,friends_about_me,friends_actions.books,friends_actions.music,friends_actions.news,friends_actions.video,friends_activities,friends_birthday,friends_education_history,friends_events,friends_games_activity,friends_groups,friends_hometown,friends_interests,friends_likes,friends_location,friends_notes,friends_photos,friends_questions,friends_relationship_details,friends_relationships,friends_religion_politics,friends_status,friends_subscriptions,friends_videos,friends_website,friends_work_history,ads_management,create_event,create_note,export_stream,friends_online_presence,manage_friendlists,manage_notifications,manage_pages,photo_upload,publish_stream,read_friendlists,read_insights,read_mailbox,read_page_mailboxes,read_requests,read_stream,rsvp_event,share_item,sms,status_update,user_online_presence,video_upload,xmpp_login','response_type': 'token,code','client_id': '356275264482347'}).text
    fb_dtsg = re.search('DTSGInitData",,{"token":"(.+?)"', get_data.replace('[]', '')).group(1)
    print(fb_dtsg)
    facebook_android = "350685531728"
    facebook_iphone = "6628568379"
    messenger_for_iphone = "237759909591655"
    messenger_for_iphone_dev = "202805033077166"
    facebook_lite = "275254692598279"
    messenger_for_lite = "200424423651082"
    ads_manager_app_android = "438142079694454"
    ads_manager_app_ios = "1479723375646806"
    page_ios = "165907476854626"
    page_android = "121876164619130"
    page_windows = "1174099472704185"
    business_manager = "436761779744620"
    messenger_kids_ios = "522404077880990"
    messenger_ios_house = "184182168294603"
    facebook_ipad = "124024574287414"
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(f"     {yellow}[01] {blue}FACEBOOK FOR ANDROID")
    print(f"     {yellow}[02] {blue}FACEBOOK MESSENGER FOR ANDROID")
    print(f"     {yellow}[03] {blue}FACEBOOK FOR IPHONE")
    print(f"     {yellow}[04] {blue}FACEBOOK MESSENGER FOR IPHONE")
    print(f"     {yellow}[05] {blue}FACEBOOK FOR LITE")
    print(f"     {yellow}[06] {blue}FACEBOOK MESSENGER FOR LITE")
    print(f"     {yellow}[07] {blue}ADS MANAGER APP FOR ANDROID")
    print(f"     {yellow}[08] {blue}ADS MANAGER APP FOR IOS")
    print(f"     {yellow}[09] {blue}FACEBOOK MESSENGER FOR IPHONE DEV")
    print(f"     {yellow}[10] {blue}PAGES MANAGER FOR IOS")
    print(f"     {yellow}[11] {blue}PAGES MANAGER FOR ANDROID")
    print(f"     {yellow}[12] {blue}PAGES MANAGER FOR WINDOWS")
    print(f"     {yellow}[13] {blue}BUSINESS MANAGER")
    print(f"     {yellow}[14] {blue}MESSENGER KIDS FOR IOS")
    print(f"     {yellow}[15] {blue}MESSENGER FOR IOS [IN-HOUSE]")
    print(f"     {yellow}[16] {blue}FACEBOOK FOR IPAD")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    type_access_token = input(" ENTER THE TOKEN TYPE YOU WANT TO GET: ")
    if type_access_token == '1':
    	app_id = facebook_android
    elif type_access_token == '2':
    	app_id = messenger_for_android
    elif type_access_token == '3':
    	app_id = facebook_iphone
    elif type_access_token == '4':
    	app_id = messenger_for_iphone
    elif type_access_token == '5':
    	app_id = facebook_lite
    elif type_access_token == '6':
    	app_id = messenger_for_lite
    elif type_access_token == '7':
    	app_id = ads_manager_app_android
    elif type_access_token == '8':
    	app_id = ads_manager_app_ios
    elif type_access_token == '9':
    	app_id = messenger_for_iphone_dev
    elif type_access_token == '10':
    	app_id = page_ios
    elif type_access_token == '11':
    	app_id = page_android
    elif type_access_token == '12':
    	app_id = page_windows
    elif type_access_token == '13':
    	app_id = business_manager
    elif type_access_token == '14':
    	app_id = messenger_kids_ios
    elif type_access_token == '15':
    	app_id = messenger_ios_house
    elif type_access_token == '16':
    	app_id = facebook_ipad
    url = f'https://www.facebook.com/dialog/oauth/business/cancel/?app_id={app_id}&version=v12.0&logger_id=&user_scopes[0]=user_birthday&user_scopes[1]=user_religion_politics&user_scopes[2]=user_relationships&user_scopes[3]=user_relationship_details&user_scopes[4]=user_hometown&user_scopes[5]=user_location&user_scopes[6]=user_likes&user_scopes[7]=user_education_history&user_scopes[8]=user_work_history&user_scopes[9]=user_website&user_scopes[10]=user_events&user_scopes[11]=user_photos&user_scopes[12]=user_videos&user_scopes[13]=user_friends&user_scopes[14]=user_about_me&user_scopes[15]=user_posts&user_scopes[16]=email&user_scopes[17]=manage_fundraisers&user_scopes[18]=read_custom_friendlists&user_scopes[19]=read_insights&user_scopes[20]=rsvp_event&user_scopes[21]=xmpp_login&user_scopes[22]=offline_access&user_scopes[23]=publish_video&user_scopes[24]=openid&user_scopes[25]=catalog_management&user_scopes[26]=user_messenger_contact&user_scopes[27]=gaming_user_locale&user_scopes[28]=private_computation_access&user_scopes[29]=instagram_business_basic&user_scopes[30]=user_managed_groups&user_scopes[31]=groups_show_list&user_scopes[32]=pages_manage_cta&user_scopes[33]=pages_manage_instant_articles&user_scopes[34]=pages_show_list&user_scopes[35]=pages_messaging&user_scopes[36]=pages_messaging_phone_number&user_scopes[37]=pages_messaging_subscriptions&user_scopes[38]=read_page_mailboxes&user_scopes[39]=ads_management&user_scopes[40]=ads_read&user_scopes[41]=business_management&user_scopes[42]=instagram_basic&user_scopes[43]=instagram_manage_comments&user_scopes[44]=instagram_manage_insights&user_scopes[45]=instagram_content_publish&user_scopes[46]=publish_to_groups&user_scopes[47]=groups_access_member_info&user_scopes[48]=leads_retrieval&user_scopes[49]=whatsapp_business_management&user_scopes[50]=instagram_manage_messages&user_scopes[51]=attribution_read&user_scopes[52]=page_events&user_scopes[53]=business_creative_transfer&user_scopes[54]=pages_read_engagement&user_scopes[55]=pages_manage_metadata&user_scopes[56]=pages_read_user_content&user_scopes[57]=pages_manage_ads&user_scopes[58]=pages_manage_posts&user_scopes[59]=pages_manage_engagement&user_scopes[60]=whatsapp_business_messaging&user_scopes[61]=instagram_shopping_tag_products&user_scopes[62]=read_audience_network_insights&user_scopes[63]=user_about_me&user_scopes[64]=user_actions.books&user_scopes[65]=user_actions.fitness&user_scopes[66]=user_actions.music&user_scopes[67]=user_actions.news&user_scopes[68]=user_actions.video&user_scopes[69]=user_activities&user_scopes[70]=user_education_history&user_scopes[71]=user_events&user_scopes[72]=user_friends&user_scopes[73]=user_games_activity&user_scopes[74]=user_groups&user_scopes[75]=user_hometown&user_scopes[76]=user_interests&user_scopes[77]=user_likes&user_scopes[78]=user_location&user_scopes[79]=user_managed_groups&user_scopes[80]=user_photos&user_scopes[81]=user_posts&user_scopes[82]=user_relationship_details&user_scopes[83]=user_relationships&user_scopes[84]=user_religion_politics&user_scopes[85]=user_status&user_scopes[86]=user_tagged_places&user_scopes[87]=user_videos&user_scopes[88]=user_website&user_scopes[89]=user_work_history&user_scopes[90]=email&user_scopes[91]=manage_notifications&user_scopes[92]=manage_pages&user_scopes[93]=publish_actions&user_scopes[94]=publish_pages&user_scopes[95]=read_friendlists&user_scopes[96]=read_insights&user_scopes[97]=read_page_mailboxes&user_scopes[98]=read_stream&user_scopes[99]=rsvp_event&user_scopes[100]=read_mailbox&user_scopes[101]=business_creative_management&user_scopes[102]=business_creative_insights&user_scopes[103]=business_creative_insights_share&user_scopes[104]=whitelisted_offline_access&redirect_uri=fbconnect%3A%2F%2Fsuccess&response_types[0]=token&response_types[1]=code&display=page&action=finish&return_scopes=false&return_format[0]=access_token&return_format[1]=code&tp=unspecified&sdk=&selected_business_id=&set_token_expires_in_60_days=false'
    res = session.post(url, data={'fb_dtsg': str(fb_dtsg)}).text
    session.close()
    access_token = re.findall(r'access_token=([^"]*)&data_access_expiration_time', res)[0]
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    print(access_token)

class FacebookApiVIP(object):
    def __init__(self, cookie):
        self.cookie = cookie
        self.user_id = self.extract_user_id(cookie)
        self.headers = self.generate_headers(cookie)
        self.session = self.create_session()
        self.fb_dtsg = None
        self.jazoest = None

    def extract_user_id(self, cookie):
        try:
            return cookie.split('c_user=')[1].split(';')[0]
        except IndexError:
            print("Cannot get user_id from cookie: c_user not found in cookie")
            raise ValueError("Invalid cookie")

    def generate_headers(self, cookie):
        return {
            'authority': 'mbasic.facebook.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'origin': 'https://mbasic.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://mbasic.facebook.com/',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cookie
        }

    def create_session(self):
        session = requests.Session()
        retry = Retry(
            total=5,
            backoff_factor=0.3,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "POST"]
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def get_thongtin(self):
        if self.fb_dtsg and self.jazoest:
            print("Using cached data.")
            return self.fb_dtsg, self.jazoest
        try:
            home = self.session.get('https://mbasic.facebook.com/profile.php', headers=self.headers, timeout=10).text
            self.fb_dtsg = re.search(r'name="fb_dtsg" value="(.*?)"', home).group(1)
            self.jazoest = re.search(r'name="jazoest" value="(.*?)"', home).group(1)
            ten = re.search(r'<title>(.*?)</title>', home).group(1)
            print(f" FACEBOOK NAME: {ten}, ID: {self.user_id}")
            return ten, self.user_id
        except AttributeError as e:
            print(f"Unable to get user information: Required information not found in response: {e}")
            return None
        except Exception as e:
            print(f"Unable to get user information: {e}")
            return None

    def report_user(self, target_user_id, timeout):
        if not self.fb_dtsg or not self.jazoest:
            print("Data not loaded yet. Reloading...")
            self.get_thongtin()
        reasons = {
            'spam': 'Spam',
            'violation': 'Violation of the rules',
            'hate_speech': 'Hate language',
            'pornography': 'Pornographic content',
            'harassment': 'Abuse',
            'impersonation': 'Fake',
            'personal_attack': 'Personal attack'
        }
        for reason_code, reason_description in reasons.items():
            data = {
                'av': self.user_id,
                '__user': self.user_id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'target_user_id': target_user_id,
                'report_type': 'user',
                'reason': reason_code
            }
            try:
                response = self.session.post('https://www.facebook.com/report/user', headers=self.headers, data=data, timeout=timeout)
                if response.status_code == 200:
                    print(f" {green}SUCCESSFULLY REPORTED USER {target_user_id} with reason '{reason_description}'.")
                else:
                    print(f" {red}FAILED REPORT WITH REASON '{reason_description}'. Response status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error executing report with reason '{reason_description}': {e}")
            except Exception as e:
                pass

def report_fb():
    clear_screen()
    ethan()
    colorful_loading()
    cookie = input(" ENTER COOKIE FACEBOOK: ")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    api = FacebookApiVIP(cookie)
    api.get_thongtin()
    target_user_id = input(" ENTER THE ID OF THE PERSON YOU WANT TO REPORT: ")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    timeout = int(input(" ENTER TIMEOUT REPORT IN SECONDS: "))
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    api.report_user(target_user_id, timeout)

class Spinner:

    def __init__(self, message):
        self.message = message
        self.stop_running = False
        self.thread = None
        self.animation_cycle = itertools.cycle(ARRAY_ANIMATION)
        self.columns = shutil.get_terminal_size().columns

    def start(self):
        self.stop_running = False
        self.thread = threading.Thread(target=self._animate)
        self.thread.start()

    def _animate(self):
        while not self.stop_running:
            sys.stdout.write(f'\r{self.message} {next(self.animation_cycle)}')
            sys.stdout.flush()
            time.sleep(0.1)

    def stop(self, exit_status):
        self.stop_running = True
        if self.thread is not None:
            self.thread.join()
        sys.stdout.write('\r' + ' ' * self.columns + '\r')
        sys.stdout.flush()

def wait():
    for i in range(100):
        print(f' Wait 2 Menite For Next Submit : {i + 1}/120', end='\r')
        time.sleep(1)
        os.system('clear')

class TikTokBooster:

    def __init__(self):
        self.ua = UserAgent('ios').Random()
        self.base_url = 'https://api.likesjet.com/freeboost/3'

    def boost_video(self, user: str, link: str) -> dict:
        email = f'suyibislam{random.randint(10000, 99999)}@gmail.com'
        headers = {'Host': 'api.likesjet.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': self.ua}
        data = {'link': link, 'tiktok_username': user, 'email': email}
        response = requests.post(self.base_url, json=data, headers=headers).json()
        return response

def tiktok_views():
    clear_screen()
    ethan()
    colorful_loading()
    user = input(f' {white}TIKTOK USERNAME : ')
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    link = input(f' {white}VIDEO LINK : ')
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    booster = TikTokBooster()
    try:
        response = booster.boost_video(user, link)
    except Exception as e:
        print(f"{red}[ERROR] Failed to send views: {str(e)}{w}")
        wait()
        main()
        return
    if response.get('status'):
        print(f'     {red}[REACTOR] {yellow}{user}  {blue}───────> {green}SUCCESSFULLY VIEW SENT!')
    else:
        pass
    wait()

class fbpost:
    def __init__(self, link):
        self.link = link

    def shir(self, token):
        url = "https://graph.facebook.com/me/feed"
        payload = {
            'link': self.link,
            'published': '1',
            'privacy': '{"value":"SELF"}',
            'access_token': token
        }
        try:
            response = requests.post(url, data=payload)
            uid = response.json().get('id')
            if response.status_code == 200:
                print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY SHARED!")
                return True
            else:
                pass
                return False
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return False

def sgtz(link, file_path, num_shares):
    start_all = time.time()
    tokens = gettokesz(file_path)
    if len(tokens) < num_shares:
        print("Not enough tokens to meet the requested number of shares.")
        return

    def worker(token):
        fb_poster = fbpost(link)
        fb_poster.shir(token)
    with ThreadPoolExecutor(max_workers=20) as executor:
        for token in tokens[:num_shares]:
            executor.submit(worker, token)
    end_all = time.time()
    print(f"\nSharing started at: {time.ctime(start_all)}")
    print(f"Sharing ended at: {time.ctime(end_all)}")
    print(f"Total duration: {end_all - start_all:.2f} seconds")

def ttsu(*file_paths):
    counts = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                counts.append(sum(1 for line in file if line.strip()))
        except FileNotFoundError:
            counts.append(0)
    return counts

def tts():
    file_paths = [
        '/sdcard/boostphere/FRAACCOUNT.txt',
        '/sdcard/boostphere/FRAPAGES.txt',
        '/sdcard/boostphere/RPWACCOUNT.txt',
        '/sdcard/boostphere/RPWPAGES.txt',
    ]
    for file_path in file_paths:
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                pass
            print(f"Created file: {file_path}")

def public():
    file_map = {
        '1': '/sdcard/boostphere/FRAACCOUNT.txt',
        '2': '/sdcard/boostphere/FRAPAGES.txt',
        '3': '/sdcard/boostphere/RPWACCOUNT.txt',
        '4': '/sdcard/boostphere/RPWPAGES.txt'
    }
    print(f"     {yellow}[01] {blue}FRA ACCOUNT")
    print(f"     {yellow}[02] {blue}FRA PAGES")
    print(f"     {yellow}[03] {blue}RPW ACCOUNT")
    print(f"     {yellow}[04] {blue}RPW PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"{white} CHOOSE : ").strip()
    file_path = file_map.get(choice)
    if not file_path:
        print("Invalid choice. Exiting.")
        return
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    a = input(f" {white}ENTER THE POST ID TO SHARE: ")
    post_id = get_combined_data(a)
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    num_shares = int(input(f" {yellow}LIMIT: "))
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    link = f"https://www.facebook.com/{post_id}"
    sgtz(link, file_path, num_shares)
def share112():
    clear()
    ethan()    
    colorful_loading()
    access_token = input('ENTER THE TOKEN: ').strip()
    linex()
    share_url = input('ENTER THE FACEBOOK POST LINK: ').strip()
    linex()
    try:
        share_count = int(input('HOW MANY SHARES WILL THE TOOL STOP: ').strip())
    except ValueError:
        print('{red}INVALID INPUT PLEASE ENTER A NUMBER FOR SHARE COUNT.')
        return
    linex()
    time_interval = 0.01
    delete_after = 3600
    shared_count = 0
    lock = threading.Lock()
    start_time = t.time()
    success_list = []
    headers = {
        'authority': 'b-graph.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }

    def share_post():
        nonlocal shared_count
        try:
            response = requests.post(
                f'https://b-graph.facebook.com/me/feed?access_token={access_token}&fields=id&limit=1&published=0',
                json={
                    'link': share_url,
                    'privacy': {'value': 'SELF'},
                    'no_story': True,
                },
                headers=headers
            )
            if response.status_code == 200:
                with lock:
                    shared_count += 1
                    success_list.append(response.json().get('id'))
                print(f'{green} SUCCESSFULLY {red}SHARED {shared_count} {orange} ⪼ {white} {share_count}')
                if shared_count == share_count:
                    print('{green}FINISHED SHARING POSTS.')
                    if success_list:
                        threading.Timer(delete_after, delete_post, args=(success_list[-1],)).start()
            else:
                print(f'{red}FAILED TO SHARE POST: {response.json()}')
        except requests.exceptions.RequestException as error:
            print(f'{red}ERROR: {str(error)}')
    while shared_count < share_count:
        share_post()
        #time.sleep(time_interval)
    elapsed_time = t.time() - start_time
    avg_time_per_share = elapsed_time / share_count if share_count > 0 else 0
    total_time = timedelta(seconds=int(elapsed_time))
    avg_time = timedelta(seconds=int(avg_time_per_share))
    print(f"🚀 TARGET: {share_url}")
    print(f"✅ SUCCESSFULLY SHARED: {shared_count}/{share_count}")
    print(f"⏳ TOTAL TIME: {total_time}")
    print(f"⏱️ AVERAGE TIME PER SHARE: {avg_time}")
    linex()
def pub():
	
    tts()
    fra_file = '/sdcard/boostphere/FRAACCOUNT.txt'
    fra_pages_file = '/sdcard/boostphere/FRAPAGES.txt'
    rpw_file = '/sdcard/boostphere/RPWACCOUNT.txt'
    rpw_pages_file = '/sdcard/boostphere/RPWPAGES.txt'
    total_accounts, total_pages, rpw_accounts, rpw_pages = ttsu(
        fra_file, fra_pages_file, rpw_file, rpw_pages_file
    )
    clear_screen()
    ethan()
    colorful_loading()
    print(f"""               {Q7}💥OVERVIEW OF STORED ACCOUNT & PAGES☑️
 {Q7}─────────────────────────────────────────────────────────────────\033[0m
                            {Q7}FRA ACCOUNT{yellow} : {green}{total_accounts}
                            {Q7}FRA PAGES  {yellow} : {green}{total_pages}
                            {Q7}RPW ACCOUNT{yellow} : {green}{rpw_accounts}
                            {Q7}RPW PAGES  {yellow} : {green}{rpw_pages}
 {Q7}─────────────────────────────────────────────────────────────────\033[0m""")
    print(f"     {yellow}[1] {blue}EXTRACT ACCOUNT")
    print(f"     {yellow}[2] {blue}AUTO SHARE")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"{white} CHOOSE : ").strip()
    if choice == '1': 
        extraction()
    if choice == '2': 
        share()
def react():
    ses = requests.Session()

    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                result = response.json().get('id')
                return result
        except Exception as e:
            print(f"{red}  An error occurred: {e}")
        return None

    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        print(f"{red}  Invalid post link.")
        return None

    def get_access_token_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip().split('\n')
        except FileNotFoundError:
            print(f"{red}  Start the tool first!")
            return None
    clear()
    ethan()
    print(f'''{white}  CHOOSE FACEBOOK TO REACT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    
    account_choose = input(f'''{yellow}  Choose : {green}''')
    
    file_path = None
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    elif account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    elif account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    elif account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    elif account_choose == '0' or account_choose == '00':
        main()
        return
    if file_path is None:
        print(f'''{red}  Invalid Input!''')
        sleep(1.5)
        react()
        return
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    post_link = input(f'''{yellow}  Enter post link: {green}''')
    target_uid = extract_uid_from_link(post_link)
    if not target_uid:
        print(f'''{red}  UID extraction failed. Please provide a valid post link. Copy link on Facebook Lite!''')
        return None
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{red}  [1] {blue}LIKE''')
    print(f'''{red}  [2] {blue}LOVE''')
    print(f'''{red}  [3] {blue}HAHA''')
    print(f'''{red}  [4] {blue}WOW''')
    print(f'''{red}  [5] {blue}ANGRY''')
    print(f'''{red}  [6] {blue}SAD''')
    line()
    react_choice = input(f'''{yellow}  Choose : {green}''')
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD'
    }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f'''{red}  Invalid reaction choice.''')
        return None
    converted_link = convert_to_traodoisub(post_link)
    if not converted_link:
        print(f"{red}  Failed to convert the link.")
        return None
    line()
    try:
        limit = int(input(f'''{yellow}  Input quantity of reactions, limit is {green}{len(access_tokens)} : '''))
    except ValueError:
        print(f'''{red}  Error: Please enter a valid number for the limit.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}  Error: The specified limit exceeds the number of available reactors.''')
        return None
    success_count = 0
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = f'''{target_uid}_{converted_link}'''
        auto_react = f'''https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'''
        time.sleep(1)
        headers_ = {'user-agent': W_ueragnt()}  # Assuming W_ueragnt() is defined
        response = requests.post(auto_react, headers=headers_)
        if response.ok:
            print(f'''{green}  REACTOR {i + 1} ---> Successfully Reacted! ''')
            success_count += 1
        else:
            print(f'''{red}  REACTOR {i + 1} ---> Failed to React!''')
            failure_count += 1
    line()
    print(f'''{yellow}  TOTAL : ''')
    print(f'''{green}  Completed : {white}{success_count}''')
    print(f'''{red}  Failed : {white}{failure_count}''')
def extraction():
    clear_screen()
    ethan()
    print(f"     {yellow}[1] {blue}EXTRACT ACCOUNT")
    print(f"     {yellow}[2] {blue}EXTRACT PAGES")
    print(f" {Q7}─────────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"{white} CHOOSE : ").strip()
    if choice == '1':
        axl1()
    elif choice == '2':
        axl2()
    else:
        print(f"{red}INVALID CHOICE")
        
def main3() -> None:
    ethan()
    input(f"{Q} PRESS ENTER TO START....")
    for make in range(100):
        ses = requests.Session()
        response = ses.get(
            url='https://x.facebook.com/reg',
            params={"_rdc":"1","_rdr":"","wtsid":"rdr_0t3qOXoIHbMS6isLw","refsrc":"deprecated"},
        )
        mts = ses.get("https://x.facebook.com").text
        m_ts = re.search(r'name="m_ts" value="(.*?)"',str(mts)).group(1)
        formula = extractor(response.text)
        email2 = GetEmail()
        firstname,lastname = fake_name()
        print(f"{Q} NAME  - {red}{firstname} {lastname}")
        print(f"{Q} EMAIL - {red}{email2}")
        payload = {
            'ccp': "2",
            'reg_instance': str(formula["reg_instance"]),
            'submission_request': "true",
            'helper': "",
            'reg_impression_id': str(formula["reg_impression_id"]),
            'ns': "1",
            'zero_header_af_client': "",
            'app_id': "103",
            'logger_id': str(formula["logger_id"]),
            'field_names[0]': "firstname",
            'firstname': firstname,
            'lastname': lastname,
            'field_names[1]': "birthday_wrapper",
            'birthday_day': str(random.randint(1,28)),
            'birthday_month': str(random.randint(1,12)),
            'birthday_year': str(random.randint(1992,2009)),
            'age_step_input': "",
            'did_use_age': "false",
            'field_names[2]': "reg_email__",
            'reg_email__': email2,
            'field_names[3]': "sex",
            'sex': "2",
            'preferred_pronoun': "",
            'custom_gender': "",
            'field_names[4]': "reg_passwd__",
            'name_suggest_elig': "false",
            'was_shown_name_suggestions': "false",
            'did_use_suggested_name': "false",
            'use_custom_gender': "false",
            'guid': "",
            'pre_form_step': "",
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0],"MrCode@123"),
            'submit': "Sign Up",
            'fb_dtsg': "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",
            'jazoest': str(formula["jazoest"]),
            'lsd': str(formula["lsd"]),
            '__dyn': "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
            '__csr': "",
            '__req': "p",
            '__fmt': "1",
            '__a': "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
            '__user': "0"
        }
        header1 = {
            "Host":"m.facebook.com",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":ugenX(),
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "dnt":"1",
            "X-Requested-With":"mark.via.gp",
            "Sec-Fetch-Site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "dpr":"1.75",
            "viewport-width":"980",
            "sec-ch-ua":"\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile":"?1",
            "sec-ch-ua-platform":"\"Android\"",
            "sec-ch-ua-platform-version":"\"\"",
            "sec-ch-ua-model":"\"\"",
            "sec-ch-ua-full-version-list":"",
            "sec-ch-prefers-color-scheme":"dark",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
        }
        reg_url = "https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1"
        py_submit = ses.post(reg_url, data=payload, headers=header1)
        #print(ses.cookies.get_dict().items())
        if "c_user" in py_submit.cookies:
            first_cok = ses.cookies.get_dict()
            uid = str(first_cok["c_user"])
            header2 = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2',
                'referer': 'https://m.facebook.com/login/save-device/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': ugenX(),
                'viewport-width': '980',      
            }
            params = {
                'next': 'https://m.facebook.com/?deoia=1',
                'soft': 'hjk',
            }
            con_sub = ses.get('https://x.facebook.com/confirmemail.php', params=params, headers=header2).text
            valid = GetCode(email2)
            if valid:
                print(f"{green} FB UID - {G}{uid}")
                print(f"{green} LOGIN OTP - {G}{valid}")
                confirm_id(email2,uid,valid,con_sub,ses)
            else:
                print(f"{red} \x1b[38;5;206mSUCCESSFULLY DISABLED ID")
                linex()
        else:
            print(f"{red} {green}SUCCESSFULLY CHECKPOINT ID")
            linex()
from fake_useragent import UserAgent
ua = UserAgent()
def ugenX():
    ualist = [ua.random for _ in range(50)]
    return str(random.choice(ualist))
    
def extractor(data):
    try:
        soup = BeautifulSoup(data,"html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error":str(e)}
def GetEmail():
    response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
    return response['email']
def GetCode(email):
    try:
        response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').text
        code = re.search(r'FB-(\d+)', response).group(1)
        return code
    except:
        return None
def fake_name():
    first = Faker().first_name()
    last = Faker().last_name()
    return first,last
    
def confirm_id(mail,uid,otp,data,ses):
    try:
        url = "https://m.facebook.com/confirmation_cliff/"
        params = {
        'contact': mail,
        'type': "submit",
        'is_soft_cliff': "false",
        'medium': "email",
        'code': otp}
        payload = {
        'fb_dtsg': 'NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0',
        'jazoest': re.search(r'"\d+"', data).group().strip('"'),
        'lsd': re.search('"LSD",\[\],{"token":"([^"]+)"}',str(data)).group(1),
        '__dyn': "",
        '__csr': "",
        '__req': "4",
        '__fmt': "1",
        '__a': "",
        '__user': uid}
        headers = {
        'User-Agent': ugenX(),
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'sec-ch-ua-full-version-list': "",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-mobile': "?1",
        'x-asbd-id': "129477",
        'x-fb-lsd': "KnpjLz-YdSXR3zBqds98cK",
        'sec-ch-prefers-color-scheme': "light",
        'sec-ch-ua-platform-version': "\"\"",
        'origin': "https://m.facebook.com",
        'x-requested-with': "mark.via.gp",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'priority': "u=1, i"}
        response = ses.post(url, params=params, data=payload, headers=headers)
        if "checkpoint" in str(response.url):
            print(f"{X}{R} FUCKED ID DISABLED")
            linex()
        else:
            cookie = (";").join([ "%s=%s" % (key,value) for key,value in ses.cookies.get_dict().items()])
            print(f"{X} SUCCESS - {G}{uid}|MrCode@123|{cookie}")
            open("/sdcard/SUCCESS-OK-ID.txt","a").write(uid+"|MrCode@123|"+cookie+"\n")
            linex()
    except Exception as e:
        linex()
        pass

# ================= ACCOUNT INFO =================
def account():
    clear_screen()
    ethan()

    # ensure files exist
    open('/sdcard/boostphere/FRAACCOUNT.txt', 'a').close()
    open('/sdcard/boostphere/FRAPAGES.txt', 'a').close()
    open('/sdcard/boostphere/RPWACCOUNT.txt', 'a').close()
    open('/sdcard/boostphere/RPWPAGES.txt', 'a').close()

    fraaccounts_file = '/sdcard/boostphere/FRAACCOUNT.txt'
    frapages_file   = '/sdcard/boostphere/FRAPAGES.txt'
    rpwaccounts     = '/sdcard/boostphere/RPWACCOUNT.txt'
    rpwpages        = '/sdcard/boostphere/RPWPAGES.txt'

    total_accounts, total_pages = count_tokens(fraaccounts_file, frapages_file)
    total_account_rpw, total_pages_rpw = count_tokens(rpwaccounts, rpwpages)

    print(f"""
{DD}
{DD}   {Q7}FRA ACCOUNT{yellow} : {green}{total_accounts:<10}                {DD}
{DD}   {Q7}FRA PAGES  {yellow} : {green}{total_pages:<10}                {DD}
{DD}   {Q7}RPW ACCOUNT{yellow} : {green}{total_account_rpw:<10}             {DD}
{DD}   {Q7}RPW PAGES  {yellow} : {green}{total_pages_rpw:<10}             {DD}
{DD}
""")


# ================= MAIN MENU =================
def main_menu():
    print("")
    print(f"{YY}              MAIN MENU              {DD}")
    print(f" {YY}[{Q} 1. {YY}] {C} ACCOUNT STATUS AND CHECKER              ")
    print(f" {YY}[{Q} 2. {YY}] {C} FACEBOOK REACTION TOOL SERVICES         ")
    print(f" {YY}[{Q} 3. {YY}] {C} CUSTOMIZATION COMMENT SERVICES          ")
    print(f" {YY}[{Q} 4. {YY}] {C} FOLLOWERS TOOL SERVICES                 ")
    print(f" {YY}[{Q} 5. {YY}] {C} SHARE TOOL SERVICES                     ")
    print(f" {YY}[{Q} 6. {YY}] {C} OTHER TOOL SERVICES                     ")
    print(f" {YY}[{Q} 0. {YY}] {C} TOOL EXIT MENU                          ")
    print("")

    choice = input(f"{white}{DD} {C}CHOOSE : ").strip()

    if choice == "1":
        column_1()
    elif choice == "2":
        column_2()
    elif choice == "3":
        column_3()
    elif choice == "4":
        column_4()
    elif choice == "5":
        column_5()
    elif choice == "6":
        column_6()
    elif choice == "0":
        exit()
    else:
        main_menu()


# ================= COLUMN 1 =================
def column_1():
    print(f"TOOL MAIN MENU")
    print(f"{DD} 1. Facebook Account Extraction")
    print(f"{DD} 2. Live Account Checker")
    print(f"{DD} 3. Reset Tool")
    print(f"{DD} 4. Update Tool")
    print(f"{DD} 0. Back")

    c = input(f"{white}{DD} {C}CHOOSE : ").strip()

    if c == "1":
        extraction()
    elif c == "2":
        fetch_account_info(file_options)
    elif c == "3":
        reset_tool()
    elif c == "4":
        update_tool()
    elif c == "0":
        main_menu()
    else:
        column_1()


# ================= COLUMN 2 =================
def column_2():
    print(f"\n{DD} {YY}COLUMN 2 - REACTION")
    print(f"{DD} 1. Reaction Fast")
    print(f"{DD} 2. Reaction Slow")
    print(f"{DD} 3. Reaction Reel / Video")
    print(f"{DD} 4. Reaction Group Post")
    print(f"{DD} 5. Reaction Live")
    print(f"{DD} 6. Reaction Comments")
    print(f"{DD} 0. Back")

    c = input(f"{white}{DD} {C}CHOOSE : ").strip()

    if c == "1":
        perform_reaction_fast()
    elif c == "2":
        react()
    elif c == "3":
        reels()
    elif c == "4":
        group_react()
    elif c == "5":
        live_react()
    elif c == "6":
        comment_react()
    elif c == "0":
        main_menu()
    else:
        column_2()


# ================= COLUMN 3 =================
def column_3():
    print(f"\n{DD} {YY}COLUMN 3 - CUSTOM COMMENT")
    print(f"{DD} 1. Custom Comment")
    print(f"{DD} 2. Comment on Live")
    print(f"{DD} 3. Reply Comment")
    print(f"{DD} 0. Back")

    c = input(f"{white}{DD} {C}CHOOSE : ").strip()

    if c == "1":
        perform_comment_fast()
    elif c == "2":
        live_comment()
    elif c == "3":
        reply()
    elif c == "0":
        main_menu()
    else:
        column_3()


# ================= COLUMN 4 =================
def column_4():
    print(f"\n{DD} {YY}COLUMN 4 - FOLLOWER")
    print(f"{DD} 1. Auto Followers")
    print(f"{DD} 2. Page / Profile Follower")
    print(f"{DD} 3. Page Likes & Followers")
    print(f"{DD} 0. Back")

    c = input(f"{white}{DD} {C}CHOOSE : ").strip()

    if c == "1":
        auto_follow_fast()
    elif c == "2":
        auto_follow_page()
    elif c == "3":
        perform_actions_from_file()
    elif c == "0":
        main_menu()
    else:
        column_4()


# ================= COLUMN 5 =================
def column_5():
    print(f"\n{DD} {YY}COLUMN 5 - SHARE")
    print(f"{DD} 1. Auto Share Fast")
    print(f"{DD} 2. Auto Share Slow")
    print(f"{DD} 3. Page Likes & Follower")
    print(f"{DD} 0. Back")

    c = input(f"{white}{DD} {C}CHOOSE : ").strip()

    if c == "1":
        main2()
    elif c == "2":
        share112()
    elif c == "3":
        pub()
    elif c == "0":
        main_menu()
    else:
        column_5()


# ================= COLUMN 6 =================
def column_6():
	
    print(f"\n{DD} {YY}COLUMN 6 - OTHERS")
    print(f"{DD} 1. Token Getter")
    print(f"{DD} 2. Facebook Mass Report")
    print(f"{DD} 3. FB Story Views")
    print(f"{DD} 4. Auto Create FB Account")
    print(f"{DD} 5. TikTok Views")
    print(f"{DD} 6. Token Checker")
    print(f"{DD} 7. Duplicate Account Checker")
    print(f"{DD} 0. Back")

    c = input(f"{white}{DD} {C}CHOOSE : ").strip()

    if c == "1":
        get_token()
    elif c == "2":
        report_fb()
    elif c == "3":
        perform_viewfb_fast()
    elif c == "4":
        main3()
    elif c == "5":
        tiktok_views()
    elif c == "6":
        check()
    elif c == "7":
        remove_duplicates()
    elif c == "0":
        main_menu()
    else:
        column_6()


# ================= START PROGRAM =================
account()
main_menu()

    

if __name__ == "__main__":
       #generate_and_check_code()
       main()
   
    
    
    
