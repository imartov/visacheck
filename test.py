import json, os
from time import sleep

from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from dotenv import load_dotenv

from utils import wait_random_time
from main import ScrapyPage


def test_scrapy() -> None:

    ua = UserAgent()
    random_ua = ua.random
    # test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

    options = Options()
    # options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
    options.add_argument("--window-size=1920,1080")
    options.add_argument(f'--user-agent={random_ua}')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=options)

    load_dotenv()
    driver.get("https://www.django-rest-framework.org/api-guide/permissions/")
    wait_random_time(fromm=1.5, to=2.5)

    scrapy = ScrapyPage()
    exist = scrapy.check_displayed_element(driver=driver, xpath="//a[text()='Django REST framework False']")
    print(exist)

    # wait_random_time(fromm=1.6, to=2.2)
    # main_page = driver.find_element(By.XPATH, "//a[text()='Installation']")
    # main_page.click()

    # wait_random_time(fromm=1.6, to=2.2)
    # main_page = driver.find_element(By.XPATH, "//a[text()='Requirements']")
    # main_page.click()

    # wait_random_time(fromm=20.6, to=30.2)

def compare(one:str, two:str) -> bool:
    if one == two:
        print(True)
    else:
        print(False)


def check_json() -> None:
    with open("xpaths_visa_type.json", "r", encoding="utf-8") as file:
        xpaths_visa_type_list = json.load(file)
    for city, visa_data in xpaths_visa_type_list.items():
        if "subcategory" in visa_data:
            print(city, "subcategory exist")
        else:
            print(city, "subcategory not exist")


def main() -> None:
    test_scrapy()
    
if __name__ == "__main__":
    main()