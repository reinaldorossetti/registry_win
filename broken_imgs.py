from selenium import webdriver
from selenium.webdriver.common.by import By
from requests import get

# Instanciando o chrome driver.
driver = webdriver.Chrome()
# Abre a url.
driver.get("http://the-internet.herokuapp.com/broken_images")
# Espera de forma implicita os elementos carregar na pagina.
driver.implicitly_wait(10)
# Procura os elementos no browser via CSS Selector.
elementos = driver.find_elements(By.CSS_SELECTOR, "img")

for x in elementos:
    # pega o link
    url = x.get_property('src')
    # carrego o link na biblioteca requests.
    result = get(url)
    # verifico o status code da url.
    # se for status 404 que dizer que a url nao foi encontrada, entao a url quebrou.
    if result.status_code == 404:
        print("Url quebrou: {}".format(url))

# fecha o browser
driver.close()
