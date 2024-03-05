import pyautogui
import time

pyautogui.PAUSE = 1

for i in range(50):
    time.sleep(2)


    # Simular Ctrl + Home
    pyautogui.hotkey('ctrl', 'home')
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'home')
    time.sleep(2)
    #Voto 1
    # pyautogui.click(x=649, y=400)
    #Voto 2
    # pyautogui.click(x=649, y=445)
    #Voto 3
    pyautogui.click(x=649, y=510)
    time.sleep(4)

    # Simular Ctrl + End
    pyautogui.hotkey('ctrl', 'end')
    time.sleep(4)

    # Sou humano?
    pyautogui.click(x=633, y=500) # clique no botao de login
    time.sleep(16)


    # Simular Ctrl + Home
    pyautogui.hotkey('ctrl', 'home')
    time.sleep(5)
    
    # Votar novamente
    pyautogui.click(x=654, y=270) # clique no botao de login
    time.sleep(7)

