from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

def main():
    url = 'https://github.com/zigjag?tab=repositories'
    html = requests.get(url)
    bs = BeautifulSoup(html.text, 'lxml')

    dataList = []
    dataColumn = [i.text.strip() for i in bs.findAll('h3', class_='wb-break-all')]

    df = pd.DataFrame({'repos': dataColumn})
    df.to_json('repos.json')
    print(df)

main()
