from selenium import webdriver
import math, time

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
