import os
from time import sleep

from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from dotenv import load_dotenv

from utils import wait_random_time


def find_entry():
    ua = UserAgent()
    random_ua = ua.random

    options = Options()
    # options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
    options.add_argument("--window-size=1920,1080")
    options.add_argument(f'--user-agent={random_ua}')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")
    # options.add_argument(f"user-data-dir={os.getenv('DIR_CHROME_PROFILE')}")

    driver = webdriver.Chrome(options=options)
    solver = RecaptchaSolver(driver=driver)
    load_dotenv()

    # TODO: redirect from google search
    driver.get(os.getenv("URL"))

    wait_random_time(fromm=10.25, to=13.6)
    # TODO: scroll down
    button_accept_cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    button_accept_cookies.click()

    wait_random_time(fromm=0.76, to=2.87)
    language_drop_down_list = driver.find_element(By.XPATH, '//*[@id="dropdownMenuButton"]')
    language_drop_down_list.click()

    wait_random_time(fromm=0.29, to=2.36)
    select_russian_language = driver.find_element(By.XPATH, '/html/body/app-root/div/header/div/div/div/div/a[2]')
    select_russian_language.click()

    wait_random_time(fromm=1.61, to=3.02)
    input_login = driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
    input_login.send_keys(Keys.CONTROL, "a")
    wait_random_time(fromm=0.34, to=1.01)
    for letter in os.getenv("LOGIN"):
        input_login.send_keys(letter)
        wait_random_time(fromm=0.34, to=0.76)

    wait_random_time(fromm=1.23, to=3.34)
    input_password = driver.find_element(By.XPATH, '//*[@id="mat-input-1"]')
    input_password.send_keys(Keys.CONTROL, "a")
    wait_random_time(fromm=0.34, to=1.01)
    for letter in os.getenv("PASSWORD"):
        input_password.send_keys(letter)
        wait_random_time(fromm=0.34, to=0.76)

    # silve captha
    wait_random_time(fromm=1.36, to=2.36)
    recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
    wait_random_time(fromm=3.89, to=5.12)
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)

    # click button login
    wait_random_time(fromm=2.01, to=3.34)
    button_login = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button')
    button_login.click()

    # click button find entry
    wait_random_time(fromm=5.89, to=8.12)
    button_find_entry = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-dashboard/section[1]/div/div[2]/div/button')
    button_find_entry.click()
    
    # TODO: fix
    # выбрать визовый центр
    wait_random_time(fromm=0.5, to=1.5)
    button_find_entry = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[1]/mat-form-field/div/div[1]/div[3]')
    button_find_entry.click()

    # выбрать визовый центр
    wait_random_time(fromm=0.5, to=1.5)
    button_find_entry = driver.find_element(By.XPATH, '//*[@id="mat-option-5"]/span')
    button_find_entry.click()

    wait_random_time(fromm=4.0, to=6.5)
    button_find_entry = driver.find_element(By.XPATH, '//*[@id="mat-select-value-3"]')
    button_find_entry.click()

    # выбрать категорию записи
    wait_random_time(fromm=0.5, to=1.5)
    button_find_entry = driver.find_element(By.XPATH, '//*[@id="mat-option-250"]/span')
    button_find_entry.click()

    wait_random_time(fromm=0.5, to=1.5)
    button_find_entry = driver.find_element(By.XPATH, '//*[@id="mat-option-250"]/span')
    button_find_entry.click()

    # выбрать подкатегорию
    wait_random_time(fromm=3.0, to=5.0)
    button_find_entry = driver.find_element(By.XPATH, '//*[@id="mat-select-value-5"]')
    button_find_entry.click()

    wait_random_time(fromm=0.5, to=1.5)
    button_find_entry = driver.find_element(By.XPATH, '//*[@id="mat-option-252"]/span')
    button_find_entry.click()

    # ввести дату рождения
    wait_random_time(fromm=3.0, to=5.0)
    button_find_entry = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[4]/div[3]/input')
    button_find_entry.send_keys(Keys.CONTROL, "a")
    wait_random_time(fromm=0.34, to=0.76)
    for letter in os.getenv("DATE_BIRTH"):
        input_login.send_keys(letter)
        wait_random_time(fromm=0.34, to=0.76)

    # выбрать гражданство
    wait_random_time(fromm=0.5, to=1.5)
    button_find_entry = driver.find_element(By.XPATH, '//*[@id="mat-select-value-7"]')
    button_find_entry.click()

    wait_random_time(fromm=1.5, to=2.5)
    button_find_entry = driver.find_element(By.XPATH, '//*[@id="mat-option-24"]/span')
    button_find_entry.click()

    wait_random_time(fromm=20.5, to=30.7)


# selenium
fourth = '//*[@id="mat-input-0"]' # click input mail: alexandr.kosyrew@mail.ru
fifth = '//*[@id="mat-input-1"]' # click input password: 5wVGLdtIZ$
sixth = '//*[@id="recaptcha-anchor"]/div[1]' # click captcha
seventh = 'choise any objects'
eith = '/html/body/app-root/div/div/app-dashboard/section[1]/div/div[1]/div[2]/button/span[1]' # button reserverd a meeting
next = '//*[@id="mat-select-6"]/div/div[2]' # click button of opened list for location
next = ''

def main():
    find_entry()

if __name__ == "__main__":
    main()