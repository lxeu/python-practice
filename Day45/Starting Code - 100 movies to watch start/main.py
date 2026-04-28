import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL).text
soup = BeautifulSoup(response, "html.parser")

h3_tags = soup.find_all(name="h3")
movie_list = [h3.getText() for h3 in h3_tags]

with open("top100movies.txt", "w") as f:
    for i in range(len(movie_list) - 1, 0, -1):
        f.write(f"{movie_list[i]}\n")