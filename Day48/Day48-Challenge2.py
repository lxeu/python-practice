from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')

search = driver.find_element(By.CLASS_NAME, "cdx-text-input__input")
search.send_keys("Python", Keys.ENTER)

