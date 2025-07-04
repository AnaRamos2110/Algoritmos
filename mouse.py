import pyautogui
import time

#Mover o mouse para a disposição(500, 500)

pyautogui.moveTo(500, 500, duration=1)


#Arrasta o mouse
pyautogui.moveTo(300, 600)
pyautogui.dragTo(600, 300, duration=2)