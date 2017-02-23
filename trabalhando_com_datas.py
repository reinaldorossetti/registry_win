from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from operator import sub
import pdb

driver = webdriver.Firefox(executable_path="/media/dev/Vms/bin/geckodriverLinux64")
driver.get('http://eonasdan.github.io/bootstrap-datetimepicker/')

sleep_time = 60
def wait_element(driver, selector):
    return WebDriverWait(driver, sleep_time).until(expected_conditions.visibility_of_element_located
                                                   ((By.CSS_SELECTOR, selector)))


date_end = datetime.now()
date_delta = timedelta(+2)
date_ini = date_end-date_delta
date_ini_format = date_ini.strftime('%m/%d/%Y')
date_end_format = date_end.strftime('%m/%d/%Y')
ini = date_ini.strftime('%d/%m/%Y')
end = date_end.strftime('%d/%m/%Y')
print(date_ini.strftime('%d/%m/%Y'))
print(date_end.strftime('%d/%m/%Y'))

driver.execute_script("""
            $('.date-range .start-date').data('DateTimePicker').show();
""")

button_calendar =  wait_element(driver, "#datetimepicker6 > span")
button_calendar.click()

print(".day[data-day='{}']".format(date_ini_format))
day_date_ini = wait_element(driver, ".day[data-day='{}']".format(date_ini_format))
day_date_ini.click()
driver.execute_script("""
            $('.date-range .start-date').data('DateTimePicker').hide();
""")


driver.execute_script("""
            $('.date-range .end-date').data('DateTimePicker').show();
""")

day_date_end = wait_element(driver, ".day[data-day='{}']".format(date_end_format))
day_date_end.click()

driver.execute_script("""
            $('.date-range .end-date').data('DateTimePicker').hide();
""")
wait_element(driver, "button[class*='btn'][type*='submit'] ").click()

verified01 =  wait_element(driver, "input[class*='start-date'][type*='text']")
verified02 =  wait_element(driver, "input[class*='end-date'][type*='text'] ")

sleep(2)
string_datetime01 = str(verified01.get_attribute('value'))
string_datetime02 = str(verified02.get_attribute('value'))

print(string_datetime01, string_datetime02)
print(date_ini_format, date_end_format)
# verifica se o calendario bate com o inserido no campo.
assert str(date_ini_format) in str(string_datetime01)
assert str(date_end_format) in str(string_datetime02)

string_datetime01 = string_datetime01.replace(" AM", "")
string_datetime02 = string_datetime02.replace(" PM", "")

data01 = datetime.strptime(string_datetime01, '%m/%d/%Y %H:%M')
data02 = datetime.strptime(string_datetime02, '%m/%d/%Y %H:%M')

print(verified01.get_attribute('value'), verified02.get_attribute('value'))
result = sub(data02, data01)

hours = (result.total_seconds()//3600)-result.days*24
minute = (result.total_seconds()-result.days*86400-hours*3600)//60

text_page = "EM {} DIAS, {} HORAS, {} MINUTOS".format(result.days,
            '{0:g}'.format(hours), '{0:g}'.format(minute))
            
print(text_page)
