from selenium import webdriver

# //*[@id="user-message"]
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_id('user-message')
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()
field1 = driver.find_element_by_id('sum1')
field1.send_keys(10)
field2 = driver.find_element_by_id('sum2')
field2.send_keys(11)
getTotal = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotal.click()
