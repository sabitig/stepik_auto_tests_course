from selenium import webdriver
import time
import math
import os 

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath("//input")
    input1.send_keys("Пу-пу-пу")
    input2 = browser.find_element_by_xpath("//input[2]")
    input2.send_keys("Пу-пу")
    input3 = browser.find_element_by_xpath("//input[3]")
    input3.send_keys("sasasa@mail.ru")
    download = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    download.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


