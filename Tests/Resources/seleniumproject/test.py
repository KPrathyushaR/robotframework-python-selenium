from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
# driver.get("https://www.google.com/")
# print(driver.title)
# driver.quit
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys("abc@gmail.com")
driver.find_element(By.NAME, "password").send_keys("abcdesfgh")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.quit()
