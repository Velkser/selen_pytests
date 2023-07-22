import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--browser_name', default="chrome")
    parser.addoption('--language', default="en")


@pytest.fixture
def browser(request):
    name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None

    print("\nStarting browser...")
    
    if name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        
    yield browser
    print("\nKill browser...")
    browser.quit()