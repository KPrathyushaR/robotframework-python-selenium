from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
driver= webdriver.Chrome()
# driver.get("https://www.google.com/")
# print(driver.title)
# driver.quit
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
print("Title:", driver.title)
print("Current URL:", driver.current_url)
print(driver.page_source)
time.sleep(3)
driver.get_window_size()
driver.capabilities["browserName"]

wait = WebDriverWait(driver,10)
try:
    username = wait.until(
    EC.visibility_of_element_located(
    (By.ID,"name")
    ))
except:
    print("Element not found")

username.clear()
username.send_keys("abcdefghf")

driver.find_element(By.ID, "email").send_keys("abcdesfgh@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[id='phone']").send_keys("9876543210")
driver.find_element(By.ID, "textarea").send_keys("puttur")

#radio button
male= driver.find_element(By.ID, "male")
print(male.is_enabled())
male.click()

female = driver.find_element(By.ID, "female")
print(female.is_enabled())
female.click()
time.sleep(10)

checkbox= driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
checkbox.click()
print(checkbox.is_selected())


driver.quit()
