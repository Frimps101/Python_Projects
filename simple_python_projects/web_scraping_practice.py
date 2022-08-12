import requests
from bs4 import BeautifulSoup as bs

get_user = input("Enter your github username: ")
url = f"https://github.com/{get_user}"

res = requests.get(url)
# soup = bs(res.content, "html.parser")

# profile_img = soup.find("img", {"alt": "Avatar"})["src"]
# print(profile_img)

soup = bs(res.content, "html.parser")

profile_img = soup.find("img", {"alt": "Avatar"})["src"]
print(profile_img)
