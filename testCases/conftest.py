import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup():
    # driver = webdriver.Chrome(executable_path="F:\selemium\chromedriver.exe")

    # s = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=s)

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    return driver

