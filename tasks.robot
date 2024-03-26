*** Settings ***
Library           CustomSelenium
Library           ExtendedSelenium

*** Tasks ***
Using CustomSelenium with Robot Framework Syntax
    Set Webdriver
    Open Url    https://docs.robocorp.com    screenshot=${OUTPUT_DIR}${/}screen.png
    [Teardown]    Driver Quit

Using Extended Selenium Library
    Open Available Browser    https://docs.robocorp.com
    Looking At Element    //a[@href="/docs/courses"]
