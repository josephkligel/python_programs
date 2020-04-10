from bs4 import *
import requests
import pandas as pd
import sqlite3

def write_to_file(dataframe):
    def ask_question():
        choice = input("Are you sure you want to write to file(s)?\ny/n: ")
        if(choice.lower() == 'y'):
            dct = {
                1: 'Excel',
                2: 'CSV',
                3: 'JSON',
                4: 'HTML',
                5: 'SQL',
                6: 'All Formats'
            }
            for k, v in dct.items():
                print(k, v, sep=') ')
            num = int(input('Choose a number (1, 2, 3, 4, 5, 6): '))
            return num
        else:
            print('Goodbye. Maybe next time.')
            exit()

    num = ask_question()
    if num == 1:
        dataframe.to_excel('output.xlsx')
        print('Data written to excel file')
        exit()
    elif num == 2:
        dataframe.to_csv('output.csv')
        print('Data written to csv file')
        exit()
    elif num == 3:
        dataframe.to_json('output.json')
        print('Data written to json file')
        exit()
    elif num == 4:
        dataframe.to_html('output.html')
        print('Data written to html file')
        exit()
    elif num == 5:
        conn = sqlite3.Connection('output.db')
        dataframe.to_sql('quotes', con=conn)
        print('Data written to sql file')
        exit()
    elif num == 6:
        dataframe.to_excel('output.xlsx')
        dataframe.to_csv('output.csv')
        dataframe.to_json('output.json')
        dataframe.to_html('output.html')
        dataframe.to_sql('output.sql')
        print('Data written all formats: excel, csv, json, html, and sql.')
        exit()
    else:
        print('Nothing has been written.')
        exit()

#Webscraping
data = requests.get("https://finance.yahoo.com/quote/MSFT/history?p=MSFT")
soup = BeautifulSoup(data.text, 'html.parser')
row_data = []
td_string = ''
quotes_table = soup.find('table', {'class': 'W(100%) M(0)'})
tbody = quotes_table.find('tbody')
for tr in tbody.find_all('tr'):
    cells = [td.text for td in tr]
    row_data.append(cells)
df = pd.DataFrame(row_data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
write_to_file(df)
# print(df)
