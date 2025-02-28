import pyautogui
import time
from time import sleep
from PIL import ImageGrab
from pynput.mouse import Controller, Button
import os

mouse = Controller()
def scroll_down_ambientes():
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

def alterar_ambiente(ambiente, alterar, alterado):
    pyautogui.PAUSE = 0.5
    # Ambiente
    ambiente = f"images\\{ambiente}_ambiente.png"
    coordinates_ambiente = pyautogui.locateCenterOnScreen(ambiente)
    sleep(1)
    pyautogui.click(coordinates_ambiente)
    sleep(2)

    # Alterar
    if alterar == "bip":
         pyautogui.PAUSE = 0.5
         pyautogui.press('down')
         pyautogui.press('enter')
         sleep(2)
    else:
        while not esperar_imagem(f"images\\{alterar}_backup.png"):
             sleep(0.1)
        pyautogui.PAUSE = 0.5
        alterar = f"images\\{alterar}_backup.png"
        coordinates_alterar = pyautogui.locateCenterOnScreen(alterar)
        pyautogui.doubleClick(coordinates_alterar)
        sleep(1)
    
    # Esperar
    alterado = f"images\\{alterado}_alterado.png"
    while not esperar_imagem(alterado):
        sleep(0.1)
    minimizar = "images\\minimizar.png"
    coordinates_minimizar = pyautogui.locateCenterOnScreen(minimizar)
    pyautogui.click(coordinates_minimizar)

def alterar_ambiente_scroll(ambiente, alterar, alterado):
    pyautogui.PAUSE = 0.5
    # Ambiente
    ambiente = f"images\\{ambiente}_ambiente.png"
    coordinates_ambiente = pyautogui.locateCenterOnScreen(ambiente)
    pyautogui.click(coordinates_ambiente) 
    sleep(5)

    scroll_down_ambientes()

    # Alterar
    pyautogui.PAUSE = 0.5
    sleep(3.5)
    alterar = f"images\\{alterar}_backup.png"
    coordinates_alterar = pyautogui.locateCenterOnScreen(alterar)
    pyautogui.doubleClick(coordinates_alterar)


    # Espera
    alterado = f"images\\{alterado}_alterado.png"
    while not esperar_imagem(alterado):
        sleep(0.1)
    clock()     

def clock():
    pyautogui.PAUSE = 0.5
    sleep(1.5)
    clock = "images\\clock.png"
    coordinates_clock = pyautogui.locateCenterOnScreen(clock)

    while not esperar_imagem("images\\clock.png"):
            sleep(1)
    pyautogui.click(coordinates_clock)
    minimizar = "images\\minimizar.png"
    coordinates_minimizar = pyautogui.locateCenterOnScreen(minimizar)
    pyautogui.click(coordinates_minimizar)

def acesso_smp():
    pyautogui.PAUSE = 0.5

    smp_path = "images\\smp.png"
    smp_selecionado_path = "images\\smp_selecionado.png"
    coordinates_smp = pyautogui.locateCenterOnScreen(smp_path)
    coordinates_smp_selecionado = pyautogui.locateCenterOnScreen(smp_selecionado_path)

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

    # Acesso DBACOCKPIT
    while not esperar_imagem("images\\lobby.png"):
            sleep(0.1)
    pyautogui.write('dbacockpit')
    pyautogui.press('Enter')
    while not esperar_imagem("images\\minimizar.png"):
            sleep(0.1)
    minimizar = "images\\minimizar.png"
    coordinates_used = pyautogui.locateCenterOnScreen(minimizar)
    pyautogui.click(minimizar)
    sleep(1)
    jobs = "images\\jobs.png"
    coordinates_used = pyautogui.locateCenterOnScreen(jobs)
    pyautogui.doubleClick(jobs)
    sleep(1)
    dba_logs = "images\\dba_logs.png"
    coordinates_used = pyautogui.locateCenterOnScreen(dba_logs)
    pyautogui.doubleClick(dba_logs)
    while not esperar_imagem("images\\lobby_bkp.png"):
            sleep(0.1)       

def acesso_pip_piq(ambiente):
     if ambiente == "piq":
        pyautogui.PAUSE = 1.5
        while not esperar_imagem("images\\piq.png"):
            sleep(0.1)
        piq = "images\\piq.png"
        coordinates_used = pyautogui.locateCenterOnScreen(piq)
        pyautogui.doubleClick(piq)
        while not esperar_imagem("images\\sap.png"):
            sleep(0.1)
        pyautogui.write(texto.upper())
        pyautogui.press('Tab')
        pyautogui.write('Mudar@2023')
        pyautogui.press('enter')
        pyautogui.press('enter')
        while not esperar_imagem("images\\lobby.png"):
            sleep(0.1)
        pyautogui.write('db14')    
        pyautogui.press('enter')
        while not esperar_imagem("images\\minimizar.png"):
            sleep(0.1)
        minimizar = "images\\minimizar.png"
        coordinates_used = pyautogui.locateCenterOnScreen(minimizar)    
        pyautogui.click(minimizar)
     elif ambiente == "pip":
        sleep(2)
        while not esperar_imagem("images\\pip.png"):
            sleep(0.1)
        pip = "images\\pip.png"
        coordinates_used = pyautogui.locateCenterOnScreen(pip)
        pyautogui.doubleClick(pip)
        while not esperar_imagem("images\\sap.png"):
            sleep(0.1)
        pyautogui.write(texto.upper())
        pyautogui.press('Tab')
        pyautogui.write('senha')
        pyautogui.press('enter')
        pyautogui.press('enter')
        while not esperar_imagem("images\\lobby.png"):
            sleep(0.1)
        pyautogui.write('db14')    
        pyautogui.press('enter')
        while not esperar_imagem("images\\minimizar.png"):
            sleep(0.1)
        minimizar = "images\\minimizar.png"
        coordinates_used = pyautogui.locateCenterOnScreen(minimizar)           
        pyautogui.click(minimizar)

def clicar_backup(a, b):
     pyautogui.PAUSE = 0.2
     backup_botao = "images\\backup_botao.png"
     coordinates_backup = pyautogui.locateCenterOnScreen(backup_botao)
     sleep(2)
     while not esperar_imagem("images\\backup_botao.png"):
          sleep(0.1)
     pyautogui.click(coordinates_backup)
     while not esperar_imagem("images\\transicao_bkp.png"):
            sleep(0.1)
     nome_arquivo = f"Prints\\Checklist Backup\\BACKUP/{a}.png"
     pyautogui.screenshot(nome_arquivo)
     pyautogui.press("esc")
     sleep(1)
     redolog_botao = "images\\redolog_botao.png"
     coordinates_redolog = pyautogui.locateCenterOnScreen(redolog_botao)
     while not esperar_imagem("images\\redolog_botao.png"):
          sleep(0.1)
     pyautogui.doubleClick(redolog_botao)
     while not esperar_imagem("images\\transicao_redolog.png"):
            sleep(0.1)
     nome_arquivo = f"Prints\\Checklist Backup\\REDOLOG/{b}.png"
     pyautogui.screenshot(nome_arquivo)
     sleep(1)

def fazer_full():
        acesso_smp()
        clicar_backup("BID", "BID")

        alterar_ambiente("bid", "bip", "bip")
        clicar_backup("BIP", "BIP")

        alterar_ambiente("bip", "csd", "csd")
        clicar_backup("CSD", "CSD")

        alterar_ambiente("csd", "csp", "csp")
        clicar_backup("CSP", "CSP")

        alterar_ambiente("csp", "csq", "csq")
        clicar_backup("CSQ", "CSQ")

        alterar_ambiente("csq", "ecd", "ecd")
        clicar_backup("ECD", "ECD")

        alterar_ambiente("ecd", "ecp", "ecp")
        clicar_backup("ECP", "ECP")

        alterar_ambiente("ecp", "epp", "epp")
        clicar_backup("EPP", "EPP")
    
        alterar_ambiente_scroll("epp", "epq", "epq")
        clicar_backup("EPQ", "EPQ")
        
        alterar_ambiente_scroll("epq", "pnd", "pnd")
        clicar_backup("PND", "PND")
        
        alterar_ambiente_scroll("pnd", "pnp", "pnp")
        clicar_backup("PNP", "PNP")
        
        alterar_ambiente_scroll("pnp", "pnq", "pnq")
        clicar_backup("PNQ", "PNQ")
    
        alterar_ambiente_scroll("pnq", "smd", "smd")
        clicar_backup("SMD", "SMD")
        
        alterar_ambiente_scroll("smd", "smp", "smp")
        clicar_backup("SMP", "SMP")
        
        alterar_ambiente_scroll("smp", "ssd", "ssd")
        clicar_backup("SSD", "SSD")
        
        alterar_ambiente_scroll("ssd", "ssp", "ssp")
        clicar_backup("SSP", "SSP")
        
        alterar_ambiente_scroll("ssp", "ssq", "ssq")
        clicar_backup("SSQ", "SSQ")

        # Saindo do DBACOCKPIT
        pyautogui.PAUSE = 1
        pyautogui.hotkey('alt', 'f4')
        sleep(1)
        pyautogui.press('Tab')
        pyautogui.press('enter')

        # PIQ
        acesso_pip_piq("piq")
        clicar_backup("PIQ", "PIQ")
        pyautogui.hotkey('alt', 'f4')
        pyautogui.press('Tab')
        sleep(0.1)
        pyautogui.press('enter')

        # PIP
        acesso_pip_piq("pip")
        clicar_backup("PIP", "PIP")
        pyautogui.hotkey('alt', 'f4')
        pyautogui.press('Tab')
        sleep(0.1)
        pyautogui.press('enter')

texto = 'usuario'

def backup_redolog():
    fazer_full()