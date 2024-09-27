import requests
from bs4 import BeautifulSoup
import time

def PlayerStatsFetch():
    
    url = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"
    response = requests.get(url)
    time.sleep(7)
    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(str(page_content), 'html.parser')
        tables = soup.find_all("table")   
        data=[]
        if tables:
            for table in tables:
                
                rows = table.find_all("tr") 
                for row in rows:
                    row_data = [cell.get_text() for cell in row.find_all(["th", "td"])]
                    row_data[1] = row_data[1].replace('Ä\x87','c')
                    row_data[1] = row_data[1].replace('Å\x86Ä£','ng')
                    data.append(row_data)
    else:
        return response.status_code  
    return data



