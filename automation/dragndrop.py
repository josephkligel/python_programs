from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
sourceBox = driver.find_element_by_xpath('//*[@id="box1"]')
destBox = driver.find_element_by_xpath('//*[@id="box101"]')
actions = ActionChains(driver)
actions.drag_and_drop(sourceBox, destBox).perform()
