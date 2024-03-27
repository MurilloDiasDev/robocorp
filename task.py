
#from ExtendedSelenium import ExtendedSelenium
from CustomSelenium import CustomSelenium
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from robocorp import workitems

def minimal_task():
    selenium = CustomSelenium()
    selenium.set_webdriver()

    for work_item in workitems.inputs:
        phrase = work_item.payload['phrase']

        print(phrase)
        print(phrase)
        print(phrase)
        print(phrase)
        print(phrase)
        time.sleep(2.0)

        selenium.open_url("https://nypost.com/search/dollar/")
        
        rows = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
        #rows = [1,2,3,4,5,6,7,8]

        for row in rows:
            row_str = str(row)

            try:
                ads_text = selenium.get_ads('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div/div/p')

                if ads_text == True:
                    continue

                title_text = selenium.get_text('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div[2]/h3/a')
                date = selenium.get_date('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div[2]/span')
                description = selenium.get_text('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div[2]/p')
                image_url = selenium.get_image_url('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div[1]/a/img')

                print("=========================================================================")
                print(date, title_text)
                print(description)
                print(image_url)

            except:
                print('error')


    #selenium.page_screenshot()
    # with open('output/log.txt', 'w', encoding='utf8') as file:
    #     file.write(text)
    #time.sleep(2.0)

if __name__ == "__main__":
    minimal_task()
