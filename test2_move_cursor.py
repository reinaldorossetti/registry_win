from selenium.webdriver import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.w3schools.com/js/tryit.asp?filename=tryjs_imagemap")
driver.implicitly_wait(15)


test = driver.find_element_by_css_selector("#iframeResult")
driver.switch_to.frame("iframeResult")

# driver.find_element_by_css_selector("area[shape=\"circle\"][alt=\"Venus\"]").click()
# driver.execute_script("document.querySelector('area[href =\"venus.htm\"]').click()")

element_mercury = driver.find_element_by_css_selector("area[shape=\"circle\"][alt=\"Venus\"]")

print(element_mercury.rect)
actions = ActionChains(driver)
actions.move_to_element(element_mercury)
actions.click().perform()


