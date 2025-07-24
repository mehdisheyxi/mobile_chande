from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_price(phone):
    options = Options()
    options.headless = ("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.digikala.com/")
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys(phone)
        search_box.submit()
        time.sleep(5)
        price_element = driver.find_element(By.XPATH,
                                            '//*[@id="ProductListPagesWrapper"]/section/div[5]/div[1]/a/div/article/div[2]/div[2]/div[4]/div[1]/div/span')
        price = price_element.text
        return price

    except Exception as e:
        print(e)

print(get_price('iphone'))
