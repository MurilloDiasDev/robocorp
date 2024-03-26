
#from ExtendedSelenium import ExtendedSelenium
from CustomSelenium import CustomSelenium



def minimal_task():
    selenium = CustomSelenium()
    selenium.set_webdriver()
    #selenium.open_url("https://github.com/robocorp/rpaframework", "github.png")
    selenium.open_url("https://www.latimes.com/")
    print("Done.")


if __name__ == "__main__":
    minimal_task()
