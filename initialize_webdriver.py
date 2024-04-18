import os
import time
import socket
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def check_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def initialize_webdriver(download_dir, headless_mode=False, max_retries=5):
    # download_dir 경로 확인 및 생성
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    attempts = 0
    while attempts < max_retries:
        try:
            # Chrome 옵션 설정
            options = Options()
            options.add_experimental_option("prefs", {
                "download.default_directory": download_dir,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "plugins.always_open_pdf_externally": True
            })
            options.add_argument('--disable-gpu') # 그래픽가속 비활성화
            if headless_mode:
                options.add_argument('--headless')  # 헤드리스 모드 활성화
            service = Service(ChromeDriverManager().install())
            service.start()
            driver = webdriver.Chrome(service=service, options=options)
            time.sleep(5)

            if check_port_in_use(service.port):
                print(f"WebDriver is running on port {service.port}")
                return driver
            else:
                raise Exception("WebDriver port is not active")

        except Exception as e:
            print(f"오류 발생: {e}. 재시도 중... ({attempts+1}/{max_retries})")
            attempts += 1
            time.sleep(5)
    

    raise Exception("웹드라이버 초기화 실패: 최대 재시도 횟수 초과")
