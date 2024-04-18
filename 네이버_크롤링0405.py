from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

def collect_data_from_page(driver, page_num):

    def scroll_to_end(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            ActionChains(driver).send_keys(Keys.END).perform()
            time.sleep(5)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    max_retries = 5
    retries = 0

    data = []

    while retries < max_retries:
        try:
            time.sleep(2)
            scroll_to_end(driver)

            ActionChains(driver).send_keys(Keys.HOME).perform()

            elements = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'basicList_list_basis')]//div[contains(translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'product_item')]")))

            for index, element in enumerate(elements, start=1):
                class_text = element.get_attribute('class')

                if "adProduct_item" in class_text:
                    category = "광고"
                elif "product_item" in class_text:
                    category = "일반"
                else:
                    category = "알 수 없음"

                title_name = element.find_element(By.XPATH, ".//div[contains(translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'product_title')]").text
                brand = title_name.split(' ')[0]
                product_name = " ".join(title_name.split(' ')[1:])

                img_area = element.find_element(By.XPATH, ".//div[contains(@class, 'thumbnail_thumb_wrap')]/a")
                href_url = img_area.get_attribute('href')
                img_tag = WebDriverWait(element, 20).until(EC.presence_of_element_located((By.XPATH, ".//div[contains(@class, 'thumbnail_thumb_wrap')]/a/img")))
                img_src = img_tag.get_attribute('src')
                i_num = img_area.get_attribute('data-i')

                data.append({"순위": index, "페이지 번호": page_num, "분류": category, "상품 이미지": img_src, "브랜드": brand, "상품명": product_name, "상품번호": i_num, "하이퍼링크": href_url})
            
            break
        
        except Exception as e:
            print(f"에러 발생: {e}. 재시도 중... ({retries+1}/{max_retries})")
            retries += 1
            if retries == max_retries:
                print("최대 재시도 횟수 도달. 작업 중단.")

    return data


def main():
    driver = webdriver.Chrome()
    driver.get('https://search.shopping.naver.com/home')

    try:
        driver.get('https://search.shopping.naver.com/search/all?query=실내자전거')
        time.sleep(1)

    except Exception as e:
        print(e)

    count = 1
    current_page = 1
    all_data = []

    for page_num in range(count):
        data = collect_data_from_page(driver, current_page)
        all_data.extend(data)

        next_button = driver.find_element(By.CLASS_NAME, 'pagination_next__pZuC6')
        next_button_text = next_button.text.strip()
        if next_button_text == '다음':
            next_button.click()
            time.sleep(1)
            current_page += 1
        else:
            print('마지막 페이지:', current_page)
            break

    # 데이터프레임으로 변환 (선택사항)
    df = pd.DataFrame(all_data)
    print(df)

    # 종료
    driver.quit()


if __name__ == "__main__":
    main()
