import tkinter as tk
from tkinter import Label, Button, ttk
from tkinter import messagebox
from time import sleep
from tkinter import Frame
from ttkthemes import ThemedTk
from tkinter import messagebox, simpledialog
import shutil
import os
import datetime
from producao_dev_quality import producao, qualidade, desenvolvimento
from backup_redolog import backup_redolog
from tabblespace import tablespace

def zipar_e_mover_backup_redolog(lista_pastas_bkp, pasta_destino_bkp):
    agora = datetime.datetime.now()
    data_hora_atual = agora.strftime("%d_%m_%Y_%H00")

    for nome_da_pasta in lista_pastas_bkp:
        pasta_a_zipar_bkp = os.path.abspath(nome_da_pasta)
        nome_arquivo_zip_bkp = f'{os.path.basename(nome_da_pasta)}_{data_hora_atual}.zip'
        destino_zip_bkp = os.path.join(os.path.abspath(pasta_destino_bkp), nome_arquivo_zip_bkp)

        shutil.make_archive(destino_zip_bkp[:-4], 'zip', pasta_a_zipar_bkp)

def zipar_e_mover(nome_da_pasta, pasta_destino):
    # Caminho absoluto da pasta a ser zipada
    pasta_a_zipar = os.path.abspath(nome_da_pasta)

    # Obter a data e hora atual
    agora = datetime.datetime.now()
    data_hora_atual = agora.strftime("%d_%m_%Y_%H00")

    # Nome do arquivo zip com base na data e hora
    nome_arquivo_zip = f'{os.path.basename(nome_da_pasta)}_{data_hora_atual}.zip'

    # Caminho completo para o destino do arquivo zip dentro da pasta "Arquivos Compactados"
    destino_zip = os.path.join(os.path.abspath(pasta_destino), nome_arquivo_zip)

    # Criar o arquivo zip usando shutil
    shutil.make_archive(destino_zip[:-4], 'zip', pasta_a_zipar)

def zip(nome):
    pasta_origem = f'Prints\\{nome}'
    pasta_destino = 'Arquivos Compactados'
    zipar_e_mover(pasta_origem, pasta_destino)

class MeuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automate Checklist")
        self.root.geometry("500x400")  # Defina o tamanho da janela

        # Use um tema estilo ttk para uma aparência mais moderna
        style = ttk.Style()
        style.theme_use("clam")  # Você pode experimentar outros temas disponíveis

        self.label = Label(root, text="Automate Checklist", font=("Arial", 18))
        self.label.pack(pady=10)

        # Checklist Full
        self.button_producao = Button(root, text="Checklist Completo", command=self.realizar_checklist_completo)
        self.button_producao.pack(pady=5)

        self.frame_horizontal = Frame(root)
        self.frame_horizontal.pack()

        # Botões da seção "Checklist Produção"
        self.button_producao = Button(root, text="Checklist Produção", command=self.realizar_checklist_producao)
        self.button_producao.pack(pady=5)

        self.frame_horizontal = Frame(root)
        self.frame_horizontal.pack()

        self.button_bip = Button(self.frame_horizontal, text="BIP", command=self.checklist_bip)
        self.button_bip.pack(side="left", padx=5)

        self.button_ecp = Button(self.frame_horizontal, text="ECP", command=self.checklist_ecp)
        self.button_ecp.pack(side="left", padx=5)

        self.button_pip = Button(self.frame_horizontal, text="PIP", command=self.checklist_pip)
        self.button_pip .pack(side="left", padx=5)

        self.button_pnp = Button(self.frame_horizontal, text="PNP", command=self.checklist_pnp)
        self.button_pnp .pack(side="left", padx=5)

        self.button_smp = Button(self.frame_horizontal, text="SMP", command=self.checklist_smp)
        self.button_smp .pack(side="left", padx=5)

        # Botão "Checklist Desenvolvimento"
        self.button_desenvolvimento = Button(root, text="Checklist Desenvolvimento", command=self.realizar_checklist_desenvolvimento)
        self.button_desenvolvimento.pack(pady=5)

        # Crie um novo quadro para os botões da seção "Checklist Desenvolvimento"
        self.frame_desenvolvimento = Frame(root)
        self.frame_desenvolvimento.pack()

        # Botões da seção "Checklist Desenvolvimento"

        self.button_ecd = Button(self.frame_desenvolvimento, text="ECD", command=self.checklist_ecd)
        self.button_ecd.pack(side="left", padx=5)

        self.button_pid = Button(self.frame_desenvolvimento, text="PID", command=self.checklist_pid)
        self.button_pid.pack(side="left", padx=5)

        self.button_pnd = Button(self.frame_desenvolvimento, text="PND", command=self.checklist_pnd)
        self.button_pnd.pack(side="left", padx=5)

        self.button_smd = Button(self.frame_desenvolvimento, text="SMD", command=self.checklist_smd)
        self.button_smd.pack(side="left", padx=5)

        # Botões da seção "Checklist Qualidade"
        self.button_qualidade = Button(root, text="Checklist Qualidade", command=self.realizar_checklist_qualidade)
        self.button_qualidade.pack(pady=5)
        # Cria um novo bloco para ficar abaixo do botão de Checklist Qualidade.
        self.frame_qualidade = Frame(root)  
        self.frame_qualidade.pack()

        self.button_biq = Button(self.frame_qualidade, text="BIQ", command=self.checklist_biq)
        self.button_biq.pack(side="left", padx=5)

        self.button_ecq = Button(self.frame_qualidade, text="ECQ", command=self.checklist_ecq)
        self.button_ecq.pack(side="left", padx=5)

        self.button_piq = Button(self.frame_qualidade, text="PIQ", command=self.checklist_piq)
        self.button_piq.pack(side="left", padx=5)

        self.button_pnq = Button(self.frame_qualidade, text="PNQ", command=self.checklist_pnq)
        self.button_pnq.pack(side="left", padx=5)

        # Botões da seção "Tablespace"
        self.button_tablespace = Button(root, text="Checklist Tablespace", command=self.realizar_checklist_tablespace)
        self.button_tablespace.pack(pady=5)

        # Botões da seção "Backup e Redolog"
        self.button_backup_sap = Button(root, text="Backup SAP", command=self.realizar_backup_sap)
        self.button_backup_sap.pack(pady=5)

    
        # Outros botões personalizados podem ser adicionados aqui
    def realizar_checklist_producao(self):
        try:
            self.root.iconify() 
            producao("Prints\\PRODUÇÃO\\BIP - 705. BBMAPFRE - BW - PRODUÇÃO", "BIP")
            producao("Prints\\PRODUÇÃO\\ECP - 701.BRMAPFRE - ECC - PRODUÇÃO", "ECP")
            producao("Prints\\PRODUÇÃO\\PIP - 708. BBMAPFRE - PI - PRODUÇÃO", "PIP")
            producao("Prints\\PRODUÇÃO\\PNP - 711. BBMAPFRE - GRC - PRODUÇÃO", "PNP")
            producao("Prints\\PRODUÇÃO\\SMP - 704. BBMAPFRE - SOLMAN PRODUÇÃO", "SMP")
            zip('PRODUÇÃO')
            self.show_message("Checklist Produção finalizado.")
        except Exception as e:
            self.show_message(f"Erro: {str(e)}")

    def realizar_checklist_desenvolvimento(self):
        try:
            self.root.iconify()  
            desenvolvimento("Prints\\DESENVOLVIMENTO\BID", "BID")
            desenvolvimento("Prints\\DESENVOLVIMENTO\ECD", "ECD")
            desenvolvimento("Prints\\DESENVOLVIMENTO\PID", "PID")
            desenvolvimento("Prints\\DESENVOLVIMENTO\PND", "PND")
            desenvolvimento("Prints\\DESENVOLVIMENTO\SMD", "SMD")
            zip('DESENVOLVIMENTO')
            self.show_message("Checklist Desenvolvimento Finalizado.")
        except Exception as e:
            self.show_message(f"Erro: {str(e)}")

    def realizar_checklist_qualidade(self):
        try:
            self.root.iconify()  
            qualidade("Prints\\QUALIDADE\BIQ", "BIQ")
            qualidade("Prints\\QUALIDADE\ECQ", "ECQ")
            qualidade("Prints\\QUALIDADE\PIQ", "PIQ")
            qualidade("Prints\\QUALIDADE\PNQ", "PNQ")
            zip('QUALIDADE')
            self.show_message("Checklist Qualidade Finalizado.")
        except Exception as e:
            self.show_message(f"Erro: {str(e)}")

    def realizar_checklist_tablespace(self):
        try:
            self.root.iconify()
            tablespace()
            zip('TABLESPACE')
            self.show_message(f"Checklist Tablespace Finalizado.")
        except Exception as e:
            self.show_message(f"Erro: {str(e)}")

    
    def realizar_backup_sap(self):
        try:
            self.root.iconify()  # Minimize a janela
            backup_redolog()
            pastas_a_zipar_bkp = ['Prints\\Checklist Backup\\BACKUP', 'Prints\\Checklist Backup\\REDOLOG']
            pasta_destino_bkp = 'Arquivos Compactados'
            zipar_e_mover_backup_redolog(pastas_a_zipar_bkp, pasta_destino_bkp)
            self.show_message("Backup SAP Finalizado.")
        except Exception as e:
            self.show_message(f"Erro: {str(e)}")


            # PRODUÇÃO FUNÇÕES #

    def checklist_bip(self):
        self.root.iconify()  # Minimize a janela
        producao("Prints\\PRODUÇÃO\\BIP - 705. BBMAPFRE - BW - PRODUÇÃO", "BIP")
        producao("Prints\\PRODUÇÃO\\ECP - 701.BRMAPFRE - ECC - PRODUÇÃO", "ECP")
        producao("Prints\\PRODUÇÃO\\PIP - 708. BBMAPFRE - PI - PRODUÇÃO", "PIP")
        producao("Prints\\PRODUÇÃO\\PNP - 711. BBMAPFRE - GRC - PRODUÇÃO", "PNP")
        producao("Prints\\PRODUÇÃO\\SMP - 704. BBMAPFRE - SOLMAN PRODUÇÃO", "SMP")
        zip("PRODUÇÃO")
        self.show_message("Checklist Produção finalizado.")
        
    def checklist_ecp(self):
        self.root.iconify()
        producao("Prints\\PRODUÇÃO\\ECP - 701.BRMAPFRE - ECC - PRODUÇÃO", "ECP")
        producao("Prints\\PRODUÇÃO\\PIP - 708. BBMAPFRE - PI - PRODUÇÃO", "PIP")
        producao("Prints\\PRODUÇÃO\\PNP - 711. BBMAPFRE - GRC - PRODUÇÃO", "PNP")
        producao("Prints\\PRODUÇÃO\\SMP - 704. BBMAPFRE - SOLMAN PRODUÇÃO", "SMP")
        zip("PRODUCAO")
        self.show_message("Checklist Produção finalizado.")

    def checklist_pip(self):
        self.root.iconify()
        producao("Prints\\PRODUÇÃO\\PIP - 708. BBMAPFRE - PI - PRODUÇÃO", "PIP")
        producao("Prints\\PRODUÇÃO\\PNP - 711. BBMAPFRE - GRC - PRODUÇÃO", "PNP")
        producao("Prints\\PRODUÇÃO\\SMP - 704. BBMAPFRE - SOLMAN PRODUÇÃO", "SMP")
        zip("PRODUÇÃO")
        self.show_message("Checklist Produção finalizado.")

    def checklist_pnp(self):
        self.root.iconify()
        producao("Prints\\PRODUÇÃO\\PNP - 711. BBMAPFRE - GRC - PRODUÇÃO", "PNP")
        producao("Prints\\PRODUÇÃO\\SMP - 704. BBMAPFRE - SOLMAN PRODUÇÃO", "SMP")
        zip("PRODUÇÃO")
        self.show_message("Checklist Produção finalizado.")

    def checklist_smp(self):
        self.root.iconify()
        producao("Prints\\PRODUÇÃO\\SMP - 704. BBMAPFRE - SOLMAN PRODUÇÃO", "SMP")
        zip("PRODUÇÃO")
        self.show_message("Checklist Produção finalizado.")

        # DESENVOLVIMENTO FUNÇÕES #

    def checklist_ecd(self):
        self.root.iconify()
        desenvolvimento("Prints\\DESENVOLVIMENTO\ECD", "ECD")
        desenvolvimento("Prints\\DESENVOLVIMENTO\PID", "PID")
        desenvolvimento("Prints\\DESENVOLVIMENTO\PND", "PND")
        desenvolvimento("Prints\\DESENVOLVIMENTO\SMD", "SMD")
        zip("DESENVOLVIMENTO")
        self.show_message("Checklist Desenvolvimento Finalizado.")

    def checklist_pid(self):
        self.root.iconify()
        desenvolvimento("Prints\\DESENVOLVIMENTO\PID", "PID")
        desenvolvimento("Prints\\DESENVOLVIMENTO\PND", "PND")
        desenvolvimento("Prints\\DESENVOLVIMENTO\SMD", "SMD")
        zip("DESENVOLVIMENTO")
        self.show_message("Checklist Desenvolvimento Finalizado.")

    def checklist_pnd(self):
        self.root.iconify()
        desenvolvimento("Prints\\DESENVOLVIMENTO\PND", "PND")
        desenvolvimento("Prints\\DESENVOLVIMENTO\SMD", "SMD")
        zip("DESENVOLVIMENTO")
        self.show_message("Checklist Desenvolvimento Finalizado.")

    def checklist_smd(self):
        self.root.iconify()
        desenvolvimento("Prints\\DESENVOLVIMENTO\SMD", "SMD")
        zip("DESENVOLVIMENTO")
        self.show_message("Checklist Desenvolvimento Finalizado.")

            # FUNÇÕES QUALIDADE #

    def checklist_biq(self):
        self.root.iconify()
        qualidade("Prints\\QUALIDADE\BIQ", "BIQ")
        qualidade("Prints\\QUALIDADE\ECQ", "ECQ")
        qualidade("Prints\\QUALIDADE\PIQ", "PIQ")
        qualidade("Prints\\QUALIDADE\PNQ", "PNQ")
        zip("QUALIDADE")
        self.show_message("Checklist Qualidade Finalizado.")

    def checklist_ecq(self):
        self.root.iconify()
        qualidade("Prints\\QUALIDADE\ECQ", "ECQ")
        qualidade("Prints\\QUALIDADE\PIQ", "PIQ")
        qualidade("Prints\\QUALIDADE\PNQ", "PNQ")
        zip("QUALIDADE")
        self.show_message("Checklist Qualidade Finalizado.")

    def checklist_piq(self):
        self.root.iconify()
        qualidade("Prints\\QUALIDADE\PIQ", "PIQ")
        qualidade("Prints\\QUALIDADE\PNQ", "PNQ")
        zip("QUALIDADE")
        self.show_message("Checklist Qualidade Finalizado.")

    def checklist_pnq(self):
        self.root.iconify()
        qualidade("Prints\\QUALIDADE\PNQ", "PNQ")
        zip("QUALIDADE")
        self.show_message("Checklist Qualidade Finalizado.")

    def show_message(self, message):
        messagebox.showinfo("Mensagem", message)

    def realizar_checklist_completo(self):
        try:
            self.root.iconify()  # Minimize a janela
            producao("Prints\\\PRODUÇÃO\\BIP - 705. BBMAPFRE - BW - PRODUÇÃO", "BIP")
            producao("Prints\\\PRODUÇÃO\\ECP - 701.BRMAPFRE - ECC - PRODUÇÃO", "ECP")
            producao("Prints\\\PRODUÇÃO\\PIP - 708. BBMAPFRE - PI - PRODUÇÃO", "PIP")
            producao("Prints\\\PRODUÇÃO\\PNP - 711. BBMAPFRE - GRC - PRODUÇÃO", "PNP")
            producao("Prints\\\PRODUÇÃO\\SMP - 704. BBMAPFRE - SOLMAN PRODUÇÃO", "SMP")
            zip('PRODUÇÃO')
            sleep(2)
            desenvolvimento("Prints\\DESENVOLVIMENTO\BID", "BID")
            desenvolvimento("Prints\\DESENVOLVIMENTO\ECD", "ECD")
            desenvolvimento("Prints\\DESENVOLVIMENTO\PID", "PID")
            desenvolvimento("Prints\\DESENVOLVIMENTO\PND", "PND")
            desenvolvimento("Prints\\DESENVOLVIMENTO\SMD", "SMD")
            zip('DESENVOLVIMENTO')
            sleep(2)
            qualidade("Prints\\QUALIDADE\BIQ", "BIQ")
            qualidade("Prints\\QUALIDADE\ECQ", "ECQ")
            qualidade("Prints\\QUALIDADE\PIQ", "PIQ")
            qualidade("Prints\\QUALIDADE\PNQ", "PNQ")
            zip('QUALIDADE')
            sleep(2)
            tablespace()
            zip('TABLESPACE')
            self.show_message("Checklist Completo.")
                     
        except Exception as e:
            self.show_message(f"Erro: {str(e)}")

if __name__ == '__main__':
    root = tk.Tk()
    app = MeuApp(root)
    root.mainloop()
''