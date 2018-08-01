from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

def find(driver):
    return driver.find_element_by_css_selector('div[id="loading-component"][class*=show]')

def wait_load(driver, timeout=30):
    # wait to appear
    wait = WebDriverWait(driver, 5)
    wait.until(find(driver))
    # wait to be gone
    wait = WebDriverWait(driver, timeout)
    wait.until_not(find(driver))
    
driver = webdriver.Chrome()
wait_load(driver)
