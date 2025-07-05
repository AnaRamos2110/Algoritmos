#Okay, segue série de exercicíos para 04/07!

#Chamando as bibliotecas principais do exercicío
import pyautogui
import time
import subprocess

#1-- minimizar todas as janelas
pyautogui.hotkey('win', 'd') #Minimiza o VS Code
time.sleep(2) #Tempo de 2 segundos

#2-- Criar pasta:
pyautogui.hotkey('ctrl', 'shift', 'n')
pyautogui.press('space')
pyautogui.write('minha pasta')
pyautogui.press('enter')
pyautogui.press('enter')

#Abrindo pasta e criando documento txt.
pyautogui.click(x=1250, y=750)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.press('space')
pyautogui.write('TXT')
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('AUTOMATICO')
pyautogui.hotkey('ctrl', 's')
pyautogui.hotkey('alt', 'f4')