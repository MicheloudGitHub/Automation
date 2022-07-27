from pytest import fixture
from selenium import webdriver

@fixture
def setup():
    ch_options=webdriver.ChromeOptions()
    driver=webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe',options=ch_options)
    return driver