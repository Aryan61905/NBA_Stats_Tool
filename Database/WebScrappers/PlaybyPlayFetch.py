
import requests
from bs4 import BeautifulSoup

def PlayByPlayFetch(token):
    
    url = f"https://www.basketball-reference.com/boxscores/pbp/{token}.html"
    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(str(page_content), 'html.parser')
        tables = soup.find_all("table")   
        
        if tables:
            for table in tables:
                data={}
                rows = table.find_all("tr") 
                for row in rows:
                    row_data = [cell.get_text() for cell in row.find_all(["th", "td"])]
                    if len(row_data) == 1:
                        title = row_data[0]
                        data[title] = []
                    data[title].append(row_data)
      
    for d in data:
        print("")
        #print(d)
        for r in data[d]:
            print(r)
    

    return data
    
print(PlayByPlayFetch("202310240DEN"))