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

    driver = webdriver.Chrome(options=options)
    solver = RecaptchaSolver(driver=driver)
    load_dotenv()

    # TODO: redirect from google search
    # TODO: open Chrome with logined user
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
        wait_random_time(fromm=0.15, to=1.46)

    wait_random_time(fromm=1.23, to=3.34)
    input_password = driver.find_element(By.XPATH, '//*[@id="mat-input-1"]')
    input_password.send_keys(Keys.CONTROL, "a")
    wait_random_time(fromm=0.34, to=1.01)
    for letter in os.getenv("PASSWORD"):
        input_password.send_keys(letter)
        wait_random_time(fromm=0.15, to=1.46)

    wait_random_time(fromm=1.36, to=2.36)
    recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
    wait_random_time(fromm=3.89, to=5.12)
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)

    wait_random_time(fromm=2.01, to=3.34)
    button_login = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button')
    button_login.click()

    wait_random_time(fromm=10.89, to=12.12)
    button_find_entry = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-dashboard/section[1]/div/div[1]/div[2]/button/span[1]')
    button_find_entry.click()

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