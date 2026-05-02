from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

sleep(0.5)

english = driver.find_element(By.ID, "langSelect-EN")
english.click()

sleep(0.9)

try:
    accept_cookies = driver.find_element(By.XPATH, "//a[text()='Got it!']")
    accept_cookies.click()
except:
    pass

driver.execute_script("""
Game.bakeryName = "Selenium Bot";
Game.bakeryNameRefresh();
""")

cookie = driver.find_element(By.ID, "bigCookie")

wait_time = 5
timeout = time() + wait_time

sleep(1)

while True:
    cookie.click()
    sleep(0.01)

    if time() > timeout:

        for upgrade in driver.find_elements(By.CSS_SELECTOR, "div[id^='upgrade']"):
            try:
                classes = upgrade.get_attribute("class") or ""
                if "enabled" in classes:
                    upgrade.click()
                    break
            except:
                continue

        for product in reversed(driver.find_elements(By.CSS_SELECTOR, "div[id^='product']")):
            try:
                classes = product.get_attribute("class") or ""
                if "enabled" in classes:
                    product.click()
                    break
            except:
                continue

        timeout = time() + wait_time