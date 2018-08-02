from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException


class Wait:

    def __init__(self, driver):
        self.driver = driver
        self.loading = "div[id=wait][style*=block]"
        self.button = "button"

    def find_wait_not_exists(self, locator, timeout=35):
        elem = None
        elem_not = None
        try:
            elem = WebDriverWait(driver, 5, 1, (ElementNotVisibleException)).\
                until(lambda x: x.find_element_by_css_selector(locator).is_displayed())
            if elem:
                elem_not = WebDriverWait(driver, timeout, 1, (ElementNotVisibleException)). \
                    until_not(lambda x: x.find_element_by_css_selector(locator).is_displayed())

        except TimeoutException:
            print("Teste excedeu o tempo esperado!")

        return elem, elem_not

    def wait_loading(self):
        print(self.find_wait_not_exists(self.loading))

    def clique(self):
        self.driver.find_element_by_css_selector(self.button).click()

driver = webdriver.Firefox()
driver.get("https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_ajax_ajaxcomplete")
driver.set_page_load_timeout(30)
driver.implicitly_wait(15)
driver.switch_to.frame("iframeResult")
test = Wait(driver)
test.clique()
test.wait_loading()
driver.quit()
