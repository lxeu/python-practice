from selenium import webdriver
from selenium.webdriver.common.by import By



chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

upcoming_events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

events = {}
for i in range(len(time)):
    events[i] = {
        "time": time[i].text,
        "event": upcoming_events[i].text,
                 }

print(events)

driver.quit()