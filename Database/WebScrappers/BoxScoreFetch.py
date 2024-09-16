
import requests
from bs4 import BeautifulSoup

def BoxScoreFetch(token):
    
    url = f"https://www.basketball-reference.com/boxscores/{token}.html"
    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(str(page_content), 'html.parser')
        tables = soup.find_all("table")   
        data={}
        flag = ""
        away = ''
        if tables:
            for table in tables:
                title = table.attrs['id']
                data[title] = []
                rows = table.find_all("tr")[1:]
                home = token[-3:]
                
                for row in rows:
                    row_data = [cell.get_text() for cell in row.find_all(["th", "td"])]
                    if row_data[0] == 'Starters':
                        flag = 'S'
                    elif row_data[0] == 'Reserves':
                        flag = 'R'
                    row_data.append(flag)
                    team = title.split("-")[1]
                    if team != home:
                        opp = home
                        away = team
                    else:
                        opp = away

                    gameType = title.split("-")[2]
                    row_data.append(team)
                    row_data.append(opp)
                    row_data.append(gameType)
                    
                    data[title].append(row_data)

    
    return data
        