from selenium import webdriver
import time
import os
import pyperclip as ppc
import math


try:   
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    button = browser.find_element_by_css_selector(".btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)
    
    field = browser.find_element_by_css_selector('#answer')
    field.send_keys(y)

    button = browser.find_element_by_css_selector(".btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    ppc.copy(addToClipBoard)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()