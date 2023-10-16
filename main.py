import os, json
from time import sleep

from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from dotenv import load_dotenv

from utils import wait_random_time


class ScrapyPage:
    ''' class for scrapy page '''
    def __init__(self) -> None:
        pass

    def enter_text_data(self, driver, xpath:str, text:str) -> None:
        ''' method for enter text data to input field '''
        element = driver.find_element(By.XPATH, xpath)
        element.send_keys(Keys.CONTROL, "a")
        wait_random_time(fromm=0.11, to=0.45)
        for letter in text:
            element.send_keys(letter)
            wait_random_time(fromm=0.11, to=0.45)

    def check_displayed_element(self, driver, xpath:str) -> bool:
        ''' this method is cchecking if element displayed '''
        try:
            element = driver.find_element(By.XPATH, xpath).is_displayed()
            return True
        except:
            return False

    def find_entry(self):
        ''' main func for scrapy page of visa '''
        ua = UserAgent()
        random_ua = ua.random
        print("random_ua: ", random_ua)

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

        # select language
        # wait_random_time(fromm=0.76, to=2.87)
        # language_drop_down_list = driver.find_element(By.XPATH, '//*[@id="dropdownMenuButton"]')
        # language_drop_down_list.click()

        # wait_random_time(fromm=0.29, to=2.36)
        # select_russian_language = driver.find_element(By.XPATH, '/html/body/app-root/div/header/div/div/div/div/a[2]')
        # select_russian_language.click()

        # enter login
        wait_random_time(fromm=1.61, to=3.02)
        self.enter_text_data(self, driver=driver, xpath='//*[@id="mat-input-0"]', text=os.getenv("LOGIN"))

        # enter password
        wait_random_time(fromm=1.23, to=3.34)
        self.enter_text_data(self, driver=driver, xpath='//*[@id="mat-input-1"]', text=os.getenv("PASSWORD"))

        # solve captha
        wait_random_time(fromm=1.36, to=2.36)
        recaptcha_iframe = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
        wait_random_time(fromm=3.89, to=5.12)
        solver.click_recaptcha_v2(iframe=recaptcha_iframe)

        # TODO: check
        # click button login
        wait_random_time(fromm=2.01, to=3.34)
        button_login = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button')
        button_login.click()

        # click button find entry
        wait_random_time(fromm=5.89, to=8.12)
        button_find_entry = driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-dashboard/section[1]/div/div[2]/div/button')
        button_find_entry.click()
        
        with open("xpaths_visa_select_category.json", "r", encoding="utf-8") as file:
                xpaths_visa_select_category_dict = json.load(file)
        
        with open("xpaths_visa_type.json", "r", encoding="utf-8") as file:
            xpaths_visa_type_dict = json.load(file)
        
        for city, visa_data in xpaths_visa_type_dict.items():

            # click drop-down list select field visa center
            wait_random_time(fromm=0.5, to=1.5)
            drop_down_list_field_visa_center = driver.find_element(By.XPATH, xpaths_visa_select_category_dict["center_select_field"])
            drop_down_list_field_visa_center.click()

            # select visa center
            wait_random_time(fromm=0.5, to=1.5)
            select_visa_center = driver.find_element(By.XPATH, visa_data["center_text"])
            select_visa_center.click()

            # click drop-down list select field visa category
            wait_random_time(fromm=4.0, to=6.5)
            drop_down_list_visa_category = driver.find_element(By.XPATH, xpaths_visa_select_category_dict["category_select_field"])
            drop_down_list_visa_category.click()

            # select visa catogory
            wait_random_time(fromm=0.5, to=1.5)
            select_visa_category = driver.find_element(By.XPATH, visa_data["category_text"])
            select_visa_category.click()

            
            if "subcategory" in visa_data:
                # click drop-down list select field visa subcategory
                wait_random_time(fromm=4.0, to=6.5)
                drop_down_list_visa_subcategory = driver.find_element(By.XPATH, xpaths_visa_select_category_dict["subcategory_select_field"])
                drop_down_list_visa_subcategory.click()

                # select visa subcategory
                wait_random_time(fromm=3.0, to=5.0)
                select_visa_subcategory = driver.find_element(By.XPATH, visa_data["subcategory_text"])
                select_visa_subcategory.click()

            # enter birth date
            wait_random_time(fromm=3.0, to=5.0)
            self.enter_text_data(self,
                                 driver=driver,
                                 xpath=xpaths_visa_select_category_dict["birth_date_input_field"],
                                 text=os.getenv("DATE_BIRTH"))

            # click drop-down list select field citizenship
            wait_random_time(fromm=0.5, to=1.5)
            drop_down_list_citizenship = driver.find_element(By.XPATH, xpaths_visa_select_category_dict["citizenship_select_field"])
            drop_down_list_citizenship.click()

            # select citizenship
            wait_random_time(fromm=1.5, to=2.5)
            select_citizenship = driver.find_element(By.XPATH, xpaths_visa_select_category_dict["citizenship"]["xpath_text"])
            select_citizenship.click()

            wait_random_time(fromm=20.5, to=30.7)

        # TODO: screen
        # TODO: shedule run
        # TODO: check if element is displayed before every click
        # TODO: check wait time
        # TODO: read security site
        # TODO: scroll down
        # TODO: stealth technologies


def main():
    pass

if __name__ == "__main__":
    main()