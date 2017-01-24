from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
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

# Get iframe location x and y.
sleep(3)
captcha = driver.find_element_by_css_selector("#CodSegCriado")
#CodSegCriado
sleep(3)
test = driver.find_element_by_css_selector("#CodSegInformado")
test.send_keys(Keys.ENTER)
sleep(3)
print(captcha.get_attribute('value'))
test.send_keys(captcha.get_attribute('value'))


test2 = driver.find_element_by_id("txtcd_Logon")
test2.send_keys("Udemy")
test2.send_keys(Keys.TAB)
sleep(3)

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
