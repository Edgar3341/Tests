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
