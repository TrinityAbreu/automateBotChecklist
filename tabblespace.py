import pyautogui
import time
from time import sleep
from PIL import ImageGrab
from pynput.mouse import Controller, Button
mouse = Controller()
texto = 'usuario'

def acesso(a, c):
     pyautogui.PAUSE = 1 
     while not esperar_imagem(f"images\\{a}.png"):
         sleep(0.1)
     ambiente = f"images\\{a}.png"
     coordinates_ambiente = pyautogui.locateCenterOnScreen(ambiente)
     sleep(2)
     pyautogui.doubleClick(coordinates_ambiente)
     while not esperar_imagem("images\\sap.png"):
        sleep(1)
     texto = 'usuario'
     senha = f'{c}'
     pyautogui.write(texto.upper())
     pyautogui.press('Tab')
     pyautogui.write(senha)   
     pyautogui.press('enter')
     pyautogui.press('enter')
     while not esperar_imagem("images\\lobby.png"):
        sleep(1)
     sleep(1)

def scroll_down():
    pyautogui.click()
    sleep(1)
    mouse.scroll(0, -10)
    sleep(1)

def esperar_imagem(aparecer_imagem, timeout=1500):
    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            print("Tempo limite excedido.")
            start_time = time.time()  # Reinicia o tempo de início
            
        try:
            image_location = pyautogui.locateCenterOnScreen(aparecer_imagem)
            
            if image_location is not None:
                if isinstance(image_location, tuple) and len(image_location) == 2:
                    return True
                else:
                    time.sleep(1)
        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")
            time.sleep(20)
            continue

def acesso_smp():
    pyautogui.PAUSE = 0.5

    smp_path = "images\\smp.png"
    smp_selecionado_path = "images\\smp_selecionado.png"
    coordinates_smp = pyautogui.locateCenterOnScreen(smp_path)
    coordinates_smp_selecionado = pyautogui.locateCenterOnScreen(smp_selecionado_path)
    sleep(1)
    if coordinates_smp:
        pyautogui.doubleClick(coordinates_smp)
    else:
        pyautogui.doubleClick(coordinates_smp_selecionado)

    while not esperar_imagem("images\\sap.png"):
            sleep(0.1)
    pyautogui.write(texto.upper())
    pyautogui.press('Tab')
    pyautogui.write('senha')
    pyautogui.press('Enter')
    pyautogui.press('Enter')
    while not esperar_imagem("images\\lobby.png"):
            sleep(0.1)
    pyautogui.write('dbacockpit')
    pyautogui.press('Enter')
    while not esperar_imagem("images\\minimizar.png"):
            sleep(0.1)
    minimizar = "images\\minimizar.png"
    coordinates_used = pyautogui.locateCenterOnScreen(minimizar)
    pyautogui.click(minimizar)
    sleep(2)
    espaco = "images\\espaco.png"
    coordinates_used = pyautogui.locateCenterOnScreen(espaco)
    pyautogui.doubleClick(espaco)
    sleep(1)
    tabblespace = "images\\tabblespace.png"
    coordinates_used = pyautogui.locateCenterOnScreen(tabblespace)
    pyautogui.doubleClick(tabblespace)
    sleep(1)
    pyautogui.press('down')
    over = "images\\overview.png"
    coordinates_used = pyautogui.locateCenterOnScreen(over)
    pyautogui.doubleClick(over)
    while not esperar_imagem("images\\used.png"):
            sleep(0.1)
    used = r"images\\used.png"
    coordinates_used = pyautogui.locateCenterOnScreen(used)
    pyautogui.rightClick(used)
    while not esperar_imagem("images\\decrescente.png"):
            sleep(0.1)
    decrescente = "images\\decrescente.png"
    coordinates_used = pyautogui.locateCenterOnScreen(decrescente)
    pyautogui.click(decrescente)
    sleep(3)

def print_ambiente(a):
      sleep(1)
      nome_arquivo = f"Prints\\TABLESPACE/{a}.png"
      pyautogui.screenshot(nome_arquivo) 
      sleep(2)

def mudar_ambiente(ambiente, alterar, alterado):
        pyautogui.PAUSE = 0.5
        # Ambiente
        ambiente = f"images\\{ambiente}_ambiente.png"
        coordinates_ambiente = pyautogui.locateCenterOnScreen(ambiente)
        sleep(1)
        pyautogui.click(coordinates_ambiente)
        sleep(3)

        # Alterar  
        pyautogui.PAUSE = 0.5
        while not esperar_imagem(f"images\\{alterar}_backup.png"):
             sleep(0.1)
        alterar = f"images\\{alterar}_backup.png"
        coordinates_alterar = pyautogui.locateCenterOnScreen(alterar)
        pyautogui.doubleClick(alterar)
        sleep(1)
        
        # Esperar
        pyautogui.PAUSE = 0.5
        alterado = f"images\\{alterado}_alterado.png"
        while not esperar_imagem(alterado):
             sleep(0.1)
        minimizar = "images\\minimizar.png"
        coordinates_minimizar = pyautogui.locateCenterOnScreen(minimizar)
        pyautogui.click(coordinates_minimizar)

def alterar_ambiente_scroll(ambiente, alterar, alterado):
    if ambiente == "ecd" and "ecp":
        pyautogui.PAUSE = 0.5
        # Ambiente
        ambiente = f"images\\{ambiente}_ambiente.png"
        coordinates_ambiente = pyautogui.locateCenterOnScreen(ambiente)
        pyautogui.click(coordinates_ambiente) 
        sleep(1)
        pyautogui.click()
        sleep(4)
        pyautogui.click()
    else:
        pyautogui.PAUSE = 0.5
        # Ambiente
        ambiente = f"images\\{ambiente}_ambiente.png"
        coordinates_ambiente = pyautogui.locateCenterOnScreen(ambiente)
        pyautogui.click(coordinates_ambiente) 
        sleep(3)

    sleep(1)
    scroll_down()

    # Alterar
    pyautogui.PAUSE = 0.5
    while not esperar_imagem(f"images\\{alterar}_backup.png"):
        sleep(0.1)
    alterar = f"images\\{alterar}_backup.png"
    coordinates_alterar = pyautogui.locateCenterOnScreen(alterar)
    sleep(2)
    pyautogui.doubleClick(coordinates_alterar)
    sleep(2)
    
    # Esperar
    if alterado == "smd":
        pyautogui.PAUSE = 0.5
        sleep(3)
        clock = "images\\clock.png"
        coordinates_clock = pyautogui.locateCenterOnScreen(clock)
        pyautogui.click(coordinates_clock)
        minimizar = "images\\minimizar.png"
        coordinates_minimizar = pyautogui.locateCenterOnScreen(minimizar)
        pyautogui.click(coordinates_minimizar)
    else:
        pyautogui.PAUSE = 0.5
        alterado = f"images\\{alterado}_alterado.png"
        while not esperar_imagem(alterado):
            sleep(0.1)
        minimizar = "images\\minimizar.png"
        coordinates_minimizar = pyautogui.locateCenterOnScreen(minimizar)
        pyautogui.click(coordinates_minimizar)

def sair():
    pyautogui.PAUSE = 1
    pyautogui.hotkey('alt', 'f4')
    sleep(1)
    pyautogui.press('Tab')
    pyautogui.press('enter')

def fazer_full():
    acesso_smp()
    print_ambiente("BID")

    mudar_ambiente("bid", "csd", "csd")
    print_ambiente("CSD")

    mudar_ambiente("csd", "csp", "csp")
    print_ambiente("CSP")

    mudar_ambiente("csp", "csq", "csq")
    print_ambiente("CSQ")

    mudar_ambiente("csq", "ecd", "ecd")
    print_ambiente("ECD")

    mudar_ambiente("ecd", "ecp", "ecp")
    print_ambiente("ECP")

    mudar_ambiente("ecp", "epp", "epp")
    print_ambiente("EPP")

    alterar_ambiente_scroll("epp", "epq", "epq")
    print_ambiente("EPQ")

    alterar_ambiente_scroll("epq", "pnd", "pnd")
    print_ambiente("PND")

    alterar_ambiente_scroll("pnd", "ssd", "ssd")
    print_ambiente("SSD")

    alterar_ambiente_scroll("ssd", "ssp", "ssp")
    print_ambiente("SSP")

    alterar_ambiente_scroll("ssp", "ssq", "ssq")
    print_ambiente("SSQ")

    sair()

def tablespace():
    fazer_full()


