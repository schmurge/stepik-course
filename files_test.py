from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'bla.txt')           # добавляем к этому пути имя файла

link = "http://suninjuly.github.io/file_input.html"

try:
    brw = webdriver.Chrome()
    brw.get(link)

    input1 = brw.find_element_by_name("firstname")
    input1.send_keys("Sirozha")
    input2 = brw.find_element_by_name("lastname")
    input2.send_keys("Siroezhkin")
    input3 = brw.find_element_by_name("email")
    input3.send_keys("bla@bla.bla")

    input4 = brw.find_element_by_id("file")
    input4.send_keys(file_path)

    button = brw.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(15)
    brw.quit()
