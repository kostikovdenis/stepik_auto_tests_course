from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try: 
    first_name_field = browser.find_element(By.NAME, "firstname")
    first_name_field.send_keys('Ivan')
    last_name_field = browser.find_element(By.NAME, "lastname")
    last_name_field.send_keys('Petrov')
    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys('ivan_petrov@yaschik.ru')
    file_field = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    file_field.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()