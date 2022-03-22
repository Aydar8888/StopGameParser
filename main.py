
from bs4 import BeautifulSoup
import requests


page = 1
while True:
    url = "https://stopgame.ru/games/filter?rating=izumitelno&p=" + str(page)
    src = requests.get(url)
    soup = BeautifulSoup(src.text, "lxml")
    game_list = soup.find_all('div', class_="caption caption-bold")
    # gage_icon = soup.find_all('div', class_="image slanted")
    # for a in gage_icon:
    #     icon_url = a.get("style")
    if (len(game_list)):
        page += 1
        for date in game_list:
            c = date.find('a')
            item_url = "https://stopgame.ru" + c.get("href")
            print(f"{date.text.strip()}: {item_url}") 
        
            
        if page == 4:
            break
    
    
    
    