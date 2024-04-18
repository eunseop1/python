from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np

driver = webdriver.Chrome()
driver.get('https://search.shopping.naver.com/home')

try:
    driver.get('https://search.shopping.naver.com/search/all?query=실내자전거')
    time.sleep(1)

except Exception as e:
    print(e)


def findElements(p_count, j):
        
    body = j.find_element(By.XPATH, "//div[contains(translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'product_title')]/a")
    title = body.get_attribute('title')
    id = body.get_attribute('data-i')

    data[p_count]['title'] = title
    data[p_count]['id'] = id
    
    product_desc_elements = j.find_elements(By.CSS_SELECTOR, '.product_desc__m2mVJ a')
    
    if product_desc_elements:
        product_desc = product_desc_elements[0]
        desc_text = product_desc.text.strip()
        if desc_text != "":
            content_split = desc_text.split(":")
            data[p_count][content_split[0]] = content_split[-1]

    return data

count = 1
product_count = 0
data = []
current_page = 1

for i in range(count):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

    search_content_input = driver.find_elements(By.XPATH, "//div[contains(translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'product_info_area')]")

    # print(len(search_content_input))
    print(f"search_content_input            {search_content_input}")
    


    for j in search_content_input:
        data.append({})

        # print(f"j   {j}")
        # print(f"product_count    {product_count}")
        data.append(findElements(product_count, j))
        product_count += 1

    next_button = driver.find_element(By.CLASS_NAME, 'pagination_next__pZuC6')
    next_button_text = next_button.text.strip()
    if next_button_text == '다음':
        next_button.click()
        time.sleep(1)
        current_page += 1
        print(data)

    else:
        print('마지막 페이지:', current_page)
        break