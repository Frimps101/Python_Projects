#! python
# open_all_links.py - A simple python program that opens all links on a page in seperate browser tabs


import webbrowser

links = []

while(True):
    user_link = input("Enter the URL you want to open: ")
    if user_link == "":
        break
    else:
        links.append("https://" + user_link)
    
    
    
for link in links:
    print(link)
    webbrowser.open_new_tab(link)