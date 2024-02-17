from main import EnglishLanding
import allure



@allure.title("Test open the Website ")
def test_open_website_english(driver):
    checking = EnglishLanding(driver, "https://dinolingo.com/")
    checking.open()
    checking.verify_elements_on_homepage()

@allure.title("How It works Endlish page")
def test_how_it_works_english_page(driver):
    how = EnglishLanding (driver, "https://dinolingo.com/")
    how.open()
    how.how_it_works_verify_elements()

@allure.title("Customer Reviews English page")
def test_customer_reviews_english_page(driver):
    reviews = EnglishLanding(driver, "https://dinolingo.com/")
    reviews.open()
    reviews.customer_reviews_verify_elements()

@allure.title("Language Courses English page. All elements verifying")
def test_language_courses(driver):
    language = EnglishLanding(driver, "https://dinolingo.com/")
    language.open()
    language.language_courses_verify_elements()


@allure.title("Curriculum page. All elements verifying / Create Account")
def test_curriculum_en(driver):
    curriculum = EnglishLanding(driver, "https://dinolingo.com/")
    curriculum.open()
    curriculum.curriculum_verify_elements()

@allure.title("Parents Guide. All elements verifying / Other Questions")
def test_parents_guide(driver):
    parents = EnglishLanding(driver, "https://dinolingo.com/")
    parents.open()
    parents.parents_guide_verify_elements()

@allure.title("Schools. All elements verifying / Get a Quite funcionality")
def test_schools(driver):
    schools = EnglishLanding(driver, "https://dinolingo.com/")
    schools.open()
    schools.schools_verify_elements()

@allure.title("Homeschoolers. All elements verifying / Check Image Persisting")
def test_homeschoolers(driver):
    homeschoolers = EnglishLanding(driver, "https://dinolingo.com/")
    homeschoolers.open()
    homeschoolers.homeschoolers_verify_elements()