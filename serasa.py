import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ETAPA 0 - pegar senhas e salvar em variaveis

## Credenciais do SERASA
serasa_username = ""
serasa_password = ""

with open("credenciais", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    index = 0
    for row in csv_reader:
        index = index + 1
        if index == 1:
            serasa_username = row[0]
        if index == 2:
            serasa_password = row[0]


# operação headless ( sem abrir navegador )
chrome_options = Options()
chrome_options.add_argument("--headless=new")

# Create a Chrome driver instance
# driver = webdriver.Chrome(chrome_options)
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=chrome_options
)

# foco da janela principal
janela_principal = driver.current_window_handle

tempoEspera = 0.5

lastCPF = None  # Deixa None senão tiver ultimo cpf

## ETAPA 1 - pegar csv
# Open the CSV file
with open("exemplo.csv", "r") as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    index = 0

    # Loop through each row in the CSV file
    for row in csv_reader:
        cpf = row[0]

        if index == 0:
            index = 1
            continue
        if not lastCPF == None and not lastCPF == cpf:
            continue

        # Do something with the row
        print("Consulta com CPF: " + cpf)

        ## ETAPA 2 - Acessar SERASA

        driver.switch_to.window(janela_principal)

        if not "login" in vars():
            # Navigate to the website where the field is located
            driver.get("https://sitenet05.serasa.com.br/GestorPJ/Default.aspx")

            username = driver.find_element(By.CSS_SELECTOR, "#txtLogonSerasa")
            # entra com usuário
            username.send_keys(serasa_username)

            # entra com senha
            password = driver.find_element(By.CSS_SELECTOR, "#txtSenhaSerasa")
            password.send_keys(serasa_password)

            login = driver.find_element(By.CSS_SELECTOR, "#imBtEntrar").click()
            print("Login")
        else:
            driver.get(
                "https://sitenet05.serasa.com.br/GestorPJ/decisao/AprovaPolitica.aspx?varTP=F&HomolPol=N&VarBase=P"
            )

        time.sleep(tempoEspera)
        decisao = driver.find_element(By.ID, "ctl00_ctl00_itemModuloDecisao").click()

        if not "overlay" in vars():
            print("Decisao")
            time.sleep(tempoEspera)
            overlay = driver.find_element(By.ID, "driver-page-overlay")
            overlay.click()

        time.sleep(tempoEspera)
        pessoal = driver.find_element(
            By.ID, "ctl00_ctl00_MainContent_cphBody_cardAnalisePF"
        ).click()
        print("Analise de pessoa")

        time.sleep(tempoEspera)
        botaCPF = driver.find_element(By.ID, "txtCPF").send_keys(cpf)
        avaliar = driver.find_element(By.CSS_SELECTOR, "#ImBtAvaliar").click()
        print("Avaliar")

        time.sleep(tempoEspera)
        relatorio = driver.find_element(
            By.ID, "ctl00_ctl00_MainContent_cphBody_btRelatorio"
        ).click()

        time.sleep(tempoEspera)
        print("Abriu relatorio")

        # pega a janela do popup
        popup_serasa = driver.window_handles[-1]
        driver.switch_to.window(popup_serasa)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

        time.sleep(tempoEspera)

        downloadRelatorio = driver.find_element(By.ID, "btoDownload").click()
        print("Download")

        time.sleep(tempoEspera)
        driver.close()
driver.quit()
