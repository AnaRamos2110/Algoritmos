#Automação -- existem bibliotecas de terceiros para ajudar neste processo !!
import pyautogui
import time
import subprocess  

#1- PASSO: ABRIR O BLOCO DE NOTAS (É UMA APLICAÇÃO DESKTOP!)

subprocess.Popen('notepad.exe')
time.sleep(2) #Para automatizar algo é sempre importante um tempo de espera para não ter delay!

#2- PASSO:  DIGITAR UM TEXTO    
pyautogui.write("Oii, Este eh um teste automatizado!", interval=0.1) #OBS, OS CARACTERES ESPECIAIS NÃO ESTÃO SENDO CHAMADOS POIS DEPENDEM DE OUTRO CÓDIGO!

