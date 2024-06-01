from wmi import WMI
import subprocess, requests, time, os
hwid = WMI().Win32_ComputerSystemProduct()[0].UUID
r = requests.get('https://pastebin.com/SZxttR2G')

try:
    if hwid in r.text:
        pass
    else:
        print('Ошибка, данных hwid не был найден в базе данных')
        print(f'HWID: {hwid}')
        time.sleep(3)
        os._exit()
except:
    print('Ошибка, не удаётся соединится с базой данных')
    time.sleep(3)
    os._exit()

print('Доступ разрешен')
time.sleep(3)
print("hello, world")
