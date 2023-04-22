import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def sendKeys( target, keys ):
    try:
        elem = driver.find_element(target[0],target[1])
    except Exception:
        print('Erro ao carregar',target)
        exit(1)
    elem.send_keys(keys)
    print("sendKeys",target,keys)


def clique( target ):
    try:
        elem = driver.find_element(target[0],target[1])
    except Exception:
        print('Erro ao carregar',target)
        exit(1)
    elem.click()
    print("click",target)


dir_path = os.getcwd()
download_path = '/pdfs'
newpath = dir_path + download_path
if not os.path.exists(newpath):
    os.makedirs(newpath)

# operação headless ( sem abrir navegador )
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": r""+newpath
  })
# Create a Chrome driver instance
# driver = webdriver.Chrome(chrome_options)
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=chrome_options
)

# foco da janela principal
janela_principal = driver.current_window_handle

tempoEspera = 5

driver.switch_to.window(janela_principal)

#driver.get("https://google.com")

driver.set_page_load_timeout(tempoEspera)
driver.implicitly_wait(tempoEspera)

driver.get('https://itupeva.sp.gov.br/site/images/livros-drive-thru.pdf')

def processar( ):
    try:
        iframes = (driver.find_element(By.TAG_NAME, "embed"))
        print('embed')
        driver.switch_to.frame(iframes)

        iframes = (driver.find_element(By.TAG_NAME, "body"))
        print('body')
        driver.switch_to.frame(iframes)

        print('viewer')
        iframes = (driver.find_element(By.ID, "viewer"))
        driver.switch_to.frame(iframes)

        iframes = (driver.find_element(By.ID, "download"))
        print('download')
        driver.switch_to.frame(iframes)
    except Exception:
        print('deu ruim')

processar()