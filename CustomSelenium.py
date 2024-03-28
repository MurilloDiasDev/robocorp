
import logging
import re
import selenium
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CustomSelenium:

    def __init__(self):
        self.driver = None
        self.logger = logging.getLogger(__name__)
        self.df = pd.DataFrame(columns=['title', 'date', 'description', 'picture_filename', 'phrases_in_title', 'phrases_in_description', 'contains_money'])
        self.regex = r'\$((\d{1,3}(,\d{3})*)|(\d+ dollars)|(\d+ USD))(\.\d{1,2})?'

    def set_chrome_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('--disable-dev-shm-usage')
        #options.add_argument("--incognito")
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument('log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        return options

    def set_webdriver(self):
        options = self.set_chrome_options()
        self.driver = webdriver.Chrome(options=options, service=Service('./chromedriver'))
        # self.driver = webdriver.Chrome(options=options, service=Service(r'C:\Users\muril\OneDrive\Área de Trabalho\Desafio\new\chromedriver.exe'))
        
    def open_url(self, url:str):
        self.driver.get(url)

    def driver_quit(self):
        if self.driver:
            self.driver.quit()

    def page_screenshot(self):
        self.driver.save_screenshot('output/Screenshot.png')

    def get_text(self, xpath:str):
        wait_fast = WebDriverWait(self.driver, 10)
        text = wait_fast.until(EC.presence_of_element_located((By.XPATH, xpath))).get_attribute('innerHTML')
        text_lstrip = text.lstrip()
        return str(text_lstrip)
    
    def get_ads(self, xpath:str):
        wait_fast = WebDriverWait(self.driver, 0.05)
        try:
            text = wait_fast.until(EC.presence_of_element_located((By.XPATH, xpath))).get_attribute('innerHTML')
            return True
        except:
            return False
    
    def get_image_url(self, xpath:str):
        wait_fast = WebDriverWait(self.driver, 10)
        text = wait_fast.until(EC.presence_of_element_located((By.XPATH, xpath))).get_attribute('src')
        return str(text)
    
    def get_date(self, xpath:str):
        wait_fast = WebDriverWait(self.driver, 10)
        text = wait_fast.until(EC.presence_of_element_located((By.XPATH, xpath))).get_attribute('innerHTML')
        text_date_regex = re.search(r"&nbsp;(.*?)\|", text).group(1)
        text_lstrip = text_date_regex.lstrip()
        return str(text_lstrip)
    
    def rows(self):
        rows = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
        return rows
    
    def outputs(self, index:str,  title_text:str, date_str:str, description:str, image_url:str, phrase:str):

        number_phrases_in_title = title_text.count(phrase)
        number_phrases_in_description = description.count(phrase)
        self.dowload_image(image_url, index)

        title_and_description = title_text + description

        if re.search(self.regex, title_and_description):
            contains_money = True
        else:
            contains_money = False

        dict = {}
        dict['title'] = title_text
        dict['date'] = date_str
        dict['description'] = description
        dict['picture_filename'] = 'image_' + str(index) + '.jpg'
        dict['phrases_in_title'] = number_phrases_in_title
        dict['phrases_in_description'] = number_phrases_in_description
        dict['contains_money'] = str(contains_money)
        num_rows = len(self.df)
        self.df.loc[num_rows] = dict
        print(index, " - ", date_str, " - ", title_text)
        
    def save_excel(self):
        self.df.to_excel('output/output.xlsx', index=False)

    def dowload_image(self, image_url, index:str):

        response = requests.get(image_url)
        with open('output/image_' + str(index) + '.jpg', 'wb') as file:
            file.write(response.content)

        

