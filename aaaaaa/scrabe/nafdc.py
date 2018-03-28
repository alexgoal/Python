import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

urls = [
    "http://www.nafdc.gov.cn/House/BuildingInfo?BuildingId=7765&ProjectId=&CaseId=011711020119"
]

charIntMap = {'01': 'A', '02': 'B', '03': 'C', '05': 'D', '06': 'E', '07': 'F'}

files = [
    "保险教室.json"
]


def get_price(url):
    res = requests.get(url)
    res.encoding = "utf-8"

    soup = BeautifulSoup(res.text, 'html.parser')
    label = soup.select_one("label")
    price = label.contents[0]
    price = price[2:]

    return price


def getPosInExcel(adr):
    max_col = 33
    adr = adr[:-1]
    len = adr.__len__()
    row = adr[len - 2] + adr[len - 1]
    col = adr[:len - 2]
    col = int(col)
    col = max_col - col + 1
    print(str(col) + ' ' + row)
    idx = charIntMap[row] + '' + str(col)
    print(idx)
    return idx


for i in range(len(urls)):
    wb = Workbook()
    sheet = wb.active
    sheet.title = "New Sheet"
    for letter in charIntMap.values():
        sheet.column_dimensions[letter].width = 15
    response = requests.get(urls[i])
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, 'html.parser')
    filename = soup.select_one('title')
    filename = filename.contents[0]
    filename = filename[3:]
    filename = filename[:-2]
    buildsToSell = soup.find_all(attrs={'class': 'sty_3'})
    buildsSelled = soup.find_all(attrs={'class': 'sty_5'})
    builds = buildsToSell + buildsSelled + soup.find_all(attrs={'class': 'sty_4'})
    contents = {}
    for build in builds:
        if build.contents[0] is not None and build.contents[0].contents[0] is not None \
                and build.contents[0].attrs is not None and 'href' in build.contents[0].attrs:
            buildwhere = build.contents[0].contents[0]
            href = 'http://www.nafdc.gov.cn/House/' + build.contents[0].attrs['href']
            contents[buildwhere] = href

    keys = sorted(contents.keys())
    print(keys)
    for k, v in contents.items():
        # print(k + ' ' + v)
        pos = getPosInExcel(k)
        price = get_price(v)
        # print(price)
        sheet[pos] = k + ' ' + price + '元'
        print(k + ' ' + price + '元')
    wb.save(filename + '.xlsx')
