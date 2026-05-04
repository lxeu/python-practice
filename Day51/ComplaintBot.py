from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 10

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0
        self.wait = WebDriverWait(self.driver, 15)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        self.go_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/a')))
        self.go_btn.click()

        sleep(50)

        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text

    def complain_to_provider(self):
        print(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.complain_to_provider()