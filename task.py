
#from ExtendedSelenium import ExtendedSelenium
from CustomSelenium import CustomSelenium
import time
from robocorp import workitems
from datetime import datetime
from datetime import timedelta

def minimal_task():
    selenium = CustomSelenium()
    selenium.set_webdriver()
    maintain = True
    date_now = datetime.now()
    page = 1
    index = 1

    for work_item in workitems.inputs:
        phrase = work_item.payload['phrase']
        months = work_item.payload['months']
        section = work_item.payload['section']


    while maintain == True:

        selenium.open_url("https://nypost.com/search/" + phrase + "/page/" + str(page) + "/?section=" + section)

        page = page + 1
        rows = selenium.rows()
        for row in rows:
            row_str = str(row)

            ads_text = selenium.get_ads('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div/div/p')

            if ads_text == True:
                continue
            index = index + 1

            title_text = selenium.get_text('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div[2]/h3/a')
            date_str = selenium.get_date('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div[2]/span')
            description = selenium.get_text('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div[2]/p')
            image_url = selenium.get_image_url('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div[1]/a/img')

            date_datetime = datetime.strptime(date_str, "%B %d, %Y ")
            delta_date = date_now - date_datetime

            months_int = int(months)

            filter_months = months_int * 31
            if delta_date.days < filter_months:
                pass
            else:
                print('FINISH')
                maintain = False
                break
                
            print(index," - ",date_datetime," - ", title_text)

            



    # for work_item in workitems.inputs:
    #     phrase = work_item.payload['phrase']
        
    # selenium.page_screenshot()
        
    # with open('output/log.txt', 'w', encoding='utf8') as file:
    #     file.write(text)
        
    #time.sleep(2.0)

if __name__ == "__main__":
    minimal_task()
