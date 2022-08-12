#! python3
# open_social_sites.py = A simple python program that opens sites i regularly visit

import webbrowser, sys

sites = [
    "fb.com",
    "instagram.com",
    "gmail.com"
]

for site in sites:
    webbrowser.open_new_tab(site)