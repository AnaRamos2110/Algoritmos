import pyautogui
import time

print("Pressione Ctrl C para parar!")
while True:
    x, y = pyautogui.position()
    print(f"Posição atual do mouse: X={x} Y={y}, end\r")
    