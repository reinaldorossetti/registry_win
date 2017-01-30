from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep



# Instanciando o firefox driver.
# Passamos o caminho do driver, no meu caso eh linux a barra / eh no windows eh o contrario.
driver = webdriver.Firefox(executable_path="/media/dev/DATA/Downloads/geckodriver")
# Abre a url.
driver.get("http://eonasdan.github.io/bootstrap-datetimepicker/")
# Espera de forma implicita os elementos carregar na pagina.
driver.implicitly_wait(15)

button_calendar = driver.find_element(By.CSS_SELECTOR, "#datetimepicker6 > span")
button_calendar.click()

# $("#datetimepicker1 > span").click();
# <td data-action="selectDay" data-day="01/31/2017" class="day">31</td>
"""
Pior caso, o day estah no proximo noh usamos o next, e procuramos o tag filho
com o find, e damos o click no final.
$(".start-date").next().children().find(".day[data-day='13/01/2017']").click()
$(".end-date").next().children().find(".day[data-day='13/01/2017']").click()
"""
# como eh um componente javascript essa eh a melhor forma.
try:
    test = driver.execute_script("""
        $("#datetimepicker6 .day[data-day='01/10/2017']").click();
    """)
except WebDriverException:
    print("exception in driver")

button_calendar = driver.find_element(By.CSS_SELECTOR, "#datetimepicker7 > span")
button_calendar.click()

try:
    test = driver.execute_script("""
        $("#datetimepicker7 .day[data-day='01/11/2017']").click();
    """)
except WebDriverException:
    print("exception in driver")
