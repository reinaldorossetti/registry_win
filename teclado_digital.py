from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from pymouse import PyMouse

driver = webdriver.Chrome(executable_path="/home/dev/Documents/bin/chromedriverLinux64")
driver.maximize_window()

# need - pip3 install PyUserInput
mouse = PyMouse()

driver.get("https://www.gestaojudicial.com.br/Paginas/Principal/_FSet_Abertura.asp")
driver.implicitly_wait(15)

def move_cursor(coors):
    # fuction move cursor, below the options.
    x, y = list(coors)
    mouse.move(x,y)

def click(coors):
    x, y = list(coors)
    mouse.press(x,y)
    mouse.release(x, y)

def SelectorWait(driver, locator):
    return WebDriverWait(driver, 45).until(presence_of_element_located((By.CSS_SELECTOR, locator)))


# Get iframe location x and y.
captcha = SelectorWait(driver, "#CodSegCriado")

#CodSegCriado
test = SelectorWait(driver, "#CodSegInformado")
test.send_keys(Keys.ENTER)
print(captcha.get_attribute('value'))
test.send_keys(captcha.get_attribute('value'))


test2 = SelectorWait(driver,"#txtcd_Logon")
test2.send_keys("Udemy")
test2.send_keys(Keys.TAB)

dic_linux = {"1":(45, 136),"2":(65, 136),"3":(95, 136)}

driver.execute_script("""
                function Color(){
                var x = document.getElementById('layerTeclado');
                x.style.left = '0px';
                x.style.top = '0px';
                x.style.visibility = 'visible';
                }
                Color();
""")

# move cursor and click
for key, numbers in sorted(dic_linux.items()):
    sleep(3)
    move_cursor(numbers)
    sleep(3)
    click(numbers)
    print(key, numbers)
