import requests
from bs4 import BeautifulSoup
import csv

# 要爬取的網址
url = 'https://mojim.com'  # 替換為你想爬取的網址
# 發送請求並獲取頁面內容
response = requests.get(url)
if response.status_code != 200:
    print('無法獲取頁面內容')
    exit()

# 解析HTML內容
soup = BeautifulSoup(response.content, 'html.parser')

# 找到歌詞內容，這裡假設歌詞位於HTML標籤<div class="lyrics">
lyrics_div = soup.find('div', class_='lyrics')
if not lyrics_div:
    print('找不到歌詞內容')
    exit()

# 提取歌詞文字
lyrics_text = lyrics_div.get_text()

# 寫入CSV檔
with open('lyrics.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['lyrics']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'lyrics': lyrics_text})

print('歌詞已成功存入 lyrics.csv')
