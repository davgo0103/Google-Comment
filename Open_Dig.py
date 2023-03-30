from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

# 定義要爬取的直營門市列表，格式為 (商家名稱, 商家Google Maps網址)
stores = [
    ("直營門市A", "https://www.google.com.tw/maps/place/%E5%8F%B0%E5%8C%97%E5%90%9B%E6%82%85%E9%85%92%E5%BA%97%E5%9C%B0%E4%B8%8B%E5%81%9C%E8%BB%8A%E5%A0%B4/@25.0329751,121.5613276,17z/data=!4m6!3m5!1s0x3442abb707092627:0x65eeaae5f6c77bc4!8m2!3d25.0355528!4d121.5631579!16s%2Fg%2F11h9pnr4hr"),
    ("直營門市B", "https://www.google.com.tw/maps/place/Grand+Hyatt+Taipei/@25.0329751,121.5613276,17z/data=!3m1!5s0x3442abb7a7f759e9:0x77e77ba535f937e4!4m9!3m8!1s0x3442abb7a75a2db7:0x44cef53b99be635a!5m2!4m1!1i2!8m2!3d25.0353727!4d121.5626133!16s%2Fm%2F026wkvf"),
    ("直營門市C", "https://www.google.com.tw/maps/place/%E5%98%9F%E5%98%9F%E6%88%BF%E4%B8%96%E8%B2%BF%E7%AB%99/@25.0329751,121.5613276,17z/data=!4m6!3m5!1s0x3442abb63b59847d:0xf0a1c92305673cdb!8m2!3d25.0341587!4d121.560726!16s%2Fg%2F12q4w2s_7"),
]

# 開啟瀏覽器
driver = webdriver.Chrome()

# 設定等待網頁加載完成的時間
wait = WebDriverWait(driver, 10)

# 逐一爬取商家評論數
for store in stores:
    # 前往商家Google Maps網址
    driver.get(store[1])

    # 等待評論數的HTML標籤出現
    review_count_tag = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[jsaction*='pane.reviewChart']")))

    # 使用BeautifulSoup解析網頁內容
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 從標籤中提取評論數字串
    review_count_str = review_count_tag.accessible_name
    
    # 提取數字部分
    review_count = int(re.search(r"\d+", review_count_str).group(0))

    # 顯示評論數
    print(f"{store[0]}的評論數：{review_count}")
# 關閉瀏覽器
driver.quit()