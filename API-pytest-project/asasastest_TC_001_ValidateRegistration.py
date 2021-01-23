import pytest
from selenium.webdriver import Chrome

def test_registration_valid_data():
    path= "/Users/mdrubel/Downloads/python_workspace/API-pytest-project/chromedriver"
    driver=Chrome(executable_path=path)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.quit()
