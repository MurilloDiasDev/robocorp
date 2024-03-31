import logging
import re
import pandas as pd
from RPA.Browser.Selenium import Selenium
import requests

class CustomSelenium:

    def __init__(self):

        self.browser = Selenium()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename='output/task.log', level=logging.INFO)
        self.logger.info('Started')
        self.df = pd.DataFrame(columns=['title', 'date', 'description', 'picture_filename', 'phrases_in_title', 'phrases_in_description', 'contains_money'])
        self.regex = r'\$((\d{1,3}(,\d{3})*)|(\d+ dollars)|(\d+ USD))(\.\d{1,2})?'

    def open_browser(self):
        self.browser.open_available_browser("https://www.google.com")  # Abre um navegador para uso

    def open_url(self, url:str):
        self.browser.go_to(url)

    def get_text(self, xpath:str):
        # text = self.browser.get_text(xpath)
        text = self.browser.get_text(locator=xpath)
        text_lstrip = text.lstrip()
        return str(text_lstrip)

    def get_not_found(self, xpath:str):
        if self.browser.get_element_attribute(xpath, "innerHTML") == 'No Articles Found':
            self.logger.info('No Articles Found')
            return True
        return False

    def get_ads(self, xpath:str):
        try:
            self.browser.get_element_attribute(xpath, "innerHTML")
            self.logger.info("ADS - advertisement found, skipping article")
            return True
        except:
            return False

    def get_image_url(self, xpath:str):
        return self.browser.get_element_attribute(xpath, "src")

    def get_date(self, xpath:str):
        text = self.browser.get_text(xpath)
        text_date_regex = re.search(r"&nbsp;(.*?)\|", text).group(1)
        text_lstrip = text_date_regex.lstrip()
        return str(text_lstrip)

    def rows(self):
        rows = list(range(1,23))
        return rows

    def outputs(self, index:str,  title_text:str, date_str:str, description:str, image_url:str, phrase:str):
        number_phrases_in_title = title_text.count(phrase)
        number_phrases_in_description = description.count(phrase)
        self.logger.info("extracting data - " + str(index) + " - " + date_str + " - " + title_text)
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

    def save_excel(self, index):
        self.df.to_excel('output/output.xlsx', index=False)
        self.logger.info('Finished - total items processed:' + str(index))

    def save_excel_not_found(self):
        dict = {}
        dict['title'] = 'No Articles Found'
        num_rows = len(self.df)
        self.df.loc[num_rows] = dict
        self.df.to_excel('output/output.xlsx', index=False)
        self.logger.info('No Articles Found')

    def dowload_image(self, image_url, index:str):
        self.logger.info("Dowload_image - " + image_url)
        response = requests.get(image_url)
        with open('output/image_' + str(index) + '.jpg', 'wb') as file:
            file.write(response.content)

    def log_error(self, text:str):
        self.page_screenshot()
        self.logger.error(text)

    def page_screenshot(self):
        self.browser.capture_page_screenshot(filename="output/screenshot.jpg")
        self.logger.info("Screenshot captured")
