from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np
import threading

driver = webdriver.Chrome()
driver.get('https://search.shopping.naver.com/home')


try:
    driver.get('https://search.shopping.naver.com/search/all?query=실내자전거')
    time.sleep(1)

except(e):
    print(e)

def findElements(p_count, j, By, selector):
    for k in j.find_elements(By, selector):
        if k.text.strip() != "":
            content_split = k.text.split(":")
            data[p_count][content_split[0]] = content_split[-1]

count = 1
product_count = 0
data = []
current_page = 1

for i in range(count):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

    search_content_input = driver.find_elements(By.CLASS_NAME, "product_info_area__xxCTi")
    # search_content_input = driver.find_elements(By.XPATH, "//div[contains(translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'product_info_area')]")

    print(len(search_content_input))

    for j in search_content_input:
        data.append({})

        content = threading.Thread(target = findElements, args=(product_count, j, By.CSS_SELECTOR, 'product_desc__m2mVJ a'))
        content.start()

        body = j.find_element(By.XPATH, "//div[contains(translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'product_title')]/a")

        title = body.get_attribute('title')
        print(title)

        cost = j.find_element(By.CSS_SELECTOR, '.price_num__S2p_v em').text
        id = body.get_attribute('data-i')
        print(id)

        data[product_count]['title'] = title
        data[product_count]['id'] = id

        content.join()
        product_count += 1
    
    # page = driver.find_element(By.CLASS_NAME, 'pagination_next__pZuC6')
    # print('성공페이지', int(page.text) -1)
    # page.click()
    # time.sleep(1)

    next_button = driver.find_element(By.CLASS_NAME, 'pagination_next__pZuC6')
    next_button_text = next_button.text.strip()
    if next_button_text == '다음':
        next_button.click()
        time.sleep(1)
        current_page += 1

        print(data)

    else:
        # 다음 버튼이 '다음'이 아니면 마지막 페이지이므로 종료
        print('마지막 페이지:', current_page)
        break



#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div > div.adProduct_info_area__dTSZf > div.adProduct_title__amInq > a

#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(2) > div > div > div.adProduct_info_area__dTSZf > div.adProduct_title__amInq > a


# //div[contains(translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'product_info_area')]
# //*[@id="content"]/div[1]/div[2]/div/div[5]/div/div/div[1]