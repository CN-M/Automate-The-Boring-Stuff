from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://kimcartoon.li')
searchElem = driver.find_element_by_css_selector('.text')
searchElem.send_keys('Craig of the creek')

butt = driver.find_element_by_css_selector('.button')
butt.click()

slct = driver.find_element_by_css_selector('#leftside > div.bigBarContainer > div > div > div.list-cartoon > div:nth-child(3) > a.hot-label')
slct.click()