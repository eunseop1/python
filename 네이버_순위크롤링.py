import requests
from bs4 import BeautifulSoup
from lxml import etree

query = input()

print('입력받은 값은 ' + query)

url = ("https://search.shopping.naver.com/search/all?query=" + query)
print("입력된 URL: " + url)

header = {'User-Agent' : 'Mozila 5.0'}
response = requests.get(url, headers=header)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    html_content = response.content
    tree = etree.HTML(html_content)

    elements = tree.xpath("//div[contains(translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'product_info_area')]")

    for element in elements:
        print("".join(element.xpath(".//text()")).strip())

else : 
    print(response.status_code)