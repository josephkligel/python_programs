lst = ['USD', 'CNY', 'JPY', 'EUR', 'GBP', 'PHP', 'NZD', 'AUD']

def check_list(currency):
    if currency in lst:
        return currency
    else:
        print("Currency was not found. Make sure the currency is in all caps.")
