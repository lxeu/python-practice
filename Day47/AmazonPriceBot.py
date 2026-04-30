from bs4 import BeautifulSoup
import requests

header = {"Accept-Language": "en-US,en;q=0.5",
          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
          }

url = "https://www.amazon.com/dp/B0D35XRV6F/ref=sspa_dk_detail_0?pd_rd_i=B0D35XRV6F&pd_rd_w=ixC37&content-id=amzn1.sym.953c7d66-4120-4d22-a777-f19dbfa69309&pf_rd_p=953c7d66-4120-4d22-a777-f19dbfa69309&pf_rd_r=XAF6S8BX0SFWQ3E8S4WD&pd_rd_wg=IjGir&pd_rd_r=8a4d5dfa-1983-48f1-a57d-f28abfa32f02&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy&th=1"
response = requests.get(url, headers=header).text

soup = BeautifulSoup(response, "html.parser")

price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_dec = soup.find(name="span", class_="a-price-fraction").getText()
price = float(price_whole + price_dec)

BUY_PRICE = 35
if price < BUY_PRICE:
    print(f"Price of item is lower than buy price! Currently ${price}.")