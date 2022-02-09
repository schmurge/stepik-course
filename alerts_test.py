import time, math
from selenium import webdriver

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    input = browser.find_element_by_id("input_value")
    x = input.text
    y = calc(x)

    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()



