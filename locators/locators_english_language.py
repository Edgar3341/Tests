
from selenium.webdriver.common.by import By
import random
class PageLocators:

    # ENGLISH LANDING
    MAIN_TEXT = (By.XPATH, "//h1")
    ACCEPT_COOKIE_BUTTON = (By.XPATH, '//button[contains(text(),"Accept All Cookies")]')
    ALL_TITLES = (By.XPATH, "//h1")
    # FOOTER
    HOW_IT_WORKS = (By.XPATH, "//a[contains(text(),'How it works')]")
    CUSTOMER_REVIEWS = (By.XPATH, "//a[contains(text(),'Customer Reviews')]")
    LANGUAGE_COURSES = (By.XPATH, "//a[contains(text(),'Language courses')]")
    CURRICULUM = (By.XPATH, "//a[contains(text(),'Curriculum')]")
    PARENTS_GUIDE = (By.XPATH, "//a[contains(text(),'Parents guide')]")
    SCHOOLS = (By.XPATH, "//a[contains(text(),'Schools')]")
    HOMESCHOOLES = (By.XPATH, "//a[contains(text(),'Homeschoolers')]")
    PRIVACY_EN = (By.XPATH, "//a[contains(text(),'Privacy')]")
    PRIVACY_ES = (By.XPATH, "//a[contains(text(),'Privacidad')]")
    TERMS_EN = (By.XPATH, "//a[contains(text(),'Terms')]")
    TERMS_ES = (By.XPATH, "//a[contains(text(),'Términos')]")
    CONTACT_US_EN = (By.XPATH, "//a[contains(text(),'Contact Us')]")
    CONTACT_US_ES = (By.XPATH, "//a[contains(text(),'Contáctenos')]")
    ABOUT_US = (By.XPATH, "//a[contains(text(),'About Us')]")
    HELP_AND_SUPPORT_EN = (By.XPATH, "//a[contains(text(),'Help & Support')]")
    HELP_AND_SUPPORT_ES = (By.XPATH, "//a[contains(text(),'Ayuda y Soporte')]")

    # SECOND TAB FOOTER
    SPANISH_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Spanish for kids')]")
    FRENCH_FOR_KIDS = (By.XPATH, "//a[contains(text(),'French for kids')]")
    ENGLISH_FOR_KIDS = (By.XPATH, "//a[contains(text(),'English for kids')]")
    ITALIAN_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Italian for kids')]")
    GERMAN_FOR_KIDS = (By.XPATH, "//a[contains(text(),'German for kids')]")
    JAPANESE_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Japanese for kids')]")
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
    HINDI_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Hindi for kids')]")
    PERSIAN_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Persian for kids')]")
    CROATIAN_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Croatian for kids')]")
    TURKISH_FOR_KIDS = (By.XPATH, "//a[contains(text(),'Turkish for kids')]")
    SEE_ALL_50_LANGUAGES = (By.XPATH, "//a[contains(text(),'See all 50 languages')]")



    # HOMEPAGE
    BEST_METHODS_TO_EACH_CHILDREN_EN = (By.XPATH, "//h2[contains(text(),'Best 10 methods to teach children a second languag')]")
    BEST_METHODS_TO_EACH_CHILDREN_ES = (By.XPATH, "//h2[contains(text(),'Los mejores 10 métodos para enseñar un segundo idioma a niños')]")
    HOMEPAGE_IMAGE = (By.XPATH, "//div[@class='image']/img")
    HOMEPAGE_LANGUAGE = (By.XPATH, "//header/div[1]/div[2]/div[1]/div[2]")
    HOMEPAGE_LANGUAGE_SPANISH = (By.XPATH, "//span[contains(text(),'Español')]")


    # NOW IT WORKS
    HOW_IT_WORKS_TITLE = (By.XPATH, "//h1")
    PROGRESS_REPORTS_EN = (By.XPATH, "//p[contains(text(),'Each child account includes several progress repor')]")
    PROGRESS_REPORTS_ES = (By.XPATH, "//p[contains(text(),'Cada cuenta de niño incluye varios reportes de pro')]")

    DEVICES_ES = (By.XPATH, "//h4[contains(text(),'Dispositivos')]")
    RECENT_COMBINATION_ES = (By.XPATH, "//p[contains(text(),'Recent studies have shown that children prefer to ')]")

    # CUSTOMER REVIEW
    CUSTOMER_REVIEWS_TITLE = (By.XPATH, "//h1")
    CUSTOMER_REVIEWS_VIDEO = (By.XPATH, "//div[@class='slideBlock fades']//iframe")
    CUSTOMER_REVIEWS_VIDEO_CLICK_EN = (By.XPATH, "//body/app-root[1]/ng-component[1]/ng-component[1]/div[1]/section[3]/article[1]/div[1]")
    CUSTOMER_REVIEWS_VIDEO_CLICK_ES = (By.XPATH, "//body/app-root[1]/ng-component[1]/ng-component[1]/div[1]/section[3]/article[1]")
    CUSTOMER_REVIEWS_VIDEO_PLAYING = (By.CSS_SELECTOR, "video")

    # LANGUAGE COURSES
    LANGUAGE_COURSES_TITLE_EN = (By.XPATH, "//h1[contains(text(),'50 languages & 30,000+ online learning activities')]")
    LANGUAGE_COURSES_RATE_THIS_PAGE_EN = (By.XPATH, "//div[contains(text(),'Please rate this page')]")
    LANGUAGE_COURSES_RATE_THIS_PAGE_ES = (By.XPATH, "//div[contains(text(),'Por favor califique esta página')]")

    # CURRICULUM
    CURRICULUM_HEADER_TEXT_EN = (By.XPATH, "//h2[contains(text(),'Dinolingo Lesson Plan & Curriculum')]")
    CURRICULUM__ACCOUNT_EN = (By.XPATH, "//body/app-root[1]/ng-component[1]/ng-component[1]/div[1]/section[1]/article[1]/div[1]/div[1]/button[1]/a[1]")

    # PARENTS GUIDE
    PARENTS_GUIDE_TITLE_EN = (By.XPATH, "//h1[contains(text(),'Tips for parents')]")
    PARENTS_GUIDE_TEXT_EN = (By.XPATH, "//p[contains(text(),'Consistency is the key. It is important to remembe')]")
    PARENTS_GUIDE_TEXT_ES = (By.XPATH, "//p[contains(text(),'La consistencia es la clave. Es importante recorda')]")
    TRY_IT_FOR_FREE_ES = (By.XPATH, "//body/app-root[1]/ng-component[1]/ng-component[1]/div[1]/section[1]/article[1]/div[1]/div[1]/button[1]/a[1]")
    PARENTS_GUIDE_OTHER_QUESTIONS_EN = (By.XPATH, "//h4[contains(text(),'Why should my child learn a foreign language now?')]")
    PARENTS_GUIDE_OTHER_QUESTIONS_ANSWER_EN = (By.XPATH, "//p[contains(text(),'There is convincing evidence, which suggests that ')]")

    # SCHOOLS
    SCHOOLS_TITLE_EN = (By.XPATH, "//h1[contains(text(),'Dinolingo for Schools')]")
    SCHOOLS_GET_A_QUOTE_EN = (By.XPATH, "//body/app-root[1]/ng-component[1]/ng-component[1]/div[1]/section[1]/article[1]/div[1]/div[1]/button[1]/a[1]")
    SCHOOLS_QUOTE_FORMULARIO_EN = (By.XPATH, "//h1[contains(text(),'School Quote')]")
    SCHOOLS_QUOTE_SCHOOLS_TEXT_EN = (By.XPATH, "//p[contains(text(),'We work with public schools, charter schools, lang')]")
    SCHOOLS_QUOTE_SCHOOLS_TEXT_ES = (By.XPATH, "//p[contains(text(),'Trabajamos con escuelas públicas, escuelas subvenc')]")
    SCHOOLS_IMAGE_EN = (By.XPATH, "//div[@class='servicesBlock']//img[@src='assets/pictures/customers.jpg']")


    # HOMESCHOOLERS
    HOMESCHOOLERS_TITLE_EN = (By.XPATH, "//h1[contains(text(),'Homeschoolers')]")
    HOMESCHOOLERS_IMAGE = (By.XPATH, "//img[@title='Flying Dino']")\

    # PRIVACY POLICY
    NEW_PAGE_HEADER = (By.XPATH, "//h1[@class='title']")

    # CONTACT_US PAGE
    CONTACT_US_HEADER = (By.XPATH, "//h1[contains(text(),'Dinolingo Help and Support')]")

    # ABOUT US
    ABOUT_US_CREATE_ACCOUNT_ES = (By.XPATH, "//body/app-root[1]/ng-component[1]/app-about-json[1]/div[1]/section[1]/article[1]/div[1]/div[1]/button[1]/a[1]")

    # ALL COURSES
    LANGUAGE_HEADERS_EN = (By.XPATH, "//h1[@class='white baloo2']")
    VIDEO_PLAY = (By.XPATH, "//body/app-root[1]/ng-component[1]/ng-component[1]/div[1]/section[5]/article[1]/video[1]")





