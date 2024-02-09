from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from locators.locators_english_language import PageLocators
import re
from selenium.common.exceptions import TimeoutException

class BasePage:
    # Initialize page locators
    locators = PageLocators()

    def __init__(self, driver, url):
        # Constructor to initialize the browser driver and URL
        self.driver = driver
        self.url = url

    def open(self):
        # Open the URL in the browser
        self.driver.get(self.url)

    # Wait until an element is visible and return it
    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # Wait until multiple elements are visible and return them
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    # Wait until an element is present in the DOM
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # Wait until multiple elements are present in the DOM
    def element_are_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    # Wait until an element is no longer visible
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    # Wait until an element is clickable and return it
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    # Scroll the browser to a specific element
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Retrieve a specific attribute from an element
    def get_attribute_element(self, element):
        return element.get_attribute(element)

    # Decorator to handle the stale element exception
    def retry_stale_element(func, max_retries=3):
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except StaleElementReferenceException:
                    continue
            raise

        return wrapper

    # Click on an element specified by the locator
    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    # Click on a random location on the page
    def random_click(self):
        actions = ActionChains(self.driver)
        actions.move_by_offset(500, 500)
        actions.click()
        actions.perform()

    def click_for_language(self):
        actions = ActionChains(self.driver)
        actions.move_by_offset(250, 250)
        actions.click()
        actions.perform()

    # Navigate back in the browser
    def back(self):
        self.driver.back()

    def execute_script_d(self, slider, new_value):
        self.driver.execute_script("arguments[0].setAttribute('aria-valuetext', arguments[1]);", slider, new_value)

    def execute_script(self, new_value):
        self.driver.execute_script("arguments[0].click();", new_value)

    def for_game(self, element):
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('click'));", element)

    def slider_move(self, locator, x_offset, y_offset):
        slider = self.driver.find_element(*locator)
        action = ActionChains(self.driver)
        action.click_and_hold(slider).move_by_offset(x_offset, y_offset).release().perform()


    def scroll_down(self):
        # Scroll the web page down by a specified number of pixels
        pixels_to_scroll = 6000
        self.driver.execute_script(f'window.scrollBy(0,{pixels_to_scroll});')

    def scroll_up(self):
        # Scroll the web page up by a specified number of pixels
        pixels_to_scroll = -500
        self.driver.execute_script(f"window.scrollBy(0,{pixels_to_scroll});")

    def get_initial_scroll_position(self):
        # Get the current vertical scroll position of the web page
        return self.driver.execute_script("return window.scrollY")