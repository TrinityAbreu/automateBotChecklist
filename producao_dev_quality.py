import pyautogui
from time import sleep
import time
from PIL import ImageGrab
from datetime import datetime, timedelta
from pynput.mouse import Controller, Button
data_ontem = datetime.today() - timedelta(days=1)
data_ontem_formatada = data_ontem.strftime('%d.%m.2024')
data_ontem_string = str(data_ontem_formatada)
mouse = Controller()
texto = 'usuario'

def scroll_down():
    mouse.scroll(0, -10)

def tablespace_qualidade_dev():
        pyautogui.pause = 1
        while not esperar_imagem("images\\minimizar.png"):
                sleep(1)
        minimizar = "images\\minimizar.png"
        coordinates_minimizar = pyautogui.locateCenterOnScreen(minimizar)
        pyautogui.click(coordinates_minimizar)
        sleep(1)
        espaco = "images\\espaco.png"
        coordinates_espaco = pyautogui.locateCenterOnScreen(espaco)
        pyautogui.doubleClick(coordinates_espaco)
        sleep(1)
        tabblespace = "images\\tabblespace.png"
        coordinates_tabblespace = pyautogui.locateCenterOnScreen(tabblespace)
        pyautogui.doubleClick(coordinates_tabblespace)
        sleep(1)
        pyautogui.press('down')
        over = "images\\overview.png"
        coordinates_over = pyautogui.locateCenterOnScreen(over)
        sleep(0.5)
        pyautogui.doubleClick(coordinates_over)
        sleep(2)
        while not esperar_imagem("images\\used.png"):
                sleep(1)
        used = r"images\\used.png"
        coordinates_used = pyautogui.locateCenterOnScreen(used)
        pyautogui.rightClick(coordinates_used)
        while not esperar_imagem("images\\decrescente.png"):
                sleep(1)
        decrescente = "images\\decrescente.png"
        coordinates_decrescente = pyautogui.locateCenterOnScreen(decrescente)
        pyautogui.click(coordinates_decrescente)
        sleep(0.5)

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

def STMS_SMP():
    pyautogui.PAUSE = 1
    pyautogui.write('STMS')
    pyautogui.press('enter')
    while not esperar_imagem("images\\transporte.png"):
        sleep(1)
    pyautogui.press('f5')
    while not esperar_imagem("images\\sintese.png"):
        sleep(1)
    pyautogui.hotkey('Shift','f6')
    sleep(1)
    pyautogui.hotkey('Shift','Tab')
    sleep(1)
    pyautogui.press('enter')
    # Acesso
    pyautogui.PAUSE = 0.2
    sleep(0.5)
    pyautogui.press('Tab')
    sleep(0.5)
    pyautogui.write('senha')
    sleep(0.5)
    pyautogui.press('Enter')
    sleep(5)
    # 1 Attemp
    pyautogui.press('Tab')
    sleep(0.5)
    pyautogui.write('senha')
    sleep(0.5)
    pyautogui.press('Enter')
    sleep(5)
    # 2 Attemp
    pyautogui.press('Tab')
    sleep(0.5)
    pyautogui.write('senha')
    sleep(0.5)
    pyautogui.press('Enter')
    sleep(5)
    # 3 Attemp
    sleep(1)
    pyautogui.press('Tab')
    sleep(0.5)
    pyautogui.write('senha')
    sleep(0.5)
    pyautogui.press('Enter')
    sleep(3)
    while not esperar_imagem("images\\tms.png"):
        sleep(1)   
    nome_arquivo = "Prints\\PRODUÇÃO\\SMP - 704. BBMAPFRE - SOLMAN PRODUÇÃO/STMS.png"
    pyautogui.screenshot(nome_arquivo)
    sleep(2)
    pyautogui.hotkey('Shift','f3')
    sleep(1)
    pyautogui.hotkey('Shift','f3')
    sleep(1)
    pyautogui.hotkey('Shift','f3')
    while not esperar_imagem("images\\lobby.png"):
        sleep(1)
    sleep(1)

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

def producao(diretorio, ambiente):
    if ambiente == "BIP":
        acesso("bip_producao", "senha")
        sleep(1)
    elif ambiente == "ECP":
        acesso("ecp_producao", "senha")    
        sleep(1)
    elif ambiente == "PIP":
        acesso("pip_producao", "senha")
        sleep(1)
    elif ambiente == "PNP":
        acesso("pnp_producao", "senha")
        sleep(1)    
    elif ambiente == "SMP":
        acesso("smp", "senha")
        sleep(1)

    if ambiente == "ECP":
         def SOST_SM51():
            pyautogui.PAUSE = 0.5
            pyautogui.write('SOST')
            pyautogui.press('enter')
            while not esperar_imagem("images\\atualizar.png"):
                sleep(1)
            atualizar = "images\\atualizar.png"
            coordinates_atualizar = pyautogui.locateCenterOnScreen(atualizar)
            pyautogui.doubleClick(coordinates_atualizar)
            sleep(0.5)
            nome_arquivo = f"{diretorio}/SOST.png"
            pyautogui.screenshot(nome_arquivo)
            pyautogui.hotkey('Shift','f3')
            while not esperar_imagem("images\\lobby.png"):
                sleep(1)
            sleep(1)

            # SM51 
            pyautogui.write('SM51')
            pyautogui.press('enter')
            while not esperar_imagem("images\\instancia.png"):
                sleep(1)
            sleep(0.5)
            nome_arquivo = f"{diretorio}/SM51.png"
            pyautogui.screenshot(nome_arquivo)
            pyautogui.hotkey('Shift','f3')
            while not esperar_imagem("images\\lobby.png"):
                sleep(1)
            sleep(1)
         SOST_SM51()   

    # ST22
    def ST22():
        pyautogui.PAUSE = 0.5
        pyautogui.write('ST22')
        pyautogui.press('Enter')
        while not esperar_imagem("images\\hoje.png"):
            sleep(1)
        hoje = "images\\hoje.png"
        coordinates_hoje = pyautogui.locateCenterOnScreen(hoje)
        pyautogui.click(coordinates_hoje)
        sleep(1)
        nome_arquivo = f"{diretorio}/ST22.png"
        pyautogui.screenshot(nome_arquivo)
        sleep(1)
        pyautogui.hotkey('Shift', 'f3')
    ST22()

    # DB01
    def DB01():
        pyautogui.PAUSE = 0.5
        pyautogui.write('DB01')
        pyautogui.press('Enter')
        while not esperar_imagem("images\\oracle.png"):
            sleep(0.1)
        nome_arquivo = f"{diretorio}/DB01.png"
        sleep(1)
        pyautogui.screenshot(nome_arquivo)
        pyautogui.hotkey('Shift','f3')
        while not esperar_imagem("images\\lobby.png"):
            sleep(0.1)
    DB01()

    # SM12
    def SM12():
        pyautogui.PAUSE = 0.5
        pyautogui.write('SM12')
        pyautogui.press('enter')
        while not esperar_imagem("images\\bloqueio.png"):
            sleep(1)
        pyautogui.PAUSE = 0.1
        pyautogui.write('*')
        pyautogui.press('Tab')
        pyautogui.write('*')
        pyautogui.press('Tab')
        pyautogui.press('Tab')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write('*')
        pyautogui.press('enter')
        while not esperar_imagem("images\\detalhes.png"):
            sleep(0.1)
        sleep(1)
        pyautogui.PAUSE = 0.5
        nome_arquivo = f"{diretorio}/SM12.png"
        pyautogui.screenshot(nome_arquivo)
        pyautogui.hotkey('Shift','f3')
        sleep(1)
        while not esperar_imagem("images\\bloqueio.png"):
            sleep(0.1)
        pyautogui.hotkey('Shift','f3')
        while not esperar_imagem("images\\lobby.png"):
            sleep(0.1)
    SM12()

    # SM13
    def SM13():
        pyautogui.PAUSE = 0.5
        pyautogui.write('SM13')
        pyautogui.press('enter')
        while not esperar_imagem("images\\relogio.png"):
            sleep(1)
        pyautogui.press('enter')
        while not esperar_imagem("images\\atualizacao.png"):
            sleep(0.1)
        sleep(1)
        nome_arquivo = f"{diretorio}/SM13.png"
        pyautogui.screenshot(nome_arquivo)
        pyautogui.hotkey('Shift','f3')
        while not esperar_imagem("images\\relogio.png"):
            sleep(0.1)
        pyautogui.hotkey('Shift','f3')
        sleep(1)
        while not esperar_imagem("images\\lobby.png"):
            sleep(0.1)
    SM13()

    # ST06 
    if ambiente == "ECP":
        def ST06_ECP():
            pyautogui.PAUSE = 0.5
            pyautogui.write('ST06')
            pyautogui.press('enter')
            while not esperar_imagem("images\\sistemas_files.png"):
                sleep(1)
            sistemas_files = "images\\sistemas_files.png"
            coordinates_sistemas_files = pyautogui.locateCenterOnScreen(sistemas_files)
            pyautogui.click(coordinates_sistemas_files)
            while not esperar_imagem("images\\livre.png"):
                sleep(1)
            livre = "images\\livre.png"
            coordinates_livre = pyautogui.locateCenterOnScreen(livre)
            pyautogui.rightClick(coordinates_livre)
            while not esperar_imagem("images\\crescente.png"):
                sleep(1)
            crescente = "images\\crescente.png"
            coordinates_crescente = pyautogui.locateCenterOnScreen(crescente)
            pyautogui.click(coordinates_crescente)
            sleep(0.5)
            nome_arquivo = f"{diretorio}/ST06_ECP03.png"
            pyautogui.screenshot(nome_arquivo)
            sleep(1)

            # ECP_00
            ecp_00 = "images\\ecp_00.png"
            coordinates_ecp_00 = pyautogui.locateCenterOnScreen(ecp_00)
            pyautogui.click(coordinates_ecp_00)
            while not esperar_imagem("images\\livre.png"):
                sleep(1)
            livre = "images\\livre.png"
            coordinates_livre = pyautogui.locateCenterOnScreen(livre)
            pyautogui.rightClick(livre)
            while not esperar_imagem("images\\crescente.png"):
                sleep(1)
            crescente = "images\\crescente.png"
            coordinates_crescente = pyautogui.locateCenterOnScreen(crescente)
            pyautogui.click(coordinates_crescente)
            sleep(0.5)
            nome_arquivo = f"{diretorio}/ST06_ECP00.png"
            pyautogui.screenshot(nome_arquivo)
            sleep(1)

            # ECP_04
            ecp_04 = "images\\ecp_04.png"
            coordinates_ecp_04 = pyautogui.locateCenterOnScreen(ecp_04)
            pyautogui.click(coordinates_ecp_04)
            while not esperar_imagem("images\\livre.png"):
                sleep(1)
            livre = "images\\livre.png"
            coordinates_livre = pyautogui.locateCenterOnScreen(livre)
            pyautogui.rightClick(livre)
            while not esperar_imagem("images\\crescente.png"):
                sleep(1)
            crescente = "images\\crescente.png"
            coordinates_crescente = pyautogui.locateCenterOnScreen(crescente)
            pyautogui.click(coordinates_crescente)
            sleep(0.5)
            nome_arquivo = f"{diretorio}/ST06_ECP04.png"
            pyautogui.screenshot(nome_arquivo)
            sleep(1)

            # ECP_05
            ecp_05 = "images\\ecp_05.png"
            coordinates_ecp_05 = pyautogui.locateCenterOnScreen(ecp_05)
            pyautogui.click(coordinates_ecp_05)
            while not esperar_imagem("images\\livre.png"):
                sleep(1)
            livre = "images\\livre.png"
            coordinates_livre = pyautogui.locateCenterOnScreen(livre)
            pyautogui.rightClick(livre)
            while not esperar_imagem("images\\crescente.png"):
                sleep(1)
            crescente = "images\\crescente.png"
            coordinates_crescente = pyautogui.locateCenterOnScreen(crescente)
            pyautogui.click(coordinates_crescente)
            sleep(0.5)
            nome_arquivo = f"{diretorio}/ST06_ECP05.png"
            pyautogui.screenshot(nome_arquivo)
            sleep(1)
            pyautogui.hotkey('Shift','f3')
            while not esperar_imagem("images\\lobby.png"):
                sleep(1)
            sleep(1)
        ST06_ECP()

    elif ambiente == "SMP":
        def ST06_SMP():
            pyautogui.PAUSE = 0.5
            pyautogui.write('ST06')
            pyautogui.press('enter')
            while not esperar_imagem("images\\sistemas_files.png"):
                sleep(1)
            sistemas_files = "images\\sistemas_files.png"
            coordinates_sistemas_files = pyautogui.locateCenterOnScreen(sistemas_files)
            pyautogui.click(coordinates_sistemas_files)
            while not esperar_imagem("images\\livre.png"):
                sleep(1)
            livre = "images\\livre.png"
            coordinates_livre = pyautogui.locateCenterOnScreen(livre)
            pyautogui.rightClick(coordinates_livre)
            while not esperar_imagem("images\\crescente.png"):
                sleep(1)
            crescente = "images\\crescente.png"
            coordinates_crescente = pyautogui.locateCenterOnScreen(crescente)
            pyautogui.click(coordinates_crescente)
            sleep(0.5)
            nome_arquivo = f"{diretorio}/ST06_SMP05.png"
            pyautogui.screenshot(nome_arquivo)
            sleep(1)

            # SMP 00
            smp_00 = "images\\smp_00.png"
            coordinates_smp_00 = pyautogui.locateCenterOnScreen(smp_00)
            pyautogui.click(coordinates_smp_00)
            while not esperar_imagem("images\\livre.png"):
                sleep(1)
            livre = "images\\livre.png"
            coordinates_livre = pyautogui.locateCenterOnScreen(livre)
            pyautogui.rightClick(coordinates_livre)
            while not esperar_imagem("images\\crescente.png"):
                sleep(1)
            crescente = "images\\crescente.png"
            coordinates_crescente = pyautogui.locateCenterOnScreen(crescente)
            pyautogui.click(coordinates_crescente)
            sleep(0.5)
            nome_arquivo = f"{diretorio}/ST06_SMP00.png"
            pyautogui.screenshot(nome_arquivo)
            sleep(1)
            pyautogui.hotkey('Shift','f3')
            while not esperar_imagem("images\\lobby.png"):
                sleep(1)
        ST06_SMP()

    elif ambiente == "PIP":
        def ST06_PIP():
            pyautogui.PAUSE = 0.5
            pyautogui.write('ST06')
            pyautogui.press('enter')
            while not esperar_imagem("images\\sistemas_files.png"):
                sleep(1)
            sistemas_files = "images\\sistemas_files.png"
            coordinates_sistemas_files = pyautogui.locateCenterOnScreen(sistemas_files)
            pyautogui.click(coordinates_sistemas_files)
            while not esperar_imagem("images\\livre.png"):
                sleep(1)
            livre = "images\\livre.png"
            coordinates_livre = pyautogui.locateCenterOnScreen(livre)
            pyautogui.rightClick(coordinates_livre)
            while not esperar_imagem("images\\crescente.png"):
                sleep(1)
            crescente = "images\\crescente.png"
            coordinates_crescente = pyautogui.locateCenterOnScreen(crescente)
            pyautogui.click(coordinates_crescente)
            sleep(0.5)
            nome_arquivo = f"{diretorio}/ST06.png"
            pyautogui.screenshot(nome_arquivo)
            sleep(1)
            pyautogui.hotkey('Shift','f3')
            while not esperar_imagem("images\\lobby.png"):
                sleep(1)
            sleep(1)
        ST06_PIP()

    elif ambiente == "PNP":
        def ST06_PNP():
            pyautogui.PAUSE = 0.5
            pyautogui.write('ST06')
            pyautogui.press('enter')
            while not esperar_imagem("images\\sistemas_files.png"):
                sleep(1)
            sistemas_files = "images\\sistemas_files.png"
            coordinates_sistemas_files = pyautogui.locateCenterOnScreen(sistemas_files)
            pyautogui.click(coordinates_sistemas_files)
            while not esperar_imagem("images\\livre.png"):
                sleep(1)
            livre = "images\\livre.png"
            coordinates_livre = pyautogui.locateCenterOnScreen(livre)
            pyautogui.rightClick(coordinates_livre)
            while not esperar_imagem("images\\crescente.png"):
                sleep(1)
            crescente = "images\\crescente.png"
            coordinates_crescente = pyautogui.locateCenterOnScreen(crescente)
            pyautogui.click(coordinates_crescente)
            sleep(0.5)
            nome_arquivo = f"{diretorio}/ST06.png"
            pyautogui.screenshot(nome_arquivo)
            sleep(1)
            pyautogui.hotkey('Shift','f3')
            while not esperar_imagem("images\\lobby.png"):
                sleep(1)
            sleep(1)
        ST06_PNP()

    else:
        def ST06():
            pyautogui.PAUSE = 0.5
            pyautogui.write('ST06')
            pyautogui.press('enter')
            while not esperar_imagem("images\\sistemas_files.png"):
                sleep(1)
            sistemas_files = "images\\sistemas_files.png"
            coordinates_sistemas_files = pyautogui.locateCenterOnScreen(sistemas_files)
            pyautogui.click(coordinates_sistemas_files)
            while not esperar_imagem("images\\livre.png"):
                sleep(1)
            livre = "images\\livre.png"
            coordinates_livre = pyautogui.locateCenterOnScreen(livre)
            pyautogui.rightClick(coordinates_livre)
            while not esperar_imagem("images\\crescente.png"):
                sleep(1)
            crescente = "images\\crescente.png"
            coordinates_crescente = pyautogui.locateCenterOnScreen(crescente)
            pyautogui.click(coordinates_crescente)
            sleep(0.5)
            nome_arquivo = f"{diretorio}/ST06.png"
            pyautogui.screenshot(nome_arquivo)
            sleep(1)
            pyautogui.hotkey('Shift','f3')
            while not esperar_imagem("images\\lobby.png"):
                sleep(1)
        ST06()

    # STMS
    if ambiente == "SMP":
        STMS_SMP()
    else:
        def STMS():
            pyautogui.PAUSE = 0.5
            pyautogui.write('STMS')
            pyautogui.press('enter')
            transporte = "images\\transporte.png"
            while not esperar_imagem(transporte):
                sleep(1)
            sleep(1)
            pyautogui.press('f5')
            sleep(1)
            sintese = "images\\sintese.png"
            while not esperar_imagem(sintese):
                sleep(1)
            pyautogui.hotkey('Shift','f6')
            sleep(1)
            pyautogui.hotkey('Shift','Tab')
            sleep(1)
            pyautogui.press('enter')
            tms = "images\\tms.png"
            while not esperar_imagem(tms):
                sleep(1)
            sleep(1)
            nome_arquivo = f"{diretorio}/STMS.png"
            pyautogui.screenshot(nome_arquivo)
            pyautogui.hotkey('Shift','f3')
            sleep(2)
            pyautogui.hotkey('Shift','f3')
            sleep(2)
            pyautogui.hotkey('Shift','f3')
            while not esperar_imagem("images\\lobby.png"):
                sleep(1)
        STMS()

    # ST04
    def ST04():
        pyautogui.PAUSE = 1
        pyautogui.write('ST04')
        pyautogui.press('enter')
        while not esperar_imagem("images\\day.png"):
            sleep(1)
        day = ("images\\day.png")
        coordinates_day = pyautogui.locateCenterOnScreen(day)
        pyautogui.click(coordinates_day)
        sleep(1)
        scroll_down()
        sleep(0.5)
        nome_arquivo = f"{diretorio}/ST04.png"
        pyautogui.screenshot(nome_arquivo)
    ST04()

    if ambiente == "BIP":
        def ST04_BIP():
            pyautogui.PAUSE = 1
            tablespace_qualidade_dev()
            nome_arquivo = f"{diretorio}/DB02.png"
            nome_arquivo_table = ("Prints\\TABLESPACE/BIP.png")
            pyautogui.screenshot(nome_arquivo)
            sleep(0.5)
            pyautogui.screenshot(nome_arquivo_table)
            pyautogui.PAUSE = 0.5
            pyautogui.hotkey('Shift','f3')
            sleep(0.3)
            while not esperar_imagem("images\\lobby.png"):
                    sleep(1)
            sleep(1)
        ST04_BIP()

    elif ambiente == "PNP":
        def ST04_PNP():
            pyautogui.PAUSE = 1
            tablespace_qualidade_dev()
            nome_arquivo = f"{diretorio}/DB02.png"
            nome_arquivo_table = ("Prints\\TABLESPACE/PNP.png")
            pyautogui.screenshot(nome_arquivo)
            pyautogui.screenshot(nome_arquivo_table)
            pyautogui.PAUSE = 0.5
            pyautogui.hotkey('Shift','f3')
            sleep(0.3)
            while not esperar_imagem("images\\lobby.png"):
                    sleep(1)
            sleep(1)
        ST04_PNP()

    elif ambiente == "SMP":
        def ST04_SMP():
            pyautogui.PAUSE = 1
            tablespace_qualidade_dev()
            nome_arquivo = f"{diretorio}/DB02.png"
            nome_arquivo_table = ("Prints\\TABLESPACE/SMP.png")
            pyautogui.screenshot(nome_arquivo)
            pyautogui.screenshot(nome_arquivo_table)
            pyautogui.PAUSE = 0.5
            pyautogui.hotkey('Shift','f3')
            sleep(0.3)
            while not esperar_imagem("images\\lobby.png"):
                    sleep(1)
            sleep(1)
        ST04_SMP()

    elif ambiente == "PIP":
        def ST04_PIP():
            pyautogui.PAUSE = 0.5
            tablespace_qualidade_dev()
            nome_arquivo = f"{diretorio}/DB02.png"
            nome_arquivo_table = ("Prints\\TABLESPACE/PIP.png")
            pyautogui.screenshot(nome_arquivo)
            pyautogui.screenshot(nome_arquivo_table)
            pyautogui.PAUSE = 0.5
            pyautogui.hotkey('Shift','f3')
            sleep(0.3)
            while not esperar_imagem("images\\lobby.png"):
                    sleep(1)
            sleep(1)
        ST04_PIP()

    else:
        def ST04():
            pyautogui.PAUSE = 0.5
            tablespace_qualidade_dev()
            nome_arquivo = f"{diretorio}/DB02.png"
            pyautogui.screenshot(nome_arquivo)
            pyautogui.PAUSE = 0.5
            pyautogui.hotkey('Shift','f3')
            sleep(0.3)
            while not esperar_imagem("images\\lobby.png"):
                    sleep(1)
            sleep(1)
        ST04()

    # SM58
    if ambiente == "ECP":
         pass
    else:
        def SM58():
            pyautogui.PAUSE = 0.5
            pyautogui.write('SM58')
            pyautogui.press('Enter')
            while not esperar_imagem("images\\rfc.png"):
                    sleep(1)
            pyautogui.write(data_ontem_string)
            sleep(0.3)
            pyautogui.PAUSE = 0.1
            pyautogui.press('Tab')
            pyautogui.press('Tab')
            pyautogui.press('Tab')
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.write('*')
            pyautogui.press('f8')
            sleep(1)
            nome_arquivo = f"{diretorio}/SM58.png"
            pyautogui.screenshot(nome_arquivo)
            pyautogui.PAUSE = 1
            pyautogui.hotkey('Shift','f3')
            sleep(0.3)
            pyautogui.hotkey('Shift','f3')
            sleep(0.3)
            while not esperar_imagem("images\\lobby.png"):
                    sleep(1)
            sleep(1)
        SM58()

    # SM37
    def SM37():
        pyautogui.PAUSE = 0.5
        pyautogui.write('SM37')
        pyautogui.press('enter')
        pyautogui.PAUSE = 0.1
        while not esperar_imagem("images\\selecao.png"):
                sleep(1)
        pyautogui.write('SAP_*')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write('*')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('space') 
        pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.PAUSE = 1
        pyautogui.press('f8')
        sleep(1)
        nome_arquivo = f"{diretorio}/SM37.png"
        pyautogui.screenshot(nome_arquivo)
        sleep(1)
        pyautogui.hotkey('Shift','f3')
        sleep(1)
        pyautogui.hotkey('Shift','f3')
        sleep(1)
        pyautogui.press("enter")
        while not esperar_imagem("images\\lobby.png"):
            sleep(1)
        sleep(1)
    SM37()

    # SM66
    def SM66():
        pyautogui.PAUSE = 0.5
        pyautogui.write('SM66')
        pyautogui.press('enter')
        sleep(3)
        tmp = "images\\tmp.png"
        coordinates_tmp = pyautogui.locateCenterOnScreen(tmp)
        duracao = "images\\duracao.png"
        coordinates_duracao = pyautogui.locateCenterOnScreen(duracao)
        if coordinates_tmp:
            pyautogui.rightClick(tmp)
        else:
            pyautogui.rightClick(duracao)        
        sleep(1)
        decrescente = "images\\decrescente.png"
        coordinates_decrescente = pyautogui.locateCenterOnScreen(decrescente)
        pyautogui.click(coordinates_decrescente)
        sleep(2)
        nome_arquivo = f"{diretorio}/SM66.png"
        pyautogui.screenshot(nome_arquivo)
        pyautogui.PAUSE = 0.5
        pyautogui.hotkey('alt', 'f4')
        sleep(1)
        pyautogui.press('Tab')
        pyautogui.press('enter')
    SM66()

def qualidade(diretorio, ambiente):
    if ambiente == "BIQ":
        acesso("biq", "senha")

    elif ambiente == "ECQ":
        acesso("ecq_qualidade", "senha")

    elif ambiente == "PIQ":
        acesso("piq", "Mudar@2023")

    elif ambiente == "PNQ":
        acesso("pnq", "senha")

    # ST22
    def ST22():
        pyautogui.PAUSE = 0.5
        pyautogui.write('ST22')
        pyautogui.press('Enter')
        while not esperar_imagem("images\\hoje.png"):
            sleep(1)
        hoje = "images\\hoje.png"
        coordinates_hoje = pyautogui.locateCenterOnScreen(hoje)
        pyautogui.click(coordinates_hoje)
        sleep(1)
        nome_arquivo = f"{diretorio}/ST22.png"
        pyautogui.screenshot(nome_arquivo)
        sleep(1)
        pyautogui.hotkey('Shift', 'f3')
    ST22()

    # SM12
    def SM12():
        pyautogui.PAUSE = 0.5
        pyautogui.write('SM12')
        pyautogui.press('enter')
        while not esperar_imagem("images\\bloqueio.png"):
            sleep(1)
        pyautogui.PAUSE = 0.1
        pyautogui.write('*')
        pyautogui.press('Tab')
        pyautogui.write('*')
        pyautogui.press('Tab')
        pyautogui.press('Tab')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write('*')
        pyautogui.press('enter')
        while not esperar_imagem("images\\detalhes.png"):
            sleep(0.1)
        sleep(1)
        pyautogui.PAUSE = 0.5
        nome_arquivo = f"{diretorio}/SM12.png"
        pyautogui.screenshot(nome_arquivo)
        pyautogui.hotkey('Shift','f3')
        sleep(1)
        while not esperar_imagem("images\\bloqueio.png"):
            sleep(0.1)
        pyautogui.hotkey('Shift','f3')
        while not esperar_imagem("images\\lobby.png"):
            sleep(0.1)
    SM12()

    # SM13
    def SM13():
        pyautogui.PAUSE = 0.5
        pyautogui.write('SM13')
        pyautogui.press('enter')
        while not esperar_imagem("images\\relogio.png"):
            sleep(1)
        pyautogui.press('enter')
        while not esperar_imagem("images\\atualizacao.png"):
            sleep(0.1)
        sleep(1)
        nome_arquivo = f"{diretorio}/SM13.png"
        pyautogui.screenshot(nome_arquivo)
        pyautogui.hotkey('Shift','f3')
        while not esperar_imagem("images\\relogio.png"):
            sleep(0.1)
        pyautogui.hotkey('Shift','f3')
        sleep(1)
        while not esperar_imagem("images\\lobby.png"):
            sleep(0.1)
    SM13()

    # ST06
    def ST06():
        pyautogui.PAUSE = 0.5
        pyautogui.write('ST06')
        pyautogui.press('enter')
        while not esperar_imagem("images\\sistemas_files.png"):
            sleep(1)
        sistemas_files = "images\\sistemas_files.png"
        coordinates_sistemas_files = pyautogui.locateCenterOnScreen(sistemas_files)
        pyautogui.click(coordinates_sistemas_files)
        while not esperar_imagem("images\\livre.png"):
            sleep(1)
        livre = "images\\livre.png"
        coordinates_livre = pyautogui.locateCenterOnScreen(livre)
        pyautogui.rightClick(coordinates_livre)
        while not esperar_imagem("images\\crescente.png"):
            sleep(1)
        crescente = "images\\crescente.png"
        coordinates_crescente = pyautogui.locateCenterOnScreen(crescente)
        pyautogui.click(coordinates_crescente)
        sleep(0.5)
        nome_arquivo = f"{diretorio}/ST06.png"
        pyautogui.screenshot(nome_arquivo)
        sleep(1)
        pyautogui.hotkey('Shift','f3')
        while not esperar_imagem("images\\lobby.png"):
            sleep(1)
    ST06()

     # ST04 - Tablespace - BIQ, PIQ, ECQ, PNQ

    if ambiente == "BIQ":
        def ST04_BIQ():
            pyautogui.PAUSE = 0.5
            pyautogui.write('ST04')
            pyautogui.press('enter')
            tablespace_qualidade_dev()
            pyautogui.screenshot("Prints\\TABLESPACE/BIQ.png")
            pyautogui.PAUSE = 0.5
            pyautogui.hotkey('Shift','f3')
            sleep(0.3)
            while not esperar_imagem("images\\lobby.png"):
                    sleep(1)
            sleep(1)
        ST04_BIQ()

    elif ambiente == "PIQ":
        def ST04_PIQ():
            pyautogui.PAUSE = 0.5
            pyautogui.write('ST04')
            pyautogui.press('enter')
            tablespace_qualidade_dev()
            pyautogui.screenshot("Prints\\TABLESPACE/PIQ.png")
            pyautogui.PAUSE = 0.5
            pyautogui.hotkey('Shift','f3')
            sleep(0.3)
            while not esperar_imagem("images\\lobby.png"):
                    sleep(1)
            sleep(1)
        ST04_PIQ()

    elif ambiente == "ECQ":
        def ST04_ECQ():
            pyautogui.PAUSE = 0.5
            pyautogui.write('ST04')
            pyautogui.press('enter')
            tablespace_qualidade_dev()
            pyautogui.screenshot("Prints\\TABLESPACE/ECQ.png")
            pyautogui.PAUSE = 0.5
            pyautogui.hotkey('Shift','f3')
            sleep(0.3)
            while not esperar_imagem("images\\lobby.png"):
                    sleep(1)
            sleep(1)
        ST04_ECQ()

    elif ambiente == "PNQ":
        def ST04_PNQ():
            pyautogui.PAUSE = 0.5
            pyautogui.write('ST04')
            pyautogui.press('enter')
            tablespace_qualidade_dev()
            pyautogui.screenshot("Prints\\TABLESPACE/PNQ.png")
            pyautogui.PAUSE = 0.5
            pyautogui.hotkey('Shift','f3')
            sleep(0.3)
            while not esperar_imagem("images\\lobby.png"):
                    sleep(1)
            sleep(1)

    # SM66
    def SM66():
        pyautogui.PAUSE = 0.5
        pyautogui.write('SM66')
        pyautogui.press('enter')
        sleep(3)
        tmp = "images\\tmp.png"
        coordinates_tmp = pyautogui.locateCenterOnScreen(tmp)
        duracao = "images\\duracao.png"
        coordinates_duracao = pyautogui.locateCenterOnScreen(duracao)
        if coordinates_tmp:
            pyautogui.rightClick(tmp)
        else:
            pyautogui.rightClick(duracao)        
        sleep(1)
        decrescente = "images\\decrescente.png"
        coordinates_decrescente = pyautogui.locateCenterOnScreen(decrescente)
        pyautogui.click(coordinates_decrescente)
        sleep(2)
        nome_arquivo = f"{diretorio}/SM66.png"
        pyautogui.screenshot(nome_arquivo)
        pyautogui.PAUSE = 0.5
        pyautogui.hotkey('alt', 'f4')
        sleep(1)
        pyautogui.press('Tab')
        pyautogui.press('enter')
    SM66()

def desenvolvimento(diretorio, ambiente):
    if ambiente == "BID":
        acesso("bid", "senha")

    elif ambiente == "ECD":
        acesso("ecd", "senha")

    elif ambiente == "PID":
        acesso("pid", "senha")

    elif ambiente == "PND":
        acesso("pnd_desenvolvimento", "senha")

    elif ambiente == "SMD":
        acesso("smd", "senha")
 
    # ST22
    def ST22():
        pyautogui.PAUSE = 0.5
        pyautogui.write('ST22')
        pyautogui.press('Enter')
        while not esperar_imagem("images\\hoje.png"):
            sleep(1)
        hoje = "images\\hoje.png"
        coordinates_hoje = pyautogui.locateCenterOnScreen(hoje)
        pyautogui.click(coordinates_hoje)
        sleep(1)
        nome_arquivo = f"{diretorio}/ST22.png"
        pyautogui.screenshot(nome_arquivo)
        sleep(1)
        pyautogui.hotkey('Shift', 'f3')
    ST22()

    # SM12
    def SM12():
        pyautogui.PAUSE = 0.5
        pyautogui.write('SM12')
        pyautogui.press('enter')
        while not esperar_imagem("images\\bloqueio.png"):
            sleep(1)
        pyautogui.PAUSE = 0.1
        pyautogui.write('*')
        pyautogui.press('Tab')
        pyautogui.write('*')
        pyautogui.press('Tab')
        pyautogui.press('Tab')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write('*')
        pyautogui.press('enter')
        while not esperar_imagem("images\\detalhes.png"):
            sleep(0.1)
        sleep(1)
        pyautogui.PAUSE = 0.5
        nome_arquivo = f"{diretorio}/SM12.png"
        pyautogui.screenshot(nome_arquivo)
        pyautogui.hotkey('Shift','f3')
        sleep(1)
        while not esperar_imagem("images\\bloqueio.png"):
            sleep(0.1)
        pyautogui.hotkey('Shift','f3')
        while not esperar_imagem("images\\lobby.png"):
            sleep(0.1)
    SM12()

    # SM13
    def SM13():
        pyautogui.PAUSE = 0.5
        pyautogui.write('SM13')
        pyautogui.press('enter')
        while not esperar_imagem("images\\relogio.png"):
            sleep(1)
        pyautogui.press('enter')
        while not esperar_imagem("images\\atualizacao.png"):
            sleep(0.1)
        sleep(1)
        nome_arquivo = f"{diretorio}/SM13.png"
        pyautogui.screenshot(nome_arquivo)
        pyautogui.hotkey('Shift','f3')
        while not esperar_imagem("images\\relogio.png"):
            sleep(0.1)
        pyautogui.hotkey('Shift','f3')
        sleep(1)
        while not esperar_imagem("images\\lobby.png"):
            sleep(0.1)
    SM13()

    # ST06
    def ST06():
        pyautogui.PAUSE = 0.5
        pyautogui.write('ST06')
        pyautogui.press('enter')
        while not esperar_imagem("images\\sistemas_files.png"):
            sleep(1)
        sistemas_files = "images\\sistemas_files.png"
        coordinates_sistemas_files = pyautogui.locateCenterOnScreen(sistemas_files)
        pyautogui.click(coordinates_sistemas_files)
        while not esperar_imagem("images\\livre.png"):
            sleep(1)
        livre = "images\\livre.png"
        coordinates_livre = pyautogui.locateCenterOnScreen(livre)
        pyautogui.rightClick(coordinates_livre)
        while not esperar_imagem("images\\crescente.png"):
            sleep(1)
        crescente = "images\\crescente.png"
        coordinates_crescente = pyautogui.locateCenterOnScreen(crescente)
        pyautogui.click(coordinates_crescente)
        sleep(0.5)
        nome_arquivo = f"{diretorio}/ST06.png"
        pyautogui.screenshot(nome_arquivo)
        sleep(1)
        pyautogui.hotkey('Shift','f3')
        while not esperar_imagem("images\\lobby.png"):
            sleep(1)
    ST06()

    if ambiente == "SMD":
      def ST04_SMD():
            pyautogui.PAUSE = 0.5
            pyautogui.write('ST04')
            pyautogui.press('enter')
            tablespace_qualidade_dev()
            pyautogui.screenshot("Prints\\TABLESPACE/SMD.png")
            pyautogui.PAUSE = 0.5
            sleep(1)
            pyautogui.hotkey('Shift','f3')
            sleep(1)
            while not esperar_imagem("images\\lobby.png"):
                    sleep(1)
      ST04_SMD()

    # SM66
    def SM66():
        pyautogui.PAUSE = 0.5
        pyautogui.write('SM66')
        pyautogui.press('enter')
        sleep(3)
        tmp = "images\\tmp.png"
        coordinates_tmp = pyautogui.locateCenterOnScreen(tmp)
        duracao = "images\\duracao.png"
        coordinates_duracao = pyautogui.locateCenterOnScreen(duracao)
        if coordinates_tmp:
            pyautogui.rightClick(tmp)
        else:
            pyautogui.rightClick(duracao)        
        sleep(1)
        decrescente = "images\\decrescente.png"
        coordinates_decrescente = pyautogui.locateCenterOnScreen(decrescente)
        pyautogui.click(coordinates_decrescente)
        sleep(2)
        nome_arquivo = f"{diretorio}/SM66.png"
        pyautogui.screenshot(nome_arquivo)
        pyautogui.PAUSE = 0.5
        pyautogui.hotkey('alt', 'f4')
        sleep(1)
        pyautogui.press('Tab')
        pyautogui.press('enter')
    SM66()

