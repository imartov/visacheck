import os, json
from time import sleep
from random import randint
from datetime import datetime

from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from dotenv import load_dotenv
import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from utils import *
from tg import *

load_dotenv()

class ScrapyPage:
    ''' class for scrapy page '''
    def __init__(self) -> None:
        self.exception = False

    def enter_text_data(self, driver, xpath:str, text:str) -> None:
        ''' method for enter text data to input field '''
        element = driver.find_element(By.XPATH, xpath)
        element.send_keys(Keys.CONTROL, "a")
        wait_random_time(fromm=0.05, to=0.25)
        element.send_keys(Keys.DELETE)
        wait_random_time(fromm=0.11, to=0.45)
        for letter in text:
            element.send_keys(letter)
            wait_random_time(fromm=0.11, to=0.45)

    def check_displayed_element(self, driver, xpath:str) -> bool:
        ''' this method is checking if element displayed '''
        try:
            element = driver.find_element(By.XPATH, xpath).is_displayed()
            return True
        except:
            return False
        
    def smooth_scroll(self, driver, height:int, step:int, up=False, end=False) -> None:
        ''' this method is for smooth scroll to bottom or top '''
        total_height = int(driver.execute_script("return document.body.scrollHeight")) if end else height
        if up:
            current_height = driver.execute_script("return window.pageYOffset")
            init_height = current_height
            while init_height >= height:
                driver.execute_script("window.scrollTo({}, {});".format(current_height, init_height))
                init_height -= step
        else:
            for i in range(1, total_height, step):
                driver.execute_script("window.scrollTo(0, {});".format(i))

    def login_recaptha(self, driver) -> None:
        solver = RecaptchaSolver(driver=driver)
        wait = WebDriverWait(driver, 10)
        # enter login
        wait_random_time(fromm=1.61, to=3.02)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-input-0"]')))
        self.enter_text_data(driver=driver, xpath='//*[@id="mat-input-0"]', text=os.getenv("LOGIN"))

        # enter password
        wait_random_time(fromm=1.23, to=3.34)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-input-1"]')))
        self.enter_text_data(driver=driver, xpath='//*[@id="mat-input-1"]', text=os.getenv("PASSWORD"))

        # solve captha
        wait_random_time(fromm=1.36, to=2.36)
        recaptcha_iframe = wait.until(EC.element_to_be_clickable((By.XPATH, '//iframe[@title="reCAPTCHA"]')))
        wait_random_time(fromm=3.89, to=5.12)
        solver.click_recaptcha_v2(iframe=recaptcha_iframe)

        # click button login
        wait_random_time(fromm=2.01, to=3.34)
        button_login = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button')))
        button_login.click()

        # click button find entry
        wait_random_time(fromm=4.0, to=6.12)
        button_find_entry = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div/app-dashboard/section[1]/div/div[2]/div/button')))
        button_find_entry.click()

    def init_driver(self) -> object:
        ua = UserAgent()
        random_ua = ua.random
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

        options = Options()
        options.headless = False
        # options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
        options.add_argument("--window-size=1920,1080")
        options.add_argument(f'--user-agent={ua}')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument('--headless')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--disable-gpu')
        # options.add_argument(f"user-data-dir={os.getenv('DIR_CHROME_PROFILE')}")

        
        driver = uc.Chrome(browser_executable_path=os.getenv("PATH_BROWSER"),
                            driver_executable_path=os.getenv("PATH_DRIVER"),
                            options=options)
        driver.maximize_window()
        driver.get(os.getenv("URL"))
        wait_random_time(fromm=8.0, to=10.0)
        wait = WebDriverWait(driver, 10)
        # accept cookies
        button_accept_cookies = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
        button_accept_cookies.click()
        return driver
    
    def find_entry(self, driver:object) -> None:
        ''' main func for scrapy page of visa '''
        send_mess_text(path_to_message="tgdata\\messages\\run_bot.txt")
        with open("xpaths_visa_select_category.json", "r", encoding="utf-8") as file:
                    xpaths_visa_select_category_dict = json.load(file)
        with open("xpaths_visa_type.json", "r", encoding="utf-8") as file:
            xpaths_visa_type_dict = json.load(file)
        wait = WebDriverWait(driver, 10)
        try:
            while not self.exception:
                for city, visa_data in xpaths_visa_type_dict.items():
                    # click drop-down list select field visa center
                    wait_random_time(fromm=2.6, to=4.5)
                    drop_down_list_field_visa_center = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths_visa_select_category_dict["center_select_field"])))
                    drop_down_list_field_visa_center.click()

                    # select visa center
                    wait_random_time(fromm=0.8, to=1.5)
                    select_visa_center = wait.until(EC.element_to_be_clickable((By.XPATH, visa_data["center_text"])))
                    actions = ActionChains(driver)
                    actions.move_to_element(select_visa_center).perform()
                    select_visa_center.click()

                    # click drop-down list select field visa category
                    wait_random_time(fromm=4.0, to=6.5)
                    drop_down_list_visa_category = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths_visa_select_category_dict["category_select_field"])))
                    drop_down_list_visa_category.click()

                    # select visa catogory
                    wait_random_time(fromm=0.8, to=1.5)
                    select_visa_category = wait.until(EC.element_to_be_clickable((By.XPATH, visa_data["category_text"])))
                    select_visa_category.click()
                    
                    if "subcategory" in visa_data:
                        wait_random_time(fromm=1.0, to=1.5)
                        self.smooth_scroll(driver=driver, height=0, step=randint(4, 8), end=True)
                        # click drop-down list select field visa subcategory
                        wait_random_time(fromm=2.0, to=3.5)
                        drop_down_list_visa_subcategory = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths_visa_select_category_dict["subcategory_select_field"])))
                        drop_down_list_visa_subcategory.click()

                        # select visa subcategory
                        wait_random_time(fromm=0.8, to=1.5)
                        select_visa_subcategory = wait.until(EC.element_to_be_clickable((By.XPATH, visa_data["subcategory_text"])))
                        select_visa_subcategory.click()
                    else:
                        wait_random_time(fromm=1.0, to=1.5)
                        self.smooth_scroll(driver=driver, height=0, step=randint(4, 8), end=True)

                    # enter birth date
                    wait_random_time(fromm=3.0, to=5.0)
                    wait.until(EC.element_to_be_clickable((By.XPATH, xpaths_visa_select_category_dict["birth_date_input_field"])))
                    self.enter_text_data(driver=driver,
                                            xpath=xpaths_visa_select_category_dict["birth_date_input_field"],
                                            text=os.getenv("DATE_BIRTH"))

                    # click drop-down list select field citizenship
                    wait_random_time(fromm=1.0, to=3.0)
                    drop_down_list_citizenship = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths_visa_select_category_dict["citizenship_select_field"])))
                    drop_down_list_citizenship.click()

                    # select citizenship
                    wait_random_time(fromm=1.5, to=2.5)
                    select_citizenship = wait.until(EC.element_to_be_clickable((By.XPATH, xpaths_visa_select_category_dict["citizenship"]["xpath_text"])))
                    actions = ActionChains(driver)
                    actions.move_to_element(select_citizenship).perform()
                    select_citizenship.click()
                    wait_random_time(fromm=1.0, to=1.5)

                    # create screen
                    driver.save_screenshot(os.getenv("PATH_SCREEN_FOLDER"))

                    # check if message abot no entry is displaying
                    try:
                        wait = WebDriverWait(driver, 1)
                        # wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/div/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[6]/div")))
                        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()=' Приносим извинения, в настоящий момент нет доступных слотов для записи. Пожалуйста, попробуйте позже ']")))
                        # send_message(city=city, visa_center=visa_data["center_text"][15:-2], time=get_current_time())
                    except Exception as ex:
                        send_message(city=city, visa_center=visa_data["center_text"][15:-2], time=get_current_time(), entry=True)

                    text_log = f"City: {city} - comlpeted, time: {get_current_time()}"
                    logging(text=text_log)

                    self.smooth_scroll(driver=driver, height=randint(30, 60), step=randint(4, 8), up=True)
                # driver.refresh()
                wait_random_time(fromm=400.0, to=700.0)

        except Exception as ex:
            send_mess_text(path_to_message=os.getenv("TG_MESS_FAIL_SCRIPT"))
            self.exception = True
            with open("debug.txt", "w", encoding="utf-8") as file:
                file.write(str(ex))
            driver.close()
            driver.quit()

    def run_bot(self, driver:object) -> None:
        try:
            self.login_recaptha(driver=driver)
        except Exception as ex:
            self.exception = True
            logging(text=str(ex))
            send_mess_text(path_to_message="tgdata\\messages\\stop_run.txt")
        if self.exception:
            wait_random_time(fromm=1200.0, to=2400)
            self.run_bot(driver=driver)
        else:
            try:
                self.find_entry(driver=driver)
            except Exception as ex:
                driver.refresh()
                wait_random_time(fromm=8.0, to=10.0)
                self.run_bot(driver=driver)


def main():
    sp = ScrapyPage()
    driver = sp.init_driver()
    sp.run_bot(driver=driver)

if __name__ == "__main__":
    main()