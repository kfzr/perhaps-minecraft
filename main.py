import os
from os.path import join
import subprocess
import time
from time import sleep
from colorama import Fore,Style,init

directory = "mark"
parent_dir = "C:/"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
file = 'C:\mark\yaish.txt'
with open(file, 'a') as f:
    f.write(
        'just a joke man\ncalm down lmao'
     )


print("Minecraft token:")
print("...")
lookfor = "launcher_profiles.json"
for root, dirs, files in os.walk('C://'):
    if lookfor in files:
        path = os.path.join(root,lookfor)
        print(path)
        break
print("...")
sleep(1)
print("See, I could've easily sent myself all of your personal information, but im just not that guy.")
sleep(1)
print("So anyways enjoy your (Minecraft) launcher profiles path")
sleep(1)
print("and have a good day.")
easteregg = input()
if easteregg == "no":
    print("...")
    sleep(2.3)
    print("Excuse me?")
    print("...")
    sleep(1)
    print("No?")
    sleep(5)
    print("ok.")
    print(f"{Fore.RED}ill show u no.")
    print("...")
    sleep(3)
    print("located system32 [C:\Windows\System32]")
    sleep(1)
    print("injecting memz into %%path*sys32")
    print("no init: 534.62")
    print("no init: 521.75")
    print("no init: 550.69")
    print("no init: 546.42")
    sleep(1)
    print("method init on def")
    sleep(3)
    print("Still 'no'?")
    