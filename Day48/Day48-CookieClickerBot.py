from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

sleep(0.5)

english = driver.find_element(By.ID, "langSelect-EN")
english.click()

sleep(0.9)

accept_cookies = driver.find_element(By.XPATH, "//a[text()='Got it!']")
accept_cookies.click()

driver.execute_script("""
Game.bakeryName = "Selenium Bot's";
Game.bakeryNameRefresh();
""")

cookie = driver.find_element(By.ID, "bigCookie")

wait_time = 5
timeout = time() + wait_time

sleep(1)

while True:
    cookie.click()

    if time() > timeout:
        try:
            upgrades = driver.find_elements(By.CSS_SELECTOR, "div[id^='upgrade']")
            for upgrade in upgrades:
                if "enabled" in upgrade.get_attribute("class"):
                    upgrade.click()
                    break

            products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product']")
            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()

        except (NoSuchElementException, ValueError):
            print("Couldn't find item")


        timeout = time() + wait_time