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
        text = self.element_is_visible(self.locators.CUSTOMER_REVIEWS_TITLE_EN)
        expected_title = "Customer Reviews"
        assert text.text == expected_title
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK).click()
        time.sleep(2)
        if self.driver.get_window_rect()['width'] == self.driver.execute_script('return window.screen.width') and \
                self.driver.get_window_rect()['height'] == self.driver.execute_script('return window.screen.height'):
            print("Video is in full screen mode.")
        else:
            print("Video is not in full screen mode.")

    def language_courses_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.LANGUAGE_COURSES).click()
        text = self.element_is_visible(self.locators.LANGUAGE_COURSES_TITLE_EN)
        expected_title = "50 languages & 30,000+ online learning activities"
        assert text.text == expected_title
        self.scroll_down()
        time.sleep(3)
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_EN)
        expected_title_three = "Please rate this page"
        assert text_three.text == expected_title_three


    def curriculum_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CURRICULUM).click()
        text = self.element_is_visible(self.locators.CURRICULUM_HEADER_TEXT_EN)
        expected_title = "Dinolingo Lesson Plan & Curriculum"
        assert text.text == expected_title
        self.back()
        self.scroll_down()
        time.sleep(3)
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_EN)
        expected_title_three = "Please rate this page"
        assert text_three.text == expected_title_three


    def parents_guide_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.PARENTS_GUIDE).click()
        text = self.element_is_visible(self.locators.PARENTS_GUIDE_TITLE_EN)
        expected_title = "Tips for parents"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PARENTS_GUIDE_TEXT_EN)
        expected_text = "Consistency is the key. It is important to remember to login and practice once a day."
        assert text_two.text == expected_text
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.PARENTS_GUIDE_OTHER_QUESTIONS_EN).click()
        time.sleep(2)
        text_three = self.element_is_visible(self.locators.PARENTS_GUIDE_OTHER_QUESTIONS_ANSWER_EN)
        expected_text_three = "There is convincing evidence, which suggests that children who learn a second language at an early age have a greater chance of succeeding with reading, vocabulary, and writing, throughout their academic and professional career. In addition, such children are more likely to develop healthier critical thinking and social skills, both significant advantages in life. Studies also show, bilingual students, including adult students, often achieve higher scores on standardized tests and college entrance exams. According to the 'American Council on the Teaching of Foreign Languages', ACTFL, learning a second language has a greater advantage for children both in the near and distant future, enabling them to easily interact with multinationals. This will be a definite competitive edge in the global business arena later in life. Please feel free to check out our blog for additional scientific resources on this topic."
        assert text_three.text == expected_text_three

    def schools_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.SCHOOLS).click()
        text = self.element_is_visible(self.locators.SCHOOLS_TITLE_EN)
        expected_title = "Dinolingo for Schools"
        assert text.text == expected_title
        self.element_is_visible(self.locators.SCHOOLS_GET_A_QUOTE_EN).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.SCHOOLS_QUOTE_FORMULARIO_EN)
            expected_text = "School Quote 01"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])
        else:
            print("The School Quote window not open")
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.SCHOOLS_QUOTE_SCHOOLS_TEXT_EN)
        expected_text_three = "We work with public schools, charter schools, language schools, private schools, language tutors, governments, and institutions."
        assert text_three.text == expected_text_three
        image = self.element_is_visible(self.locators.SCHOOLS_IMAGE_EN)
        assert image.is_displayed(), "Image is not displayed on the page"

