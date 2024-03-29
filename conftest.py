# Import necessary libraries
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




# Function to configure browser UI
def configure_browser_ui():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Consider adding other options if needed
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

@pytest.fixture(scope='function')
def driver(request):
    driver = configure_browser_ui()
    driver.maximize_window()
    yield driver
    driver.quit()




# Second driver fixture (if needed)
@pytest.fixture(scope='function')
def driver_two(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver






