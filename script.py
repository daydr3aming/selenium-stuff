from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# https://googlechromelabs.github.io/chrome-for-testing/ Chrome Driver Link
# chromedriver.exe tiene que estar en el mismo directorio que el script
# Selenium Integration Project - A01639914


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome()

driver.get("https://google.com")

element = driver.find_element(By.CLASS_NAME, "gLFyf")
element.send_keys("Hello World!")

input("Enter para continuar...")
driver.quit()