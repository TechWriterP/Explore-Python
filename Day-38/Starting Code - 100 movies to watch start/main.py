import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")

# title_list = []
titles = soup.find_all("h3", class_="title")

# for title in titles:
#     title_list.append(title.getText())
# title_list.reverse()
# print(title_list)

with open("movies.txt", 'w', encoding="utf-8") as file:
    for title in titles:
        title_name = title.getText()
        file.write(f"{title_name}\n")


