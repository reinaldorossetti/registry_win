from selenium import webdriver

browser = webdriver.Chrome()  # Get local session of firefox
browser.get("https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_hide_p")

with open('jquery.min.js', 'r') as jquery_js:  # read the jquery from a file
    jquery = jquery_js.read()
    browser.execute_script(jquery)  # active the jquery lib

elem = browser.find_element_by_id("menuButton")
# now you can write some jquery code then execute_script them
js = "$(arguments[0]).trigger(\"click\");"

success = browser.execute_script(js, elem)
if (success == False): print("falhou")