import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
FUNCTION = "TIME_SERIES_DAILY"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "YGW7O140ZAJT9SBZ"
NEWS_API_KEY = "1b2ab338ef714986bf63e1531150453b"

stock_params = {
    "function": FUNCTION,
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
stocks_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stocks_response.raise_for_status()
print(stocks_response.text)
data = stocks_response.json()["Time Series (Daily)"]


dates = list(data.keys())

latest_day = dates[1]
previous_day = dates[2]

latest_close = data[latest_day]["4. close"]
previous_close = data[previous_day]["4. close"]

difference = abs(float(latest_close) - float(previous_close))
perc_diff = difference / previous_close * 100

if perc_diff > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    top_three_articles = news_response.json()["articles"][:3]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in top_three_articles]
    for article in formatted_articles:
        print(article)
