import time
from locators.locators_english_language import PageLocators
from base.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class EnglishLanding(BasePage):
    locators = PageLocators()

    def verify_elements_on_homepage(self):
        text = self.element_is_visible(self.locators.MAIN_TEXT)
        expected = "#1 Language Learning Website and App for Kids"
        assert text.text == expected

        text_two = self.element_is_visible(self.locators.BEST_METHODS_TO_EACH_CHILDREN)
        expected_two = "Best 10 methods to teach children a second language"
        assert text_two.text == expected_two

        try:
            image_element = self.element_is_visible(self.locators.HOMEPAGE_IMAGE)
            if image_element.is_displayed():
                print("Image is presented on the website.")
            else:
                print("Image is not displayed on the website.")
        except NoSuchElementException:
            print("Image element not found on the website.")


    def how_it_works_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HOW_IT_WORKS).click()
        text = self.element_is_visible(self.locators.HOW_IT_WORKS_TITLE)
        expected_title = "How it works"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PROGRESS_REPORTS)
        expected_message = "Each child account includes several progress reports such as time, activity, test and daily report."
        assert text_two.text == expected_message
        text_combination = self.element_is_visible(self.locators.RECENT_COMBINATION)
        expected_message_two = "Recent studies have shown that children prefer to watch animations over real-life footage. Designed to capture your child’s attention, 80% of DinoLingo videos are presented as either 3D or 2D animations."
        assert text_combination.text == expected_message_two
        print("How it works page works good")

    def customer_reviews_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS).click()
        text = self.element_is_visible(self.locators.CUSTOMER_REVIEWS_TITLE)
        expected_title = "Customer Reviews"
        assert text.text == expected_title
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK).click()
        time.sleep(2)
        if self.driver.get_window_rect()['width'] == self.driver.execute_script('return window.screen.width') and \
                self.driver.get_window_rect()['height'] == self.driver.execute_script('return window.screen.height'):
            print("Video is in full screen mode.")
        else:
            print("Video is not in full screen mode.")



