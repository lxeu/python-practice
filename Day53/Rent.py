from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from time import sleep


# ----- bs4 -----

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=headers).text
soup = BeautifulSoup(response, "html.parser")

# prices
price_tags = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices = [
    "".join(c for c in price.text if c.isdigit() or c == "$" or c == ",")
    for price in price_tags
]

# links
url_tags = soup.find_all(name="a", class_="property-card-link")
urls = [url.get("href") for url in url_tags]

# address
address_tags = soup.find_all(name="address")
addresses = [address.text.replace(" | ", " ").strip() for address in address_tags]


# ----- selenium -----

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeUvZQ9sY0PCJZGspxdABvFuVc97iGr0IFy95fDwU-IbydFHg/viewform?usp=dialog")

# upload info to form
for i in range(len(urls)):

    sleep(0.5)
    inputs = driver.find_elements(By.CLASS_NAME, "whsOnd")
    inputs[0].send_keys(addresses[i])
    inputs[1].send_keys(prices[i])
    inputs[2].send_keys(urls[i])
    submit_btn = driver.find_element(By.CLASS_NAME, "NPEfkd")
    submit_btn.click()
    
    sleep(0.5)

    submit_again = driver.find_element(By.LINK_TEXT, "Submit another response")
    submit_again.click()