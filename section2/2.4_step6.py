from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element(By.ID, "button")
# button.click()
browser.close()

