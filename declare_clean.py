from random import random
from selenium import webdriver

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options, executable_path=r'C:\bin\chromedriver.exe') #edit path to webdriver
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
driver.get('https://myaces.nus.edu.sg/htd/htd')
userfield = driver.find_element_by_name('UserName')
passfield = driver.find_element_by_name('Password')
user = 'nusstu\EXXXXX' #edit
pw = 'yourpassword' #edit
userfield.send_keys(user)
passfield.send_keys(pw)
driver.find_element_by_id("submitButton").click()
temp = str(round(36 + random(),1))
driver.find_element_by_xpath('//*[@id="submitDisable"]/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody/tr[3]/td[3]/input[1]').click()
driver.find_element_by_xpath('//*[@id="submitDisable"]/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td[3]/input[1]').click()
driver.find_element_by_id('temperature').send_keys(temp)
driver.find_element_by_name('Save').click()
