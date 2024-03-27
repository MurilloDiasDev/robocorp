
#from ExtendedSelenium import ExtendedSelenium
from CustomSelenium import CustomSelenium
import time



def minimal_task():
    selenium = CustomSelenium()
    selenium.set_webdriver()
    #selenium.open_url("https://github.com/robocorp/rpaframework", "github.png")
    selenium.open_url("https://www.latimes.com/")
    time.sleep(2.0)
    selenium.driver.save_screenshot('Screenshot.png')




    print("Done.")


if __name__ == "__main__":
    minimal_task()
