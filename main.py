import yfinance as yf


msft = yf.Ticker("adyx")

# print(msft.info)

hist = msft.history(period="5d")
print(hist)