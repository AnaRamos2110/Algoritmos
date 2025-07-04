import pyautogui

#Captura a tela inteira

screenshot = pyautogui.screenshot() #Armazena o print dentro da variável

#Salva a imagem
screenshot.save('screenshot.png')