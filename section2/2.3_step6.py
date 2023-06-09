from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

def calc(x):
  return str(math.log(abs(12 * math.sin(x))))

def button_click():
   return browser.find_element(By.CSS_SELECTOR, "button.btn").click()

try:

    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)

    button_click()

    time.sleep(1)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)

    input_field = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input_field.send_keys(y)

    button_click()
    
finally:
    time.sleep(7)
    browser.quit()