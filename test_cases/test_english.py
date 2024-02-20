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

@allure.title("Privacy. Redirect to the new window")
def test_privacy(driver):
    privacy = EnglishLanding(driver, "https://dinolingo.com/")
    privacy.open()
    privacy.privacy_verify_redirect()


@allure.title("Terms. Redirect to the new window")
def test_terms(driver):
    terms = EnglishLanding(driver, "https://dinolingo.com/")
    terms.open()
    terms.terms_verify_redirect()

@allure.title("Contact us. Redirect to the new window")
def test_contact_us(driver):
    contact_us = EnglishLanding(driver, "https://dinolingo.com/")
    contact_us.open()
    contact_us.contact_us_verify_redirect()

@allure.title("About Us. Verify All elements on the page")
def test_about_us(driver):
    about_us = EnglishLanding(driver, "https://dinolingo.com/")
    about_us.open()
    about_us.about_us_verify_elements()


@allure.title("Help and Support. Redirect to the new window")
def test_help_and_support(driver):
    help = EnglishLanding(driver, "https://dinolingo.com/")
    help.open()
    help.help_and_support_verify_redirect()

@allure.title("Spanish for kids. Verify all elements / Video playing")
def test_spanish_for_kids(driver):
    spanish = EnglishLanding(driver, "https://dinolingo.com/")
    spanish.open()
    spanish.spanish_for_kids_verify_elements()


@allure.title("French for kids. Verify all elements / Video playing")
def test_french_for_kids(driver):
    french = EnglishLanding(driver, "https://dinolingo.com/")
    french.open()
    french.french_for_kids_verify_elements()


@allure.title("English for kids. Verify all elements / Video playing")
def test_english_for_kids(driver):
    english = EnglishLanding(driver, "https://dinolingo.com/")
    english.open()
    english.english_for_kids_verify_elements()

@allure.title("Italian for kids. Verify all elements / Video playing")
def test_italian_for_kids(driver):
    italian = EnglishLanding(driver, "https://dinolingo.com/")
    italian.open()
    italian.italian_for_kids_verify_elements()

@allure.title("German for kids. Verify all elements / Video playing")
def test_german_for_kids(driver):
    german = EnglishLanding(driver, "https://dinolingo.com/")
    german.open()
    german.german_for_kids_verify_elements()

@allure.title("Japanese for kids. Verify all elements / Video playing")
def test_japanese_for_kids(driver):
    japanese = EnglishLanding(driver, "https://dinolingo.com/")
    japanese.open()
    japanese.japanese_for_kids_verify_elements()

@allure.title("European Portuguese for kids. Verify all elements / Video playing")
def test_portuguese_eu_for_kids(driver):
    portuguese_eu = EnglishLanding(driver, "https://dinolingo.com/")
    portuguese_eu.open()
    portuguese_eu.portuguese_eu_for_kids_verify_elements()

@allure.title("Brasil Portuguese for kids. Verify all elements / Video playing")
def test_portuguese_br_for_kids(driver):
    portuguese_br = EnglishLanding(driver, "https://dinolingo.com/")
    portuguese_br.open()
    portuguese_br.portuguese_br_for_kids_verify_elements()


@allure.title("Russian for kids. Verify all elements / Video playing")
def test_russian_for_kids(driver):
    russian = EnglishLanding(driver, "https://dinolingo.com/")
    russian.open()
    russian.russian_for_kids_verify_elements()

@allure.title("Chinese for kids. Verify all elements / Video playing")
def test_chinese_for_kids(driver):
    chinese = EnglishLanding(driver, "https://dinolingo.com/")
    chinese.open()
    chinese.chinese_for_kids_verify_elements()

@allure.title("Greek for kids. Verify all elements / Video playing")
def test_greek_for_kids(driver):
    greek = EnglishLanding(driver, "https://dinolingo.com/")
    greek.open()
    greek.greek_for_kids_verify_elements()

@allure.title("Swedish for kids. Verify all elements / Video playing")
def test_swedish_for_kids(driver):
    swedish = EnglishLanding(driver, "https://dinolingo.com/")
    swedish.open()
    swedish.swedish_for_kids_verify_elements()

@allure.title("Dutch for kids. Verify all elements / Video playing")
def test_dutch_for_kids(driver):
    dutch = EnglishLanding(driver, "https://dinolingo.com/")
    dutch.open()
    dutch.dutch_for_kids_verify_elements()

@allure.title("Polish for kids. Verify all elements / Video playing")
def test_polish_for_kids(driver):
    polish = EnglishLanding(driver, "https://dinolingo.com/")
    polish.open()
    polish.polish_for_kids_verify_elements()

@allure.title("Arabic for kids. Verify all elements / Video playing")
def test_arabic_for_kids(driver):
    arabic = EnglishLanding(driver, "https://dinolingo.com/")
    arabic.open()
    arabic.arabic_for_kids_verify_elements()

@allure.title("Hebrew for kids. Verify all elements / Video playing")
def test_hebrew_for_kids(driver):
    hebrew = EnglishLanding(driver, "https://dinolingo.com/")
    hebrew.open()
    hebrew.hebrew_for_kids_verify_elements()


@allure.title("Ukrainian for kids. Verify all elements / Video playing")
def test_ukrainian_for_kids(driver):
    language = EnglishLanding(driver, "https://dinolingo.com/")
    language.open()
    language.ukrainian_for_kids_verify_elements()

@allure.title("Latin for kids. Verify all elements / Video playing")
def test_latin_for_kids(driver):
    language = EnglishLanding(driver, "https://dinolingo.com/")
    language.open()
    language.latin_for_kids_verify_elements()

@allure.title("Korean for kids. Verify all elements / Video playing")
def test_korean_for_kids(driver):
    language = EnglishLanding(driver, "https://dinolingo.com/")
    language.open()
    language.korean_for_kids_verify_elements()

@allure.title("Hindi for kids. Verify all elements / Video playing")
def test_hindi_for_kids(driver):
    language = EnglishLanding(driver, "https://dinolingo.com/")
    language.open()
    language.hindi_for_kids_verify_elements()

@allure.title("Persian for kids. Verify all elements / Video playing")
def test_persian_for_kids(driver):
    language = EnglishLanding(driver, "https://dinolingo.com/")
    language.open()
    language.persian_for_kids_verify_elements()

@allure.title("Croatian for kids. Verify all elements / Video playing")
def test_croatian_for_kids(driver):
    language = EnglishLanding(driver, "https://dinolingo.com/")
    language.open()
    language.croatian_for_kids_verify_elements()

@allure.title("Turkish for kids. Verify all elements / Video playing")
def test_turkish_for_kids(driver):
    language = EnglishLanding(driver, "https://dinolingo.com/")
    language.open()
    language.turkish_for_kids_verify_elements()

@allure.title("All languages. Verify all elements")
def test_all_languages_for_kids(driver):
    language = EnglishLanding(driver, "https://dinolingo.com/")
    language.open()
    language.all_languages_verify_elements()





