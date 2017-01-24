from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import win32api
import win32con


driver = webdriver.Ie()
driver.maximize_window()

driver.get("https://www.gestaojudicial.com.br/Paginas/Principal/_FSet_Abertura.asp")
driver.implicitly_wait(15)

def move_cursor(x, y):
    # fuction move cursor, below the options.
    # MOUSEEVENTF_LEFTDOWN
    # MOUSEEVENTF_LEFTUP
    # MOUSEEVENTF_RIGHTDOWN
    # MOUSEEVENTF_RIGHTUP
    # MOUSEEVENTF_MIDDLEDOWN
    # MOUSEEVENTF_MIDDLEUP
    # MOUSEEVENTF_ABSOLUTE

    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    sleep(3)

def click():
    x, y = win32api.GetCursorPos()
    win32api.SetCursorPos((x, y))
    # Left click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    # Right click
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

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

teclado = driver.find_element_by_css_selector("img[name*=\"teclado\"]")
teclado_x = int(teclado.location['x'])
teclado_y = int(teclado.location['y'])
print(teclado_x, teclado_y)

driver.execute_script("""
                function Color(){
                var x = document.getElementById('layerTeclado');
                x.style.left = '0px';
                x.style.top = '0px';
                }
                Color();
""")

# 1
move_cursor(30, 85)
sleep(5)
click()
# 2
move_cursor(50, 85)
sleep(5)
click()
# 3
move_cursor(70, 85)
sleep(5)
click()
