from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from dotenv import load_dotenv
import os
import random

load_dotenv()

SIMILAR_ACCOUNT = input("Target Instagram Account: ")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.instagram.com/accounts/login/")

    def login(self):

        sleep(1.5)

        self.email = self.driver.find_element(By.NAME, "email")
        self.email.send_keys(USERNAME)

        self.password = self.driver.find_element(By.NAME, "pass")
        self.password.send_keys(PASSWORD, Keys.ENTER)

        sleep(6)

        self.save_login = self.driver.find_element(By.XPATH, value="//div[@role='button' and contains(text(), 'Not now')]")
        if self.save_login:
            self.save_login.click()

        sleep(2)

        self.notifactions = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
        if self.notifactions:
            self.notifactions.click()

    def find_followers(self):
        sleep(3)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        
        sleep(5)
        followers_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "follower")
        followers_link.click()

        sleep(5)

        modal = self.driver.find_element(By.XPATH, "//div[@role='dialog']")
        
        for _ in range(5):
            self.driver.execute_script("""
                const dialog = arguments[0];
                const scrollable = [...dialog.querySelectorAll('*')].find(
                    el => el.scrollHeight > el.clientHeight
                );
                if (scrollable) scrollable.scrollTop = scrollable.scrollHeight;
            """, modal)
            sleep(2)
            self.follow()

    def follow(self):

        buttons = self.driver.find_elements(
            By.XPATH,
            "//div[@role='dialog']//button[contains(., 'Follow') and not(contains(., 'Following'))]"
        )
        
        for button in buttons:
            try:
                button.click()
                sleep(random.uniform(0.5, 2.5))
            except:
                pass

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()