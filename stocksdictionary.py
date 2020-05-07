# dictionary of stock ticker symbols and price

ticker_price = {'AMZN':890, 'GOOG':620, 'AAPL':800, 'MFST':352, 'WMT':258, 'INTC':325, 'VZ':198, 'FB':689, 'TWTR':461, 'SNAP':185}

while(True):

    company_ticker = input("Type a company ticker symbol, to look up their value(enter Q to quit): ").upper()

    if company_ticker == 'Q':
        break

    if company_ticker in ticker_price.keys():
        print("The price of " + company_ticker + " is $" + str('{:,}'.format(ticker_price[company_ticker])))
    else:
        print("We could not locate,", company_ticker, "try another ticker symbol.")
