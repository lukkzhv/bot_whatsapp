import pyautogui
import webbrowser
import keyboard
from time import sleep
# https://api.whatsapp.com/send?phone=554299728818

numbers = []
with open('numbers.txt', 'r') as arquivo:
    for n in arquivo:
        numbers.append(n.split('\n')[0])
for number in numbers:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={number}')
    sleep(1)
    pyautogui.click(677,323, duration=0.5)
    sleep(0.8)
    pyautogui.click(677,392, duration=0.3)
    sleep(8)
    pyautogui.typewrite('Seja bem-vindo...', interval=0.1)
    sleep(0.5)
    pyautogui.press('enter')
    sleep(60)