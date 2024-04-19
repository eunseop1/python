from playwright.sync_api import sync_playwright

# with문 은 끝나면 알아서 브라우저가 종료된다
# 이 경우에는 close()를 넣어줄 이유는 없지만 일단 넣었다
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://naver.com', wait_until='networkidle')
#     print(page.title())
    
#     input('대기중>>>>\t')
    
#     browser.close()

# 크로미어 라는 자체 브라우저를 사용한다
# 해당 브라우저는 크롬이랑 같으나, 업데이트가 안된다

# 현재 코드는 새창이 계속 뜨기에 좋은 코드가 아니다.
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, args=["--start-maximized"])
#     page = browser.new_page(no_viewport=True)
#     page.goto('https://naver.com', wait_until='networkidle')
#     print(page.title())
    
#     # //*[@id="shortcutArea"]/ul/li[6]/a
    
#     # 만약 내가 가져온 xpath가 내가 원하는 것으로 제대로 가져왔는지 확인하려면
#     # F12를 누르고 브라우저 html안에 Ctrl + F 로 검색창을 열고 붙여넣어 엔터해보자
#     # 그러면 해당하는 xpath를 표시해주는데 이를 통해 내가 제대로 가져왔는지 확인 가능하다
    
#     # GPT에게 물을때는 ? 보다는 명령어로
#     # 잘알려주면 팁을 준다는 식으로 딜을 하면 좋은 결과를 준다
#     # 왜 갑자기 GPT 이야기가 나왔느냐? 원래는 개발자가 일일히 xpath를 찾아서 구현하고, 예외처리를 해야 했지만, GPT를 통해서 이젠 물어보면서 가능하기 때문이다
     
    
#     # xpath로 가져왔는데, 쌍따음표가 이미 문자에 있다.
#     # 따라서 ' ' 안에 입력해야 제대로 작동된다
#     page.click('//*[@id="shortcutArea"]/ul/li[6]/a')
#     input('대기중>>>>\t')
    
#     browser.close()
    
    
    
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, args=["--start-maximized"])
#     page = browser.new_page(no_viewport=True)
#     page.goto('https://naver.com', wait_until='networkidle')
#     print(page.title())

#     # 요소안의 href 속성을 가져오게 한다
#     link_url = page.get_attribute('//*[@id="shortcutArea"]/ul/li[6]/a', 'href')
#     print(link_url)
    
#     page.goto(link_url)
    
#     input('대기중>>>>\t')
    
#     browser.close()





# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, args=["--start-maximized"])
#     page = browser.new_page(no_viewport=True)
#     page.goto('https://naver.com', wait_until='networkidle')
#     print(page.title())

#     # 요소안의 href 속성을 가져오게 한다
#     link_url = page.get_attribute('//*[@id="shortcutArea"]/ul/li[6]/a', 'href')
#     print(link_url)
    
#     page.goto(link_url)
    
#     input('대기중>>>>\t')
    
#     browser.close()
    
# ================================================================================
    
# 만약 파이선의 실행이 myenv로 안된다면 + 옆의 화살표를 눌러서
# Select Default Profile을 눌러서 
# Command Prompt를 누른다

# import pandas as pd    
    
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, args=["--start-maximized"])
#     page = browser.new_page(no_viewport=True)
#     page.goto('https://naver.com', wait_until='networkidle')
#     print(page.title())

#     link_url = page.get_attribute('//*[@id="shortcutArea"]/ul/li[6]/a', 'href')
#     # print(link_url)
    
#     page.goto(link_url)
    
#     # //*[@id="frame_ex1"]
    
#     page.click('//*[@id="menu"]/ul/li[4]/a/span')
    
#     doc_src = page.get_attribute('//*[@id="frame_ex1"]','src')
    
#     # print(doc_src)
#     docu_list = pd.read_html(link_url + doc_src, encoding='CP949')
    
#     df = docu_list[0]
    
#     df.columns = df.columns.droplevel(0)
#     # 컬럼 레벨 0 삭제
#     # (통화명, 통화명) 컬럼을
#     # 통화명 컬럼 처럼 간단히 하게 하기 위함
    
#     print(df)
#     # 결과값을 리스트로 가져왔다는 것을 알수 있다
#     # 첫번째 를 가져오면 데이터 프레임 형태가 될것이다
    
#     print(df.info())
#     # 확인해보면 컬럼명이 두개가 있다
    
#     input('대기중>>>>\t')
    
#     browser.close()
    
    
# ================================================================================
    
# 실습
# 매매기준율 1000 이상의 통화량과 매매기준율을 구하고 엑셀로 저장하기

# import pandas as pd    
    
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, args=["--start-maximized"])
#     page = browser.new_page(no_viewport=True)
#     page.goto('https://naver.com', wait_until='networkidle')

#     link_url = page.get_attribute('//*[@id="shortcutArea"]/ul/li[6]/a', 'href')
    
#     page.goto(link_url)
    
#     page.click('//*[@id="menu"]/ul/li[4]/a/span')
    
#     doc_src = page.get_attribute('//*[@id="frame_ex1"]','src')
    
#     docu_list = pd.read_html(link_url + doc_src, encoding='CP949')
    
#     df = docu_list[0]
    
#     df.columns = df.columns.droplevel(0)
#     # 컬럼 레벨 0 삭제
#     # (통화명, 통화명) 컬럼을
#     # 통화명 컬럼 처럼 간단히 하게 하기 위함
    
#     # result_df = df[df['매매기준율'].values >= 1000]
    
#     # result_df= result_df.groupby('통화명')[['매매기준율']].agg(['max'])
#     # result_df.('이것은실험삼아만든.csv')
    
#     result_df = df.loc[df['매매기준율'] >= 1000 ,['통화명', '매매기준율']]
#     result_df.to_excel('매매기준율이_천_이상인_통화명과_매매기준율.xlsx', index=False)
    
#     browser.close()
        
# ==============================================================================================

# 실습
# 네이버에 RPA 검색
# 뉴스 탭 이동
# 뉴스 제목, 내용, 주소를 엑셀로 저장
# query_selector_all 사용

import pandas as pd    
    
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    # page.goto('https://search.naver.com/search.naver?query=RPA', wait_until='networkidle')
    page.goto('https://naver.com', wait_until='networkidle')

    page.fill('//*[@id="query"]', 'RPA')
    
    page.click('//*[@id="sform"]/fieldset/button')
    
    page.click('//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a')
    
    # //html/body/div[3]/div[2]/div/div[1]/section
    
    # elements_xpath = '//*[@id="main_pack"]/section/div[1]/div[2]/ul/li/div/div/div/a'
    # elements_xpath = '//*[@id="main_pack"]/section'
    # //*[@id="main_pack"]/section/div[1]/div[2]/ul
    
    # elements_xpath = '//*[@id="main_pack"]/section/div[1]/div[2]/ul'
    elements_xpath = '//*[@id="main_pack"]/section/div[1]/div[2]/ul/li/div/div/div/a[2]'
    # elements_xpath = page.get_attribute('//*[@id="main_pack"]/section/div[1]/div[2]/ul/li/div/div/div/a[1]', 'title')
    
    news_titles = []
    news_elements = page.query_selector_all(elements_xpath)

    # 각 요소에서 제목 추출
    for element in news_elements:
        # 요소 내에 있는 제목 텍스트 가져오기
        title = element.inner_text()
        # 추출된 제목을 리스트에 추가
        news_titles.append(title)
    
    # news_elements = []
    # news_elements = elements_xpath
    
    print(news_titles)
    
    # //*[@id="sp_nws6"]/div[1]/div/div[2]/a[2]
    # //*[@id="main_pack"]/section
    # sp_nws1 > div.news_wrap.api_ani_send > div > div.news_contents > a.news_tit
    # //html/body/div[3]/div[2]/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[1]/div/div[2]/a[2]
    # //html/body/div[3]/div[2]/div/div[1]/section/div[1]/div[2]/ul/li[1]/div[1]/div/div[2]/a[2]
    news_title = page.get_attribute('//html/body/div[3]/div[2]/div/div[1]/section/div[1]/div[2]/ul/li[1]/div[1]/div/div[2]/a[2]','title')
    print(news_title)

    # link_url = page.get_attribute('//*[@id="query"]', 'input')
    
    # page.goto(link_url)
    
    # page.click('//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[1]/a')
    
    # doc_src = page.get_attribute('//*[@id="frame_ex1"]','src')
    
    # docu_list = pd.read_html(link_url + doc_src, encoding='CP949')
    
    # df = docu_list[0]
    
    # df.columns = df.columns.droplevel(0)
    # 컬럼 레벨 0 삭제
    # (통화명, 통화명) 컬럼을
    # 통화명 컬럼 처럼 간단히 하게 하기 위함
    
    # result_df = df.loc[df['매매기준율'] >= 1000 ,['통화명', '매매기준율']]
    # result_df.to_excel('매매기준율이_천_이상인_통화명과_매매기준율.xlsx', index=False)
    
    input("asdasdsa")
    
    browser.close()