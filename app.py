from pyautogui import *
from time import sleep
import sys
import webbrowser as wb
f = open("numbers.txt", "r")
a = f.read().split(' , ')

msg = "Your message"
for i in range(len(a)):
    wb.open(f"https://web.whatsapp.com/send?phone=+91{a[i]}&text={msg}")
    sleep(15)
    x3, y3 = [950, 750]
    moveTo(x3, y3)
    click()
    press('enter')
    sleep(10)
    hotkey("ctrl", "w")
