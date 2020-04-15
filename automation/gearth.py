from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://google.com/earth'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)
launchButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]')))
# button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[4]/a[3]/span/span')
launchButton.click()
# button.click()
