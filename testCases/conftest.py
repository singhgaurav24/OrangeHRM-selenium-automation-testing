import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup():
    # driver = webdriver.Chrome(executable_path="F:\selemium\chromedriver.exe")
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    return driver

