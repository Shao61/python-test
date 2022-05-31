import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://goodinfo.tw/tw/StockBzPerformance.asp?STOCK_ID=2330'
headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'  
}
res = rq.get(url, headers = headers)
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'lxml')
data = soup.select_one('#txtFinDetailData')

df = pd.read_html(data.prettify())
print(df)