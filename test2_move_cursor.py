from selenium.webdriver import ActionChains
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/dev/bin/chromedriverLinux64")
driver.maximize_window()

driver.get("http://www.w3schools.com/js/tryit.asp?filename=tryjs_imagemap")
driver.implicitly_wait(15)


test = driver.find_element_by_css_selector("#iframeResult")
driver.switch_to.frame("iframeResult")

Mercury = driver.find_element_by_css_selector("area[alt=\"Venus\"]")

actions = ActionChains(driver)
actions.move_to_element(Mercury)
actions.click().perform()


