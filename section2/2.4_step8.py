from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
  browser.get(link)

  WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
  browser.find_element(By.CSS_SELECTOR, "button.btn").click()

  x = int(browser.find_element(By.ID, 'input_value').text)
  y = calc(x)

  input_field = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
  input_field.send_keys(y)

  browser.find_element(By.ID, 'solve').click()

finally:
  time.sleep(3)
  browser.close()