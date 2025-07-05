import pyautogui
import time
import pyperclip



pyautogui.hotkey('win', 'r')
pyautogui.write('chrome')
pyautogui.press('enter')


time.sleep(2)

pyautogui.write('https://www.youtube.com')
pyautogui.press('enter')

time.sleep(3)

pyautogui.click(650,150)

pyperclip.copy('dark hearth- fly')
pyautogui.hotkey('ctrl', "v")
pyautogui.press('enter')
pyautogui.click(600,250)
pyautogui.press('enter')