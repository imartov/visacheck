from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from time import sleep
from dotenv import load_dotenv
import os
from utils import wait_random_time
from selenium.webdriver.common.keys import Keys


ua = UserAgent()
random_ua = ua.random
test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'

options = Options()

# options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
options.add_argument("--window-size=1920,1080")
# options.add_argument("--disable-extensions")

options.add_argument(f'--user-agent={random_ua}')

options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")
# options.add_argument("user-data-dir=C:\\Users\\alexa\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

driver = webdriver.Chrome(options=options)
solver = RecaptchaSolver(driver=driver)

load_dotenv()
driver.get("https://www.google.com/")
wait_random_time(fromm=0.5, to=1.0)

wait_random_time(fromm=500.4, to=1000.2)
link = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[1]/a/div/div[1]/h3/div')
link.click()

wait_random_time(fromm=4.00, to=6.23)
try:
    button_accept_cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    button_accept_cookies.click()
except:
    pass

wait_random_time(fromm=0.8, to=1.5)
button_register_filing = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div/div/div[4]/a')
button_register_filing.click()

wait_random_time(fromm=0.4, to=1.5)
button_register_filing = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/div/div/div[3]/div/ul[1]/li[1]/p/a')
button_register_filing.click()

wait_random_time(fromm=10.25, to=13.6)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
input_login = driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
input_login.send_keys(Keys.CONTROL, "a")
wait_random_time(fromm=0.34, to=1.01)
for letter in os.getenv("LOGIN"):
    input_login.send_keys(letter)
    wait_random_time(fromm=0.15, to=1.46)

# recaptcha_iframe = test_driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
sleep(2)

# solver.click_recaptcha_v2(iframe=recaptcha_iframe)