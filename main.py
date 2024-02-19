import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_english_language import PageLocators
from base.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

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
        self.element_is_visible(self.locators.PRIVACY).click()
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
        self.element_is_visible(self.locators.TERMS).click()
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
        self.element_is_visible(self.locators.CONTACT_US).click()
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
        text = self.element_is_visible(self.locators.ABOUT_US_TITLE_EN)
        expected_title = "about Dinolingo"
        assert text.text == expected_title

    def help_and_support_verify_redirect(self):
        self.scroll_down()
        self.scroll_down()
        self.element_is_visible(self.locators.HELP_AND_SUPPORT).click()
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
