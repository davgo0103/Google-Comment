from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

# 定義要爬取的直營門市列表，格式為 (商家名稱, 商家Google Maps網址)
stores = [
    ("直營門市", "https://goo.gl/maps/FJi9fVoXjEvhCZNe8"),
    ("直營門市", "https://goo.gl/maps/mJDhMUN5j4QbHXkX8"),
    ("直營門市", "https://goo.gl/maps/8CnEkW9xNhnMuDnYA"),
    ("直營門市", "https://goo.gl/maps/P3NXJoccKgGTmP9E6"),
    ("直營門市", "https://goo.gl/maps/GCHWyq5cw2HwwgjD6"),
    ("直營門市", "https://goo.gl/maps/9tMTJxxtg74w5QtU9"),
    ("直營門市", "https://goo.gl/maps/iEUepWczNKYRtHCN9"),
    ("直營門市", "https://goo.gl/maps/s35Vk5VHYfJTaBkJ7"),
    ("直營門市", "https://goo.gl/maps/i4RonGbMvHeeX5k97"),
    ("直營門市", "https://goo.gl/maps/JAe6AbqMd54JAZ1fA"),
    ("直營門市", "https://goo.gl/maps/u6GX1YYDAy7D678FA"),
    ("直營門市", "https://goo.gl/maps/fHnxkD21Wz4WGKQM7"),
    ("直營門市", "https://goo.gl/maps/LcdRoq93gtkXKqMP9"),
    ("直營門市", "https://goo.gl/maps/myDUWtWAP1cvjk4H7"),
    ("直營門市", "https://goo.gl/maps/EvpEUZPKUZbxrFNR8"),
    ("直營門市", "https://goo.gl/maps/k4mACUbSEQW6LnHw5"),
    ("直營門市", "https://goo.gl/maps/9ynib89nZMRwkFKC8"),
    ("直營門市", "https://goo.gl/maps/4gxshP5yWTYuKiu67"),
    ("直營門市", "https://goo.gl/maps/P39EVoXa1K6woiPWA"),
    ("直營門市", "https://goo.gl/maps/KXx5uptBa2ZGp9mo9"),
    

]

# 開啟 headless 模式，不顯示瀏覽器視窗
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')

# 開啟瀏覽器
driver = webdriver.Chrome(options=chrome_options)

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
    review_count = str(re.search(r"\d+", review_count_str.replace(',', '')).group(0))

    # 顯示評論數
    store_name =  review_count_tag._parent.title.replace('- Google 地圖', '')
    print(f"{store_name}的評論數：{review_count}")
# 關閉瀏覽器
driver.quit()