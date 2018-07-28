#http://www.86duino.com/?page_id=2255&lang=TW
#導入兩個爬取資料會使用的庫
import requests
from bs4 import BeautifulSoup
#目標網址
targetURL = 'http://www.86duino.com/?page_id=2255&lang=TW'
#(1)建立請求
req = requests.get(targetURL)
#(2)解析請求的內容
soup = BeautifulSoup(req.text, 'lxml')
#(3)透過Chrome觀察HTML結構
#(4)以下逐層「抽絲剝繭」
#找到一個table：使用find()加上條件將table取出
table = soup.find('table', attrs={'cellspacing': '0'})
#只有一個row：
rows = table.find('tr')
#有三個td
tds = rows.find_all('td')
#遍歷
for td in tds:
    #取出td裡全部元素
    datas = td.find_all()
    #遍歷
    for item in datas:
        #元素標籤名稱==?時
        if item.name == 'h4':
            print('H4：', item.text)
        elif item.name == 'h6':
            print('  H6：', item.text)
        elif item.name == 'li':
            print('    li：', item.text)
        
#迴圈跑完就完成table資料的解析了

print('=====END=====')

