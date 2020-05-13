from tkinter import *
from tkinter import messagebox, Menu
import requests
import json
import sqlite3
import time

pycrypto = Tk()
pycrypto.title("My Crypto portfolio")

con = sqlite3.connect('coin.db')
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY, symbol TEXT, amount INTEGER, price REAL)")
con.commit()

# cursor.execute("INSERT INTO coin VALUES(1, 'BTC', 2, '3250')")
# con.commit()
# cursor.execute("INSERT INTO coin VALUES(2, 'ETH', 5, 120)")
# con.commit()
# cursor.execute("INSERT INTO coin VALUES(3, 'NEO', 5, 10)")
# con.commit()
# cursor.execute("INSERT INTO coin VALUES(4, 'XRP', 3, 30)")
# con.commit()
def reset():
    for frame in pycrypto.winfo_children():
        frame.destroy()
    app_navigation()
    app_header()
    my_portfolio()

def app_navigation():
    def clear_all():
        cursor.execute("DELETE FROM coin")
        con.commit()
        messagebox.showinfo("Portfolio Notification", "Portfolio Cleared - Add New Coins")
        reset()

    def close_app():
        pycrypto.destroy()

    menu = Menu(pycrypto)
    file_item = Menu(menu)
    file_item.add_command(label='Clear Portfolio', command=clear_all)
    file_item.add_command(label='Close App', command=close_app)
    menu.add_cascade(label='File', menu=file_item)
    pycrypto.config(menu=menu)

def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=50&convert=USD&CMC_PRO_API_KEY=a4f4cb0a-d308-4307-8ad1-6796f1f869b5")
    api = json.loads(api_request.content)

    cursor.execute("SELECT * FROM coin")
    coins = cursor.fetchall()

    def font_color(amount):
        if amount >= 0:
            return 'green'
        else:
            return 'red'

    def insert_coin():
        cursor.execute("INSERT INTO coin(symbol, price, amount) VALUES(?, ?, ?)", (symbol_txt.get(), price_txt.get(), amount_txt.get()))
        con.commit()
        messagebox.showinfo("Portfolio Notification", "Coin Added to Portfolio Successfully")
        reset()

    def update_coin():
        cursor.execute("UPDATE coin SET symbol=?, price=?, amount=? WHERE id=?", (symbol_update.get(), price_update.get(), amount_update.get(), portid_update.get()))
        con.commit()
        messagebox.showinfo("Portfolio Notification", "Coin Updated to Portfolio Successfully")
        reset()

    def delete_coin():
        cursor.execute("DELETE FROM coin WHERE id=?", (portid_delete.get(),))
        con.commit()
        messagebox.showinfo("Portfolio Notification", "Coin Deletion from Portfolio Successfull")
        reset()

    total_pl = 0
    coin_row = 1
    total_current_value = 0
    total_amount_paid = 0

    for i in range(0, 50):
        for coin in coins:
            if api['data'][i]['symbol'] == coin[1]:
                total_paid = coin[2] * coin[3]
                current_value = coin[2] * api['data'][i]['quote']['USD']['price']
                pl_per_coin = api['data'][i]['quote']['USD']['price'] - coin[3]
                total_pl_coin = pl_per_coin * coin[2]

                total_pl += total_pl_coin
                total_current_value += current_value
                total_amount_paid += total_paid

                portfolio_id = Label(pycrypto, text=coin[0], bg='#F3F4F6', fg='black', font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
                portfolio_id.grid(row=coin_row, column=0, sticky=N+S+E+W)

                name = Label(pycrypto, text=api['data'][i]['symbol'], bg='#F3F4F6', fg='black', font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
                name.grid(row=coin_row, column=1, sticky=N+S+E+W)

                price = Label(pycrypto, text='${:,.2f}'.format(api['data'][i]['quote']['USD']['price']), bg='#F3F4F6', fg='black', font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
                price.grid(row=coin_row, column=2, sticky=N+S+E+W)

                no_coins = Label(pycrypto, text=coin[2], bg='#F3F4F6', fg='black', font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
                no_coins.grid(row=coin_row, column=3, sticky=N+S+E+W)

                amount_paid = Label(pycrypto, text='${:,.2f}'.format(total_paid), bg='#F3F4F6', fg='black', font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
                amount_paid.grid(row=coin_row, column=4, sticky=N+S+E+W)

                current_val = Label(pycrypto, text='${:,.2f}'.format(current_value), bg='#F3F4F6', fg=font_color(float('{:.2f}'.format(current_value))), font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
                current_val.grid(row=coin_row, column=5, sticky=N+S+E+W)

                pl_coin = Label(pycrypto, text='${:,.2f}'.format(pl_per_coin), bg='#F3F4F6', fg=font_color(float('{:.2f}'.format(pl_per_coin))), font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
                pl_coin.grid(row=coin_row, column=6, sticky=N+S+E+W)

                totalplcoin = Label(pycrypto, text='${:,.2f}'.format(total_pl_coin), bg='#F3F4F6', fg=font_color(float('{:.2f}'.format(total_pl_coin))), font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
                totalplcoin.grid(row=coin_row, column=7, sticky=N+S+E+W)

                coin_row += 1

    #Insert data
    symbol_txt = Entry(pycrypto, borderwidth=2, relief='groove')
    symbol_txt.grid(row=coin_row+1, column=1)

    price_txt = Entry(pycrypto, borderwidth=2, relief='groove')
    price_txt.grid(row=coin_row+1, column=2)

    amount_txt = Entry(pycrypto, borderwidth=2, relief='groove')
    amount_txt.grid(row=coin_row+1, column=3)

    add_coin = Button(pycrypto, text='Add Coin', command=insert_coin, bg='#142E54', fg='white', font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
    add_coin.grid(row=coin_row+1, column=4, sticky=N+S+E+W)

    #Update coin
    portid_update = Entry(pycrypto, borderwidth=2, relief='groove')
    portid_update.grid(row=coin_row+2, column=0)

    symbol_update = Entry(pycrypto, borderwidth=2, relief='groove')
    symbol_update.grid(row=coin_row+2, column=1)

    price_update = Entry(pycrypto, borderwidth=2, relief='groove')
    price_update.grid(row=coin_row+2, column=2)

    amount_update = Entry(pycrypto, borderwidth=2, relief='groove')
    amount_update.grid(row=coin_row+2, column=3)

    update_coin = Button(pycrypto, text='Update Coin', command=update_coin, bg='#142E54', fg='white', font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
    update_coin.grid(row=coin_row+2, column=4, sticky=N+S+E+W)

    #delete coin
    portid_delete = Entry(pycrypto, borderwidth=2, relief='groove')
    portid_delete.grid(row=coin_row+3, column=0)

    delete_coin = Button(pycrypto, text='Delete Coin', command=delete_coin, bg='#142E54', fg='white', font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
    delete_coin.grid(row=coin_row+3, column=4, sticky=N+S+E+W)

    #totals
    totalap = Label(pycrypto, text='${:,.2f}'.format(total_amount_paid), bg='#F3F4F6', fg=font_color(float('{:.2f}'.format(total_amount_paid))), font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
    totalap.grid(row=coin_row, column=4, sticky=N+S+E+W)

    totalcv = Label(pycrypto, text='${:,.2f}'.format(total_current_value), bg='#F3F4F6', fg=font_color(float('{:.2f}'.format(total_current_value))), font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
    totalcv.grid(row=coin_row, column=5, sticky=N+S+E+W)

    totalpl = Label(pycrypto, text='${:,.2f}'.format(total_pl), bg='#F3F4F6', fg=font_color(float('{:.2f}'.format(total_pl))), font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
    totalpl.grid(row=coin_row, column=7, sticky=N+S+E+W)

    api = ''

    refresh = Button(pycrypto, text='Refresh', command=reset,  bg='#142E54', fg='white', font='lato 12', borderwidth=2, relief='groove', padx='2', pady='2')
    refresh.grid(row=coin_row+1, column=7, sticky=N+S+E+W)

def app_header():
    portfolio_id = Label(pycrypto, text='Portfolio Id', bg='#142E54', fg='white', font='lato 12 bold', padx='5', pady='5', borderwidth='2', relief='groove')
    portfolio_id.grid(row=0, column=0, sticky=N+S+E+W)

    name = Label(pycrypto, text='Coin Name', bg='#142E54', fg='white', font='lato 12 bold', padx='5', pady='5', borderwidth='2', relief='groove')
    name.grid(row=0, column=1, sticky=N+S+E+W)

    price = Label(pycrypto, text='Price', bg='#142E54', fg='white', font='lato 12 bold', padx='5', pady='5', borderwidth='2', relief='groove')
    price.grid(row=0, column=2, sticky=N+S+E+W)

    no_coins = Label(pycrypto, text='Coins Owned', bg='#142E54', fg='white', font='lato 12 bold', padx='5', pady='5', borderwidth='2', relief='groove')
    no_coins.grid(row=0, column=3, sticky=N+S+E+W)

    amount_paid = Label(pycrypto, text='Total Amount Paid', bg='#142E54', fg='white', font='lato 12 bold', padx='5', pady='5', borderwidth='2', relief='groove')
    amount_paid.grid(row=0, column=4, sticky=N+S+E+W)

    current_val = Label(pycrypto, text='Current Value', bg='#142E54', fg='white', font='lato 12 bold', padx='5', pady='5', borderwidth='2', relief='groove')
    current_val.grid(row=0, column=5, sticky=N+S+E+W)

    pl_coin = Label(pycrypto, text='P/L Per Coin', bg='#142E54', fg='#F3F4F6', font='lato 12 bold', padx='5', pady='5', borderwidth='2', relief='groove')
    pl_coin.grid(row=0, column=6, sticky=N+S+E+W)

    total_pl = Label(pycrypto, text='Total P/L for Coin', bg='#142E54', fg='#F3F4F6', font='lato 12 bold', padx='5', pady='5', borderwidth='2', relief='groove')
    total_pl.grid(row=0, column=7, sticky=N+S+E+W)

app_navigation()
app_header()
my_portfolio()
pycrypto.mainloop()

cursor.close()
con.close()
