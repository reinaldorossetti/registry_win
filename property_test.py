from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import datetime
from logging_class import Logger

logger = Logger().get()
logger.info('Test propert')
start = datetime.now().replace(microsecond=0)
# Instanciando o firefox driver.
# Passamos o caminho do driver, no meu caso eh linux a barra / eh no windows eh o contrario.
driver = webdriver.Chrome()
# Abre a url.
driver.get("http://www.w3schools.com/tags/tryit.asp?filename=tryhtml_frame_cols")
# Espera de forma implicita os elementos carregar na pagina.
driver.implicitly_wait(10)
# Muda para o frame Pai.
driver.switch_to.frame('iframeResult')
# Muda para o frame Filho.
driver.switch_to.frame(0)
# imprime o codigo do frame atual.
print(str(driver.page_source))

def espera_explicita(driver, selector, delay=30):
    # Espera Explicita > Melhor forma de fazer.
    # An expectation for checking that an element is present on the DOM of a page and visible.
    return WebDriverWait(driver, delay).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector)))

espera_explicita(driver, "h3")

# Procura o elemento na tela via CSS Selector.
elemento = driver.find_element(By.CSS_SELECTOR, "h3")

print(elemento)

# Armazenar o elemento texto da tag a
variavel_texto = elemento.text

# Armazenar o atributo href da tag a
variavel_url = elemento.get_property('baseURI')

# imprimindo no console os valores texto e url.
print(variavel_texto)

# Fazendo os assert, se os valores sao diferentes do esperado o assert vai falhar ou
# seja nosso teste falhou.

assert "Frame A" == variavel_texto
assert "http://www.w3schools.com/tags/frame_a.htm" == variavel_url
logger.info('\n01 - Passed - Propert_test.py')
# fecha o browser
driver.close()
print(datetime.now().replace(microsecond=0) - start)

