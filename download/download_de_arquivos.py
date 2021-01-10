from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from os import path, remove, walk, getenv
from time import sleep, time

from pathlib import Path
Path("c:\\temp").mkdir(parents=True, exist_ok=True)
path_file = "c:\\temp"

# Deixei explicito a classe Options, eh comum usar o ChromeOptions, mas
# nao eh o nome da classe e sim uma abreviacao pra ela.
options = Options()
link = ""
result = False
# Habilitando as configuracoes:
# Primeiro o diretorio que vai baixar o arquivo.
# Segundo remover a mensagem de permitir download.
prefs = {"safebrowsing.enabled": True}
prefs2 = {"download.default_directory": path_file}
# atualiza o dicionario com a segunda preferencia.
prefs.update(prefs2)

# add_experimental_option eh a funcao que vamos adicionar as preferencias.
options.add_experimental_option("prefs", prefs)
# Verifica se preferencias foram setadas.
print(options.experimental_options)

# Descobre o local que o arquivo esta em dentro da pasta que passou.
def find_files(filename, search_path):
   result = []
   for root, dir, files in walk(search_path):
      if filename in files:
         result.append(path.join(root, filename))
   return result

# Criar a variavel de ambiente que vai conter o caminho do python.
PYTHON_PATH = getenv('PY')
chromedriver = find_files("chromedriver.exe", PYTHON_PATH)[0]
print(chromedriver)

driver = WebDriver(executable_path=chromedriver, chrome_options=options)
driver.get("http://www.python.org/downloads/")


def wait_element(driver_, elem):
    return WebDriverWait(driver_, 15).until(element_to_be_clickable((By.CSS_SELECTOR, elem)))


elem_download = 'div.download-for-current-os div.download-os-windows > p.download-buttons > a.button:nth-child(1)'

download_button = wait_element(driver, elem_download)
if download_button:
    link = (driver.find_element_by_css_selector(elem_download).get_attribute("href"))
    driver.find_element_by_css_selector(elem_download).click()

# Pegamos o nome do arquivo.
file = (link.split("/"))[-1]
print(file)

timeout = 60
startTime = time()

# Validamos se o arquivo existe no path.
# Criamos um timeout dinamico de no maximo 60s.

while True:
    if path.exists(path.join(path_file, file)):
        result = True
        break
    if time() - startTime > timeout:
        break
    sleep(0.5)

assert result

# removemos o arquivo ao final do teste.
remove(path.join(path_file, file))