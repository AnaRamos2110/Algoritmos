#Automatizando o clik direito do mouse com a função rightClick :))

import pyautogui #Chamando as bibliotecas!
import time

pyautogui.hotkey('win', 'd') #Minimiza o VS Code
time.sleep(1) #Tempo de 1 segundo 

time.sleep(1)
pyautogui.rightClick(x=500, y=300) #Definindo alta+largura e chamando função click direito do mouse, assim acionando o menu




#Chamando a função double click
time.sleep(1)
pyautogui.doubleClick(x=500, y=300)

