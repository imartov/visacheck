import json, os
from time import sleep
from random import randint

from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from dotenv import load_dotenv
import undetected_chromedriver as uc
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from utils import wait_random_time, get_random_int
from main import ScrapyPage


def test_scrapy() -> None:

    load_dotenv()
    # s = Service(executable_path=os.getenv("PATH_DRIVER"))
    ua = UserAgent()
    random_ua = ua.random
    # test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

    options = Options()
    options.headless = False
    # options.add_experimental_option("excludeSwitches", ["enable-automation"]) # undetected_chromedriver
    # options.add_experimental_option('useAutomationExtension', False) # undetected_chromedriver
    # options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
    # options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f'--user-agent={random_ua}')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")

    driver = uc.Chrome(options=options,
                       browser_executable_path="visacheckvenv\\chrome-win\\chrome.exe",
                       driver_executable_path="visacheckvenv\\chromedriver.exe")


    driver.maximize_window()

    driver.get("https://www.django-rest-framework.org/")
    wait_random_time(fromm=0.5, to=1.0)
    
    sp = ScrapyPage()
    sp.smooth_scroll(driver=driver, height=2000, step=randint(4, 8))
    wait_random_time(fromm=2.0, to=3.0)
    sp.smooth_scroll(driver=driver, height=1000, step=randint(4, 8), up=True)

    wait = WebDriverWait(driver, 10)

    document_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-rodzaj-container"]')))
    document_button.click()

    document_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-rodzaj-container"]')))
    counter = 1
    while counter <= 20:
        if counter % 4 == 0: # scroll every 4 elements or so
            document_button.send_keys(Keys.ARROW_DOWN)
        element = WebDriverWait(driver,5,poll_frequency=.2).until(EC.element_to_be_clickable((By.XPATH, "//li[text()='Wezwanie do zapłaty (z odsetkami)']")))
        # element.click
        counter += 1

    document_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-rodzaj-container"]')))
    document_button.click()

    # doc_type = driver.find_element(By.XPATH, "//li[text()='Wezwanie do zapłaty (z odsetkami)']")
    # actions = ActionChains(driver)
    # actions.move_to_element(doc_type).perform()

    # doc_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-rodzaj-result-ap3e-34"]')))
    # doc_type.click()
    wait_random_time(fromm=20.0, to=30.0)

    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
    element.send_keys(Keys.CONTROL, "a")
    element.send_keys("this method is cchecking")
    # sp = ScrapyPage().enter_text_data(driver=driver, text="Any text", xpath='//*[@id="APjFqb"]')

    driver.implicitly_wait(10)
    exist = driver.find_element(By.XPATH, "//a[text()='Django REST framework']")
    exist.click()

    driver.implicitly_wait(10)
    wait_random_time(fromm=1.6, to=2.2)
    main_page = driver.find_element(By.XPATH, "//a[text()='Installation']")
    main_page.click()

    driver.implicitly_wait(10)
    wait_random_time(fromm=1.6, to=2.2)
    main_page = driver.find_element(By.XPATH, "//a[text()='Requirements']")
    main_page.click()

    wait_random_time(fromm=5.6, to=10.2)

    driver.quit()


def solve_captha() -> None:
    ua = UserAgent()
    random_ua = ua.random

    options = Options()
    options.headless = False
    # options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f'--user-agent={random_ua}')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")

    driver = uc.Chrome(options=options,
                       browser_executable_path="visacheckvenv\\chrome-win\\chrome.exe",
                       driver_executable_path="visacheckvenv\\chromedriver.exe")

    solver = RecaptchaSolver(driver=driver)

    driver.get('https://www.google.com/recaptcha/api2/demo')

    recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')

    solver.click_recaptcha_v2(iframe=recaptcha_iframe)
    driver.quit()


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