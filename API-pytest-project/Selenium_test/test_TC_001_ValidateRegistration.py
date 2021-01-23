import pytest
from selenium.webdriver import Chrome
@pytest.mark.Smoke
def test_registration_valid_data():
    path= "/Selenium_test/chromedriver"
    driver=Chrome(executable_path=path)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.quit()

@pytest.mark.Sanity
def test_registration_invalid1_data():
    global path
    path= "/Users/mdrubel/Downloads/python_workspace/API-pytest-project/Selenium_test/chromedriver"

    driver=Chrome(executable_path=path)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.quit()
@pytest.mark.Smoke
def test_registration_Ivalid2_data():
    driver = Chrome(executable_path=path)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.quit()

@pytest.mark.Sanity
def test_registration_invalid3_data():
    driver=Chrome(executable_path=path)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.quit()