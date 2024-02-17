
from selenium.webdriver.common.by import By
import random
class PageLocators:

    # ENGLISH LANDING
    MAIN_TEXT = (By.XPATH, "//h1[contains(text(),'#1 Language Learning Website and App for Kids')]")

    # FOOTER
    HOW_IT_WORKS = (By.XPATH, "//a[contains(text(),'How it works')]")
    CUSTOMER_REVIEWS = (By.XPATH, "//a[contains(text(),'Customer Reviews')]")
    LANGUAGE_COURSES = (By.XPATH, "//a[contains(text(),'Language courses')]")
    CURRICULUM = (By.XPATH, "//a[contains(text(),'Curriculum')]")
    PARENTS_GUIDE = (By.XPATH, "//a[contains(text(),'Parents guide')]")
    SCHOOLS = (By.XPATH, "//a[contains(text(),'Schools')]")
    HOMESCHOOLES = (By.XPATH, "//a[contains(text(),'Homeschoolers')]")
    PRIVACY = (By.XPATH, "//a[contains(text(),'Privacy')]")
    TERMS = (By.XPATH, "//a[contains(text(),'Terms')]")
    CONTACT_US = (By.XPATH, "//a[contains(text(),'Contact Us')]")
    ABOUT_US = (By.XPATH, "//a[contains(text(),'About Us')]")
    HELP_AND_SUPPORT = (By.XPATH, "//a[contains(text(),'Help & Support')]")

    # SECOND TAB FOOTER
    SPANISH_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Spanish for kids')]")
    FRENCH_FOR_KIDS = (By.XPATH, "//a[contains(text(),'French for kids')]")
    ENGLISH_FOR_KIDS = (By.XPATH, "//a[contains(text(),'English for kids')]")
    ITALIAN_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Italian for kids')]")
    GERMAN_FOR_KIDS = (By.XPATH, "//a[contains(text(),'German for kids')]")
    PORTUGUESE_EU_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Portuguese (EU) for kids')]")
    PORTUGUESE_BR_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Portuguese (BR) for kids')]")
    RUSSIAN_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Russian for kids')]")
    CHINESE_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Chinese for kids')]")
    GREEK_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Greek for kids')]")
    SWEDISH_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Swedish for kids')]")

    # THIRD TAB FOOTER
    DUTCH_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Dutch for kids')]")
    POLISH_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Polish for kids')]")
    ARABIC_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Arabic for kids')]")
    HEBREW_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Hebrew for kids')]")
    UKRAINIAN_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Ukrainian for kids')]")
    LATIN_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Latin for kids')]")
    KOREAN_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Korean for kids')]")
    HINDI_FOR_KIDS = (By.XPATH, "//a[contains(text(),'HINDI for kids')]")
    PERSIAN_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Persian for kids')]")
    CROATIAN_FOR_KIDS = (By.XPATH, "//a[contains(text(),'CROATIAN for kids')]")
    TURKISH_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Turkish for kids')]")
    SEE_ALL_50_LANGUAGES = (By.XPATH, "//a[contains(text(),'See all 50 languages')]")



    # HOMEPAGE
    BEST_METHODS_TO_EACH_CHILDREN = (By.XPATH, "//h2[contains(text(),'Best 10 methods to teach children a second languag')]")
    HOMEPAGE_IMAGE = (By.XPATH, "//div[@class='image']/img")


    # NOW IT WORKS
    HOW_IT_WORKS_TITLE = (By.XPATH, "//h1[contains(text(),'How it works')]")
    PROGRESS_REPORTS = (By.XPATH, "//p[contains(text(),'Each child account includes several progress repor')]")
    RECENT_COMBINATION = (By.XPATH, "//p[contains(text(),'Recent studies have shown that children prefer to ')]")

    # CUSTOMER REVIEW
    CUSTOMER_REVIEWS_TITLE_EN = (By.XPATH, "//h1[contains(text(),'Customer Reviews')]")
    CUSTOMER_REVIEWS_VIDEO = (By.XPATH, "//div[@class='slideBlock fades']//iframe")
    CUSTOMER_REVIEWS_VIDEO_CLICK = (By.XPATH, "//body/app-root[1]/ng-component[1]/ng-component[1]/div[1]/section[3]/article[1]/div[1]")
    CUSTOMER_REVIEWS_VIDEO_PLAYING = (By.CSS_SELECTOR, "video")

    # LANGUAGE COURSES
    LANGUAGE_COURSES_TITLE_EN = (By.XPATH, "//h1[contains(text(),'50 languages & 30,000+ online learning activities')]")
    LANGUAGE_COURSES_RATE_THIS_PAGE_EN = (By.XPATH, "//div[contains(text(),'5 stars')]")

    # CURRICULUM
    CURRICULUM_HEADER_TEXT_EN = (By.XPATH, "//h2[contains(text(),'Dinolingo Lesson Plan & Curriculum')]")
    CURRICULUM_CREATE_ACCOUNT_EN = (By.XPATH, "//body/app-root[1]/ng-component[1]/ng-component[1]/div[1]/section[1]/article[1]/div[1]/div[1]/button[1]/a[1]")

    # PARENTS GUIDE
    PARENTS_GUIDE_TITLE_EN = (By.XPATH, "//h1[contains(text(),'Tips for parents')]")
    PARENTS_GUIDE_TEXT_EN = (By.XPATH, "//p[contains(text(),'Consistency is the key. It is important to remembe')]")
    PARENTS_GUIDE_OTHER_QUESTIONS_EN = (By.XPATH, "//h4[contains(text(),'Why should my child learn a foreign language now?')]")
    PARENTS_GUIDE_OTHER_QUESTIONS_ANSWER_EN = (By.XPATH, "//p[contains(text(),'There is convincing evidence, which suggests that ')]")

    # SCHOOLS
    SCHOOLS_TITLE_EN = (By.XPATH, "//h1[contains(text(),'Dinolingo for Schools')]")
    SCHOOLS_GET_A_QUOTE_EN = (By.XPATH, "//body/app-root[1]/ng-component[1]/ng-component[1]/div[1]/section[1]/article[1]/div[1]/div[1]/button[1]/a[1]")
    SCHOOLS_QUOTE_FORMULARIO_EN = (By.XPATH, "//h1[contains(text(),'School Quote')]")
    SCHOOLS_QUOTE_SCHOOLS_TEXT_EN = (By.XPATH, "//p[contains(text(),'We work with public schools, charter schools, lang')]")
    SCHOOLS_IMAGE_EN = (By.XPATH, "//div[@class='servicesBlock']//img[@src='assets/pictures/customers.jpg']")






