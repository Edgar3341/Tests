import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_english_language import PageLocators
from base.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class EnglishLanding(BasePage):
    locators = PageLocators()

    def verify_elements_on_homepage(self):
        text = self.element_is_visible(self.locators.MAIN_TEXT)
        expected = "#1 Language Learning Website and App for Kids"
        assert text.text == expected

        text_two = self.element_is_visible(self.locators.BEST_METHODS_TO_EACH_CHILDREN_EN)
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
        text_two = self.element_is_visible(self.locators.PROGRESS_REPORTS_EN)
        expected_message = "Each child account includes several progress reports such as time, activity, test and daily report."
        assert text_two.text == expected_message
        text_combination = self.element_is_visible(self.locators.RECENT_COMBINATION_ES)
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
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_EN).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_EN).click()
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
            expected_text = "School Quote"
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

    def homeschoolers_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HOMESCHOOLES).click()
        text = self.element_is_visible(self.locators.HOMESCHOOLERS_TITLE_EN)
        expected_title = "Homeschoolers"
        assert text.text == expected_title
        try:
            image_element = self.element_is_visible(self.locators.HOMESCHOOLERS_IMAGE)
            image_source = image_element.get_attribute("src")
            expected_image_source = "assets/dinosaurs/flyingDino.svg"
            assert image_source == expected_image_source, "Image is not persisting"
            print("Image is persisting")
        except Exception as e:
            print(f"Error: {e}")


    def privacy_verify_redirect(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.PRIVACY_EN).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Dinolingo Privacy Policy"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def terms_verify_redirect(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.TERMS_EN).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Terms & Conditions"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def contact_us_verify_redirect(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CONTACT_US_EN).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def about_us_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.ABOUT_US).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "about Dinolingo"
        assert text.text == expected_title

    def help_and_support_verify_redirect(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HELP_AND_SUPPORT_EN).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def spanish_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.SPANISH_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Spanish for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def french_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.FRENCH_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn French for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def english_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.ENGLISH_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn English for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def italian_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.ITALIAN_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Italian for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def german_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.GERMAN_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn German for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def japanese_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.JAPANESE_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Japanese for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def portuguese_eu_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.PORTUGUESE_EU_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn European Portuguese for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def portuguese_br_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.PORTUGUESE_BR_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Portuguese for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def russian_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.RUSSIAN_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Russian for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def chinese_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CHINESE_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Chinese for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def greek_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.GREEK_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Greek for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def swedish_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.SWEDISH_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Swedish for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def dutch_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.DUTCH_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Dutch for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def polish_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.POLISH_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Polish for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def arabic_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.ARABIC_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Arabic for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hebrew_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HEBREW_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Hebrew for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def ukrainian_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.UKRAINIAN_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Ukrainian for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def latin_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.LATIN_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Latin for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def korean_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.KOREAN_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Korean for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hindi_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HINDI_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Hindi for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def persian_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.PERSIAN_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Persian for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def croatian_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CROATIAN_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Croatian for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def turkish_for_kids_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.TURKISH_FOR_KIDS).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "Learn Turkish for Kids"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def all_languages_verify_elements(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.SEE_ALL_50_LANGUAGES).click()
        text = self.element_is_visible(self.locators.LANGUAGE_HEADERS_EN)
        expected_title = "50 languages & 30,000+ online learning activities"
        assert text.text == expected_title


class SpanishLanding(BasePage):
    locators = PageLocators()


    def verify_elements_on_homepage_es(self):
        text = self.element_is_visible(self.locators.MAIN_TEXT)
        expected = "Sitio Web y Aplicación #1 de Aprendizaje de Idiomas para Niños"
        assert text.text == expected

        text_two = self.element_is_visible(self.locators.BEST_METHODS_TO_EACH_CHILDREN_ES)
        expected_two = "Los mejores 10 métodos para enseñar un segundo idioma a niños"
        assert text_two.text == expected_two
        try:
            image_element = self.element_is_visible(self.locators.HOMEPAGE_IMAGE)
            if image_element.is_displayed():
                print("Image is presented on the website.")
            else:
                print("Image is not displayed on the website.")
        except NoSuchElementException:
            print("Image element not found on the website.")


    def how_it_works_verify_element_es(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HOW_IT_WORKS).click()
        self.element_is_visible(self.locators.HOMEPAGE_LANGUAGE).click()
        self.element_is_visible(self.locators.HOMEPAGE_LANGUAGE_SPANISH).click()
        text = self.element_is_visible(self.locators.HOW_IT_WORKS_TITLE)
        expected_title = "Cómo funciona"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PROGRESS_REPORTS_ES)
        expected_message = "Cada cuenta de niño incluye varios reportes de progreso como tiempo, actividad, evaluación y reporte diario."
        assert text_two.text == expected_message
        text_combination = self.element_is_visible(self.locators.DEVICES_ES)
        expected_message_two = "Dispositivos"
        assert text_combination.text == expected_message_two
        print("How it works page works good")


   #  ---------

    def customer_reviews_verify_elements_es(self):
        text = self.element_is_visible(self.locators.CUSTOMER_REVIEWS_TITLE)
        print(text.text)
        expected_title = "Opiniones de Clientes"
        assert text.text == expected_title
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_ES).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_ES).click()
        time.sleep(2)
        if self.driver.get_window_rect()['width'] == self.driver.execute_script('return window.screen.width') and \
                self.driver.get_window_rect()['height'] == self.driver.execute_script('return window.screen.height'):
            print("Video is in full screen mode.")
        else:
            print("Video is not in full screen mode.")

    def language_courses_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "50 idiomas y más de 30,000 actividades en línea"
        assert text.text == expected_title
        self.scroll_down()
        time.sleep(3)
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_ES)
        expected_title_three = "Por favor califique esta página"
        assert text_three.text == expected_title_three
        print("The webpage working as expected")



    def curriculum_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Programa de Estudio"
        assert text.text == expected_title
        self.element_is_visible(self.locators.CURRICULUM__ACCOUNT_EN).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Cree Su Cuenta Gratuita"
        assert text_two.text == expected_title_two
        self.back()
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_ES)
        expected_title_three = "Por favor califique esta página"
        assert text_three.text == expected_title_three
        print("Redirecting to create account works as expected")


    def parents_guide_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Consejos para padres"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PARENTS_GUIDE_TEXT_ES)
        expected_text = "La consistencia es la clave. Es importante recordar iniciar sesión y practicar una vez al día."
        assert text_two.text == expected_text
        self.element_is_visible(self.locators.TRY_IT_FOR_FREE_ES).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Cree Su Cuenta Gratuita"
        assert text_two.text == expected_title_two
        print("The parents guide website working as expected. Try it for free redirects to the account creation")


    def schools_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Dinolingo para Escuelas"
        assert text.text == expected_title
        self.element_is_visible(self.locators.SCHOOLS_GET_A_QUOTE_EN).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.SCHOOLS_QUOTE_FORMULARIO_EN)
            expected_text = "School Quote"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])
        else:
            print("The School Quote window not open")
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.SCHOOLS_QUOTE_SCHOOLS_TEXT_ES)
        expected_text_three = "Trabajamos con escuelas públicas, escuelas subvencionadas, escuelas privadas, tutores de idiomas, gobiernos e instituciones."
        assert text_three.text == expected_text_three
        image = self.element_is_visible(self.locators.SCHOOLS_IMAGE_EN)
        assert image.is_displayed(), "Image is not displayed on the page"
        print("Schools page working as expected. Users can open Schools Quote ")

    def homeschoolers_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Educación en el Hogar"
        assert text.text == expected_title
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_ES)
        expected_title_three = "Por favor califique esta página"
        assert text_three.text == expected_title_three
        print("The webpage working as expected")


    def privacy_verify_redirect_es(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.PRIVACY_ES).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Dinolingo Privacy Policy"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def terms_verify_redirect_es(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.TERMS_ES).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Terms & Conditions"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def contact_us_verify_redirect_es(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CONTACT_US_ES).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def about_us_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Acerca de Dinolingo"
        assert text.text == expected_title
        self.element_is_visible(self.locators.ABOUT_US_CREATE_ACCOUNT_ES).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Cree Su Cuenta Gratuita"
        assert text_two.text == expected_title_two
        self.back()
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_ES)
        expected_title_three = "Por favor califique esta página"
        assert text_three.text == expected_title_three
        print("Redirecting to create account works as expected")


    def help_and_support_verify_redirect_es(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HELP_AND_SUPPORT_ES).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def spanish_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Español para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def french_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Francés para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def english_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Inglés para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def italian_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Italiano para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def german_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Alemán para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def japanese_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Japonés para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def portuguese_eu_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Portugués para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def russian_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Ruso para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def chinese_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Chino para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def greek_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Griego para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def swedish_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Sueco para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def dutch_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Holandés para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def polish_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Polaco para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def arabic_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Árabe para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hebrew_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Hebreo para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def ukrainian_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Ucraniano para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def latin_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Latín para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def korean_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Coreano para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hindi_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Hindi para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def persian_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Persa para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def croatian_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Croata para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def turkish_for_kids_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizaje Turco para Niños"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def all_languages_verify_elements_es(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "50 idiomas y más de 30,000 actividades en línea"
        assert text.text == expected_title



class ItalianLanding(BasePage):
    locators = PageLocators()


    def verify_elements_on_homepage_it(self):
        text = self.element_is_visible(self.locators.MAIN_TEXT)
        expected = "1° sito web e app di apprendimento delle lingue per bambini"
        assert text.text == expected

        text_two = self.element_is_visible(self.locators.BEST_METHODS_TO_EACH_CHILDREN_IT)
        expected_two = "I 10 migliori metodi per insegnare una seconda lingua ai bambini"
        assert text_two.text == expected_two
        try:
            image_element = self.element_is_visible(self.locators.HOMEPAGE_IMAGE)
            if image_element.is_displayed():
                print("Image is presented on the website.")
            else:
                print("Image is not displayed on the website.")
        except NoSuchElementException:
            print("Image element not found on the website.")


    def how_it_works_verify_element_it(self):
        text = self.element_is_visible(self.locators.HOW_IT_WORKS_TITLE)
        expected_title = "Come funziona"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PROGRESS_REPORTS_iT)
        expected_message = "Ogni account per bambini include diverse relazioni sui progressi, come i report su tempo, attività, test e i report giornalieri."
        assert text_two.text == expected_message
        text_combination = self.element_is_visible(self.locators.DEVICES_IT)
        expected_message_two = "Dispositivi"
        assert text_combination.text == expected_message_two
        print("How it works page works good")


   #  ---------

    def customer_reviews_verify_elements_it(self):
        text = self.element_is_visible(self.locators.CUSTOMER_REVIEWS_TITLE)
        print(text.text)
        expected_title = "Recensioni dei clienti"
        assert text.text == expected_title
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_ES).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_ES).click()
        time.sleep(2)
        if self.driver.get_window_rect()['width'] == self.driver.execute_script('return window.screen.width') and \
                self.driver.get_window_rect()['height'] == self.driver.execute_script('return window.screen.height'):
            print("Video is in full screen mode.")
        else:
            print("Video is not in full screen mode.")

    def language_courses_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "50 lingue e più di 30.000 attività didattiche online"
        assert text.text == expected_title
        self.scroll_down()
        time.sleep(3)
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_IT)
        expected_title_three = "Valuta questa pagina"
        assert text_three.text == expected_title_three
        print("The webpage working as expected")



    def curriculum_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Curriculum"
        assert text.text == expected_title
        self.element_is_visible(self.locators.CURRICULUM__ACCOUNT_EN).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Crea il tuo account gratuito"
        assert text_two.text == expected_title_two
        self.back()
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_IT)
        expected_title_three = "Valuta questa pagina"
        assert text_three.text == expected_title_three
        print("Redirecting to create account works as expected")


    def parents_guide_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Consigli per i genitori"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PARENTS_GUIDE_TEXT_IT)
        expected_text = "La costanza è fondamentale. È importante ricordarsi di accedere ed esercitarsi una volta al giorno."
        assert text_two.text == expected_text
        self.element_is_visible(self.locators.TRY_IT_FOR_FREE_ES).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Crea il tuo account gratuito"
        assert text_two.text == expected_title_two
        print("The parents guide website working as expected. Try it for free redirects to the account creation")


    def schools_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Dinolingo per le scuole"
        assert text.text == expected_title
        self.element_is_visible(self.locators.SCHOOLS_GET_A_QUOTE_EN).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.SCHOOLS_QUOTE_FORMULARIO_EN)
            expected_text = "School Quote"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])
        else:
            print("The School Quote window not open")
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.SCHOOLS_QUOTE_SCHOOLS_TEXT_IT)
        expected_text_three = "Lavoriamo con scuole pubbliche, charter school, scuole di lingue, scuole private, tutor di lingue, governi e istituzioni."
        assert text_three.text == expected_text_three
        image = self.element_is_visible(self.locators.SCHOOLS_IMAGE_EN)
        assert image.is_displayed(), "Image is not displayed on the page"
        print("Schools page working as expected. Users can open Schools Quote ")

    def homeschoolers_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Studenti da casa"
        assert text.text == expected_title
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_IT)
        expected_title_three = "Valuta questa pagina"
        assert text_three.text == expected_title_three

        print("The webpage working as expected")


    def privacy_verify_redirect_it(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.PRIVACY_EN).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Dinolingo Privacy Policy"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def terms_verify_redirect_it(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.TERMS_IT).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Terms & Conditions"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def contact_us_verify_redirect_it(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CONTACT_US_IT).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def about_us_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Informazioni su Dinolingo"
        assert text.text == expected_title
        self.element_is_visible(self.locators.ABOUT_US_CREATE_ACCOUNT_ES).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Crea il tuo account gratuito"
        print(text_two.text)
        assert text_two.text == expected_title_two
        self.back()
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_IT)
        expected_title_three = "Valuta questa pagina"
        assert text_three.text == expected_title_three
        print("Redirecting to create account works as expected")


    def help_and_support_verify_redirect_it(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HELP_AND_SUPPORT_IT).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def spanish_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del spagnolo per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def french_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del francese per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def english_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del inglese per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def italian_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del italiano per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def german_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del tedesco per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def japanese_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del giapponese per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def portuguese_eu_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del portoghese eu per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def russian_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del russo per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def chinese_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del cinese per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def greek_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del greco per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def swedish_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del svedese per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def dutch_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del olandese per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def polish_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del polacco per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def arabic_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del arabo per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hebrew_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del ebraico per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def ukrainian_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del ucraino per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def latin_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del latino per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def korean_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del coreano per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hindi_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del hindi per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def persian_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del persiano per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def croatian_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del croato per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def turkish_for_kids_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendimento del turco per bambini"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def all_languages_verify_elements_it(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "50 lingue e più di 30.000 attività didattiche online"
        assert text.text == expected_title


class FrenchLanding(BasePage):
    locators = PageLocators()


    def verify_elements_on_homepage_fr(self):
        text = self.element_is_visible(self.locators.MAIN_TEXT)
        expected = "Site web et application d'apprentissage de langue N°1 pour les enfants"
        assert text.text == expected

        text_two = self.element_is_visible(self.locators.BEST_METHODS_TO_EACH_CHILDREN_FR)
        expected_two = "Les 10 meilleures méthodes pour enseigner une seconde langue aux enfants"
        assert text_two.text == expected_two
        try:
            image_element = self.element_is_visible(self.locators.HOMEPAGE_IMAGE)
            if image_element.is_displayed():
                print("Image is presented on the website.")
            else:
                print("Image is not displayed on the website.")
        except NoSuchElementException:
            print("Image element not found on the website.")


    def how_it_works_verify_element_fr(self):
        text = self.element_is_visible(self.locators.HOW_IT_WORKS_TITLE)
        expected_title = "Comment cela fonctionne-t-il ?"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PROGRESS_REPORTS_FR)
        expected_message = "Chaque compte enfant est composé de plusieurs rapports d'avancement tels que le temps, les activités, les tests et le rapport quotidien."
        assert text_two.text == expected_message
        text_combination = self.element_is_visible(self.locators.DEVICES_FR)
        expected_message_two = "Devices"
        assert text_combination.text == expected_message_two
        print("How it works page works good")

    def customer_reviews_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.CUSTOMER_REVIEWS_TITLE)
        print(text.text)
        expected_title = "Recensioni dei clienti"
        assert text.text == expected_title
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_ES).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_ES).click()
        time.sleep(2)
        if self.driver.get_window_rect()['width'] == self.driver.execute_script('return window.screen.width') and \
                self.driver.get_window_rect()['height'] == self.driver.execute_script('return window.screen.height'):
            print("Video is in full screen mode.")
        else:
            print("Video is not in full screen mode.")

    def language_courses_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "50 langues et plus de 30 000 activités d'apprentissage en ligne"
        assert text.text == expected_title
        self.scroll_down()
        time.sleep(2)
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_FR)
        expected_title_three = "Merci d'évaluer cette page"
        assert text_three.text == expected_title_three
        print("The webpage working as expected")



    def curriculum_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Curriculum"
        assert text.text == expected_title
        self.element_is_visible(self.locators.CURRICULUM__ACCOUNT_EN).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Créez votre compte gratuit"
        assert text_two.text == expected_title_two
        self.back()
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_FR)
        expected_title_three = "Merci d'évaluer cette page"
        assert text_three.text == expected_title_three
        print("Redirecting to create account works as expected")


    def parents_guide_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Conseils aux parents"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PARENTS_GUIDE_TEXT_FR)
        expected_text = "La persévérance est la clé. Il est important de garder à l'esprit qu'il faut se connecter et pratiquer une fois par jour."
        assert text_two.text == expected_text
        self.element_is_visible(self.locators.TRY_IT_FOR_FREE_ES).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Créez votre compte gratuit"
        assert text_two.text == expected_title_two
        print("The parents guide website working as expected. Try it for free redirects to the account creation")


    def schools_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Dinolingo pouor les écoles"
        assert text.text == expected_title
        self.element_is_visible(self.locators.SCHOOLS_GET_A_QUOTE_EN).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.SCHOOLS_QUOTE_FORMULARIO_EN)
            expected_text = "School Quote"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])
        else:
            print("The School Quote window not open")
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.SCHOOLS_QUOTE_SCHOOLS_TEXT_FR)
        expected_text_three = "Le service d'abonnement scolaire de Dinolingo est conçu spécialement pour les enseignants et les éducateurs et est personnalisé en fonction des écoles."
        assert text_three.text == expected_text_three
        image = self.element_is_visible(self.locators.SCHOOLS_IMAGE_EN)
        assert image.is_displayed(), "Image is not displayed on the page"
        print("Schools page working as expected. Users can open Schools Quote ")

    def homeschoolers_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Écoles à domicile"
        assert text.text == expected_title
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_FR)
        expected_title_three = "Merci d'évaluer cette page"
        assert text_three.text == expected_title_three
        print("The webpage working as expected")


    def privacy_verify_redirect_fr(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.PRIVACY_FR).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Dinolingo Privacy Policy"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def terms_verify_redirect_fr(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.TERMS_FR).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Terms & Conditions"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def contact_us_verify_redirect_fr(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CONTACT_US_FR).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def about_us_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "à propos de Dinolingo"
        assert text.text == expected_title
        self.element_is_visible(self.locators.ABOUT_US_CREATE_ACCOUNT_ES).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Créez votre compte gratuit"
        assert text_two.text == expected_title_two
        self.back()
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_FR)
        expected_title_three = "Merci d'évaluer cette page"
        print(text_three.text)
        assert text_three.text == expected_title_three
        print("Redirecting to create account works as expected")


    def help_and_support_verify_redirect_fr(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HELP_AND_SUPPORT_FR).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def spanish_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre l'Espagnol aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def french_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Français aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def english_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre l'Anglais aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def italian_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre l'Italien aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def german_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre l'Allemand aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def japanese_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Japonais aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def portuguese_eu_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Portugais aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def russian_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Russe aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def chinese_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Chinois aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def greek_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Grec aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def swedish_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Suédois aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def dutch_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Néérlandais aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def polish_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre Le Polonais aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def arabic_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre l'Arabe aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hebrew_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Hébreu aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def ukrainian_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre l'Ukrainien aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def latin_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Latin aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def korean_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Koréen aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hindi_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre l'Hindi aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def persian_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Perse aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def croatian_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Croate aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def turkish_for_kids_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Apprendre le Turc aux enfants"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def all_languages_verify_elements_fr(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "50 langues et plus de 30 000 activités d'apprentissage en ligne"
        assert text.text == expected_title


class GermanLanding(BasePage):
    locators = PageLocators()


    def verify_elements_on_homepage_de(self):
        text = self.element_is_visible(self.locators.MAIN_TEXT)
        expected = "#1 Website und App zum Sprachenlernen für Kinder"
        assert text.text == expected

        text_two = self.element_is_visible(self.locators.BEST_METHODS_TO_EACH_CHILDREN_DE)
        expected_two = "Die 10 besten Methoden, Kindern eine zweite Sprache beizubringen"
        assert text_two.text == expected_two
        try:
            image_element = self.element_is_visible(self.locators.HOMEPAGE_IMAGE)
            if image_element.is_displayed():
                print("Image is presented on the website.")
            else:
                print("Image is not displayed on the website.")
        except NoSuchElementException:
            print("Image element not found on the website.")


    def how_it_works_verify_element_de(self):
        text = self.element_is_visible(self.locators.HOW_IT_WORKS_TITLE)
        expected_title = "Wie das Programm genau funktioniert"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PROGRESS_REPORTS_DE)
        expected_message = "Das Konto eines jeden Kindes umfasst mehrere Fortschrittsberichte wie die Zeiterfassung, Aktivitäten, Tests und Tagesberichte."
        assert text_two.text == expected_message
        text_combination = self.element_is_visible(self.locators.DEVICES_DE)
        expected_message_two = "Geräte"
        assert text_combination.text == expected_message_two
        print("How it works page works good")

    def customer_reviews_verify_elements_de(self):
        text = self.element_is_visible(self.locators.CUSTOMER_REVIEWS_TITLE)
        print(text.text)
        expected_title = "Kundenbewertungen"
        assert text.text == expected_title
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_ES).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_ES).click()
        time.sleep(2)
        if self.driver.get_window_rect()['width'] == self.driver.execute_script('return window.screen.width') and \
                self.driver.get_window_rect()['height'] == self.driver.execute_script('return window.screen.height'):
            print("Video is in full screen mode.")
        else:
            print("Video is not in full screen mode.")

    def language_courses_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "50 Sprachen und mehr als 30.000 Online-Lernaktivitäten"
        assert text.text == expected_title
        self.scroll_down()
        time.sleep(2)
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_DE)
        expected_title_three = "Bitte bewerten Sie diese Seite"
        assert text_three.text == expected_title_three
        print("The webpage working as expected")



    def curriculum_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Lehrplan"
        assert text.text == expected_title
        self.element_is_visible(self.locators.CURRICULUM__ACCOUNT_EN).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Kostenloses Konto erstellen"
        assert text_two.text == expected_title_two
        self.back()
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_DE)
        expected_title_three = "Bitte bewerten Sie diese Seite"
        assert text_three.text == expected_title_three
        print("Redirecting to create account works as expected")


    def parents_guide_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Tipps für Eltern"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PARENTS_GUIDE_TEXT_DE)
        expected_text = "Hier liegt der Schlüssel zum Erfolg in der Beständigkeit. Erinnern Sie ihre Kinder daran, sich einmal täglich einzuloggen und zu üben."
        assert text_two.text == expected_text
        self.element_is_visible(self.locators.TRY_IT_FOR_FREE_ES).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Kostenloses Konto erstellen"
        assert text_two.text == expected_title_two
        print("The parents guide website working as expected. Try it for free redirects to the account creation")


    def schools_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Dinolingo für Schulen"
        assert text.text == expected_title
        self.element_is_visible(self.locators.SCHOOLS_GET_A_QUOTE_EN).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.SCHOOLS_QUOTE_FORMULARIO_EN)
            expected_text = "School Quote"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])
        else:
            print("The School Quote window not open")
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.SCHOOLS_QUOTE_SCHOOLS_TEXT_DE)
        expected_text_three = "Wir arbeiten mit öffentlichen Schulen, Privatschulen, Sprachschulen, Nachhilfelehrern, Behörden und Institutionen zusammen."
        assert text_three.text == expected_text_three
        image = self.element_is_visible(self.locators.SCHOOLS_IMAGE_EN)
        assert image.is_displayed(), "Image is not displayed on the page"
        print("Schools page working as expected. Users can open Schools Quote ")

    def homeschoolers_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Hausunterricht"
        assert text.text == expected_title
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_DE)
        expected_title_three = "Bitte bewerten Sie diese Seite"
        assert text_three.text == expected_title_three
        print("The webpage working as expected")


    def privacy_verify_redirect_de(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.PRIVACY_DE).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Dinolingo Privacy Policy"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def terms_verify_redirect_de(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.TERMS_DE).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Terms & Conditions"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def contact_us_verify_redirect_de(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CONTACT_US_DE).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def about_us_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Über Dinolingo"
        assert text.text == expected_title
        self.element_is_visible(self.locators.ABOUT_US_CREATE_ACCOUNT_ES).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Kostenloses Konto erstellen"
        assert text_two.text == expected_title_two
        self.back()
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_DE)
        expected_title_three = "Bitte bewerten Sie diese Seite"
        print(text_three.text)
        assert text_three.text == expected_title_three
        print("Redirecting to create account works as expected")


    def help_and_support_verify_redirect_de(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HELP_AND_SUPPORT_DE).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def spanish_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Spanisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def french_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Französisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def english_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Englisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def italian_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Italienisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def german_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Deutsch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def japanese_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Japanisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def portuguese_eu_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Portugiesisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def russian_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Russisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def chinese_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Chinesisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def greek_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Griechisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def swedish_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Schwedisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def dutch_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Niederländisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def polish_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Polnisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def arabic_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Arabisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hebrew_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Hebräisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def ukrainian_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Ukrainisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def latin_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Latein lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def korean_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Koreanisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hindi_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Hindi lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def persian_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Persisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def croatian_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Kroatisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def turkish_for_kids_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Türkisch lernen für Kinder"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def all_languages_verify_elements_de(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "50 Sprachen und mehr als 30.000 Online-Lernaktivitäten"
        assert text.text == expected_title

class PortugueseLanding(BasePage):
    locators = PageLocators()


    def verify_elements_on_homepage_pt(self):
        text = self.element_is_visible(self.locators.MAIN_TEXT)
        expected = "O Site e Aplicativo #1 de Aprendizado de Idiomas para Crianças"
        assert text.text == expected

        text_two = self.element_is_visible(self.locators.BEST_METHODS_TO_EACH_CHILDREN_PT)
        expected_two = "Os 10 melhores métodos para ensinar uma segunda língua para crianças"
        assert text_two.text == expected_two
        try:
            image_element = self.element_is_visible(self.locators.HOMEPAGE_IMAGE)
            if image_element.is_displayed():
                print("Image is presented on the website.")
            else:
                print("Image is not displayed on the website.")
        except NoSuchElementException:
            print("Image element not found on the website.")


    def how_it_works_verify_element_pt(self):
        text = self.element_is_visible(self.locators.HOW_IT_WORKS_TITLE)
        expected_title = "Como funciona"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PROGRESS_REPORTS_PT)
        expected_message = "A conta de cada criança inclui relatórios de progresso com dados como tempo, atividade, testes e desempenho diário."
        assert text_two.text == expected_message
        text_combination = self.element_is_visible(self.locators.DEVICES_PT)
        expected_message_two = "Dispositivos"
        assert text_combination.text == expected_message_two
        print("How it works page works good")

    def customer_reviews_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.CUSTOMER_REVIEWS_TITLE)
        print(text.text)
        expected_title = "Avaliações dos Usuários"
        assert text.text == expected_title
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_ES).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_ES).click()
        time.sleep(2)
        if self.driver.get_window_rect()['width'] == self.driver.execute_script('return window.screen.width') and \
                self.driver.get_window_rect()['height'] == self.driver.execute_script('return window.screen.height'):
            print("Video is in full screen mode.")
        else:
            print("Video is not in full screen mode.")

    def language_courses_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "50 idiomas e mais de 30.000 atividades de aprendizado online"
        assert text.text == expected_title
        self.scroll_down()
        time.sleep(2)
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_PT)
        expected_title_three = "Por favor, avalie esta página"
        assert text_three.text == expected_title_three
        print("The webpage working as expected")



    def curriculum_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Programa de Ensino"
        assert text.text == expected_title
        self.element_is_visible(self.locators.CURRICULUM__ACCOUNT_EN).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Crie sua conta grátis"
        assert text_two.text == expected_title_two
        self.back()
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_PT)
        expected_title_three = "Por favor, avalie esta página"
        assert text_three.text == expected_title_three
        print("Redirecting to create account works as expected")


    def parents_guide_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Dicas para os pais"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PARENTS_GUIDE_TEXT_PT)
        expected_text = "A consistência é um fator essencial. É importante lembrar de fazer login e praticar diariamente."
        assert text_two.text == expected_text
        self.element_is_visible(self.locators.TRY_IT_FOR_FREE_ES).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Crie sua conta grátis"
        assert text_two.text == expected_title_two
        print("The parents guide website working as expected. Try it for free redirects to the account creation")


    def schools_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Dinolingo para Escolas"
        assert text.text == expected_title
        self.element_is_visible(self.locators.SCHOOLS_GET_A_QUOTE_EN).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.SCHOOLS_QUOTE_FORMULARIO_EN)
            expected_text = "School Quote"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])
        else:
            print("The School Quote window not open")
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.SCHOOLS_QUOTE_SCHOOLS_TEXT_PT)
        expected_text_three = "Trabalhamos com escolas públicas, escolas cooperativas, escolas de idiomas, escolas particulares, professores de idiomas, governos e instituições."
        assert text_three.text == expected_text_three
        image = self.element_is_visible(self.locators.SCHOOLS_IMAGE_EN)
        assert image.is_displayed(), "Image is not displayed on the page"
        print("Schools page working as expected. Users can open Schools Quote ")

    def homeschoolers_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Ensino Domiciliar"
        assert text.text == expected_title
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_PT)
        expected_title_three = "Por favor, avalie esta página"
        assert text_three.text == expected_title_three
        print("The webpage working as expected")


    def privacy_verify_redirect_pt(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.PRIVACY_PT).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Dinolingo Privacy Policy"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def terms_verify_redirect_pt(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.TERMS_PT).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Terms & Conditions"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def contact_us_verify_redirect_pt(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CONTACT_US_PT).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def about_us_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "sobre o Dinolingo"
        assert text.text == expected_title
        self.element_is_visible(self.locators.ABOUT_US_CREATE_ACCOUNT_ES).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Crie sua conta grátis"
        assert text_two.text == expected_title_two
        self.back()
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_PT)
        expected_title_three = "Por favor, avalie esta página"
        print(text_three.text)
        assert text_three.text == expected_title_three
        print("Redirecting to create account works as expected")


    def help_and_support_verify_redirect_pt(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HELP_AND_SUPPORT_PT).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def spanish_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Espanhol para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def french_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Francês para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def english_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Inglês para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def italian_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Italiano para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def german_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Alemão para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def japanese_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Japonês para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def portuguese_eu_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Português para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def russian_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Russo para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def chinese_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Chinês para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def greek_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Grego para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def swedish_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Sueco para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def dutch_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Holandês para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def polish_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def arabic_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Árabe para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hebrew_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Hebraico para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def ukrainian_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Ucraniano para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def latin_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Latim para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def korean_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Coreano para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hindi_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Hindi para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def persian_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Persa para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def croatian_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Croata para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def turkish_for_kids_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Aprendizado de Turco para Crianças"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def all_languages_verify_elements_pt(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "50 idiomas e mais de 30.000 atividades de aprendizado online"
        assert text.text == expected_title




class RussianLanding(BasePage):
    locators = PageLocators()


    def verify_elements_on_homepage_ru(self):
        text = self.element_is_visible(self.locators.MAIN_TEXT)
        expected = "№1 сайт и приложение для изучения языков для детей"
        assert text.text == expected

        text_two = self.element_is_visible(self.locators.BEST_METHODS_TO_EACH_CHILDREN_RU)
        expected_two = "10 лучших способов научить детей второму языку"
        assert text_two.text == expected_two
        try:
            image_element = self.element_is_visible(self.locators.HOMEPAGE_IMAGE)
            if image_element.is_displayed():
                print("Image is presented on the website.")
            else:
                print("Image is not displayed on the website.")
        except NoSuchElementException:
            print("Image element not found on the website.")


    def how_it_works_verify_element_ru(self):
        text = self.element_is_visible(self.locators.HOW_IT_WORKS_TITLE)
        expected_title = "Как это работает"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PROGRESS_REPORTS_RU)
        expected_message = "Каждая учетная запись ребенка включает в себя несколько отчетов о ходе выполнения заданий, таких как время, активность, тест и ежедневный отчет."
        assert text_two.text == expected_message
        text_combination = self.element_is_visible(self.locators.DEVICES_RU)
        expected_message_two = "Устройства"
        assert text_combination.text == expected_message_two
        print("How it works page works good")

    def customer_reviews_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.CUSTOMER_REVIEWS_TITLE)
        print(text.text)
        expected_title = "Отзывы клиентов"
        assert text.text == expected_title
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_ES).click()
        time.sleep(2)
        self.element_is_visible(self.locators.CUSTOMER_REVIEWS_VIDEO_CLICK_ES).click()
        time.sleep(2)
        if self.driver.get_window_rect()['width'] == self.driver.execute_script('return window.screen.width') and \
                self.driver.get_window_rect()['height'] == self.driver.execute_script('return window.screen.height'):
            print("Video is in full screen mode.")
        else:
            print("Video is not in full screen mode.")

    def language_courses_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "50 языков и более 30 000 онлайн заданий"
        assert text.text == expected_title
        self.scroll_down()
        time.sleep(2)
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_RU)
        expected_title_three = "Пожалуйста, оцените эту страницу"
        assert text_three.text == expected_title_three
        print("The webpage working as expected")



    def curriculum_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Учебный план"
        assert text.text == expected_title
        self.element_is_visible(self.locators.CURRICULUM__ACCOUNT_EN).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Создайте бесплатную учетную запись"
        assert text_two.text == expected_title_two
        self.back()
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_RU)
        expected_title_three = "Пожалуйста, оцените эту страницу"
        assert text_three.text == expected_title_three
        print("Redirecting to create account works as expected")


    def parents_guide_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Советы для родителей"
        assert text.text == expected_title
        text_two = self.element_is_visible(self.locators.PARENTS_GUIDE_TEXT_EN)
        expected_text = "Consistency is the key. It is important to remember to login and practice once a day. Постоянство является ключом к успеху. Важно не забывать входить в систему и практиковаться один раз в день."
        assert text_two.text == expected_text
        self.element_is_visible(self.locators.TRY_IT_FOR_FREE_ES).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Создайте бесплатную учетную запись"
        assert text_two.text == expected_title_two
        print("The parents guide website working as expected. Try it for free redirects to the account creation")


    def schools_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Dinolingo для школ"
        assert text.text == expected_title
        self.element_is_visible(self.locators.SCHOOLS_GET_A_QUOTE_EN).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.SCHOOLS_QUOTE_FORMULARIO_EN)
            expected_text = "School Quote"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])
        else:
            print("The School Quote window not open")
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.SCHOOLS_QUOTE_SCHOOLS_TEXT_RU)
        expected_text_three = "Мы работаем с государственными и частными школами, языковыми школами, репетиторами, государственными учреждениями."
        assert text_three.text == expected_text_three
        image = self.element_is_visible(self.locators.SCHOOLS_IMAGE_EN)
        assert image.is_displayed(), "Image is not displayed on the page"
        print("Schools page working as expected. Users can open Schools Quote ")

    def homeschoolers_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Домашнее обучение"
        assert text.text == expected_title
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_RU)
        expected_title_three = "Пожалуйста, оцените эту страницу"
        assert text_three.text == expected_title_three
        print("The webpage working as expected")


    def privacy_verify_redirect_ru(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.PRIVACY_RU).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text_two = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Dinolingo Privacy Policy"
            assert text_two.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def terms_verify_redirect_ru(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.TERMS_RU).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.NEW_PAGE_HEADER)
            expected_text = "Terms & Conditions"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def contact_us_verify_redirect_ru(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.CONTACT_US_RU).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def about_us_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "о Dinolingo"
        assert text.text == expected_title
        self.element_is_visible(self.locators.ABOUT_US_CREATE_ACCOUNT_ES).click()
        text_two = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title_two = "Создайте бесплатную учетную запись"
        assert text_two.text == expected_title_two
        self.back()
        self.scroll_down()
        text_three = self.element_is_visible(self.locators.LANGUAGE_COURSES_RATE_THIS_PAGE_RU)
        expected_title_three = "Пожалуйста, оцените эту страницу"
        print(text_three.text)
        assert text_three.text == expected_title_three
        print("Redirecting to create account works as expected")


    def help_and_support_verify_redirect_ru(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HELP_AND_SUPPORT_RU).click()
        window_handles = self.driver.window_handles
        if len(window_handles) > 1:
            # Switch to the new window
            self.driver.switch_to.window(window_handles[-1])
            text = self.element_is_visible(self.locators.CONTACT_US_HEADER)
            expected_text = "Dinolingo Help and Support"
            assert text.text == expected_text
            self.driver.close()
            self.driver.switch_to.window(window_handles[0])

    def spanish_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите испанский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def french_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите французский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def english_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите английский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def italian_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите итальянский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def german_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите немецкий для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def japanese_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите японский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def portuguese_eu_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите португальский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def russian_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите русский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def chinese_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите китайский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def greek_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите греческий для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def swedish_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите шведский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def dutch_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите голландский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def polish_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите польский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def arabic_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите арабский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hebrew_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите иврит для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def ukrainian_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите украинский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def latin_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите латынь для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def korean_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите корейский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def hindi_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите хинди для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def persian_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите персидский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def croatian_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите хорватский для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")


    def turkish_for_kids_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "Изучите турецкий для детей"
        assert text.text == expected_title
        self.element_is_visible(self.locators.VIDEO_PLAY).click()
        video = self.element_is_visible(self.locators.VIDEO_PLAY)
        self.driver.execute_script("arguments[0].play();", video)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[@class='your-video-playback-overlay']"))
            )
            print("Video is playing.")
        except TimeoutException:
            print("Video did not start playing within the expected time.")

    def all_languages_verify_elements_ru(self):
        text = self.element_is_visible(self.locators.ALL_TITLES)
        expected_title = "50 языков и более 30 000 онлайн заданий"
        assert text.text == expected_title


