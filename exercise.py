import pyautogui
import time
import subprocess

#PARA ABRIR O BLOCO DE NOTAS 
subprocess.Popen('notepad.exe')

#PARA DIGITAR TEXTO 
time.sleep(2.5)
pyautogui.write('BUDWEISER ITS BETTER THAN HEINEKEN\n')
time.sleep(2.5)
pyautogui.hotkey('ctrl', 'shift', 's')
pyautogui.press('tab' * 4)
time.sleep(1)
pyautogui.press('enter')


