"""
Webscraping is used to get the profile image of a github user
"""

import requests
from bs4 import BeautifulSoup as bs

user = input("Enter Github username ")
url = f"https://github.com/{user}"
res = requests.get(url)
soup = bs(res.content, "html.parser")
profile_img = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_img)
