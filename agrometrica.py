import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

## Credenciais do AGROMETRICA
agro_username = ""
agro_password = ""

with open("agrometrica", "r") as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    index = 0

    for row in csv_reader:
        if index == 0:
            agro_username = row[0]
            index = 1
        else:
            agro_password = row[0]

## ETAPA 3 - Acessar AGROMETRICA

# operação headless ( sem abrir navegador )
chrome_options = Options()
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=chrome_options
)

# foco da janela principal
janela_principal = driver.current_window_handle

driver.get(
    "https://sistema.agrometrikaweb.com.br/Sinagro/Usuarios/Login?ReturnUrl=%2fSinagro%2f"
)

print("Acessa agrometrica")
# entra com usuário
username = driver.find_element(By.CSS_SELECTOR, "input[name='login']")
username.send_keys(agro_username)


# entra com senha
password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
password.send_keys(agro_password)

driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
captcha = driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()

print("Clica no ReCaptcha")
time.sleep(5)

driver.switch_to.window(janela_principal)
login = driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
print("Login")

time.sleep(5)

# Close the driver instance
# driver.quit()
