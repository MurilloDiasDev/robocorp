from CustomSelenium import CustomSelenium
from robocorp import workitems
from datetime import datetime
from datetime import timedelta

def minimal_task():

    selenium = CustomSelenium()
    selenium.open_browser()
    date_now = datetime.now()
    maintain = True
    not_found = False
    page = 1
    index = 1

    try:

        for work_item in workitems.inputs:

            phrase = work_item.payload['phrase']
            months = work_item.payload['months']
            section = work_item.payload['section']

        months_int = int(months)

        while maintain == True:

            try:
                selenium.open_url("https://nypost.com/search/" + phrase.replace(" ", "+") + "/page/" + str(page) + "/?section=" + section.replace(" ", "-"))

            except:
                selenium.log_error('browser was unable to open the page')

            page = page + 1
            rows = selenium.rows()

            for row in rows:

                row_str = str(row)
                not_found = selenium.get_not_found('//*[@id="search-results"]/div/div[3]/h2')

                ads_text = selenium.get_ads('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div/div/p')

                if not_found == True:

                    maintain = False
                    selenium.save_excel_not_found()
                    break

                if ads_text == True:
                    continue

                try:

                    title_text = selenium.get_text('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div[2]/h3/a')
                    date_str = selenium.get_date('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div[2]/span')
                    description = selenium.get_text('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div[2]/p')
                    image_url = selenium.get_image_url('//*[@id="search-results"]/div/div[3]/div[' + row_str + ']/div/div[1]/a/img')

                except:
                    selenium.log_error('was unable to extract news data')

                selenium.outputs(index, title_text, date_str, description, image_url, phrase)

                index = index + 1
                date_datetime = datetime.strptime(date_str, "%B %d, %Y")
                delta_date = date_now - date_datetime
                
                if months_int == 0:
                    months_int = 1

                else:
                    pass

                filter_months = months_int * 31

                if delta_date.days < filter_months:
                    pass

                else:
                    maintain = False
                    selenium.save_excel(index)
                    break

    except:
        selenium.log_error("missing work items")

if __name__ == "__main__":
    minimal_task()
