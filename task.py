
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
    
    #selenium.open_url("https://github.com/robocorp/rpaframework", "github.png")
    selenium.open_url("https://www.latimes.com/")
    time.sleep(2.0)
    selenium.driver.save_screenshot('output/Screenshot.png')
    wait_fast = WebDriverWait(selenium.driver, 10)
    text = wait_fast.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/main/div[2]/div/div[1]/ul[1]/li/ps-promo/div/div[2]/p'))).get_attribute('innerHTML')
    
    try:
        workitems.Outputs.create(payload=text)
    except:
        print('error in create')

    try:
        workitems.Output.add_file(path="Screenshot.png", name="screen")
    except:
        print('error in create')
    

    print(str(text))

    try:
        with open('output/log.txt', 'w', encoding='utf8') as file:
            file.write(text)
    except:
        pass

    print("Done.")


if __name__ == "__main__":
    minimal_task()
