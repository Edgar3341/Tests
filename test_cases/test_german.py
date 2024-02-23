from main import GermanLanding
import allure


@allure.title("Test open the Website in German language ")
def test_open_website_german(driver):
    checking = GermanLanding(driver, "https://dinolingo.com/de")
    checking.open()
    checking.verify_elements_on_homepage_de()

@allure.title("How is works page in German language. Verify elements ")
def test_how_it_works_german(driver):
    checking = GermanLanding(driver, "https://dinolingo.com/de/how-it-works")
    checking.open()
    checking.how_it_works_verify_element_de()

@allure.title("Customers Review page in German language. Verify elements ")
def test_customer_reviews_german(driver):
    checking = GermanLanding(driver, "https://dinolingo.com/de/reviews")
    checking.open()
    checking.customer_reviews_verify_elements_de()

@allure.title("Language cources page in German language. Verify elements ")
def test_language_courses_german(driver):
    checking = GermanLanding(driver, "https://dinolingo.com/de/language-courses")
    checking.open()
    checking.language_courses_verify_elements_de()

@allure.title("Curriculum page in German language. Verify elements ")
def test_curriculum_german(driver):
    checking = GermanLanding(driver, "https://dinolingo.com/de/curriculum")
    checking.open()
    checking.curriculum_verify_elements_de()

@allure.title("Parents guide page in German language. Verify elements ")
def test_parents_guide_german(driver):
    checking = GermanLanding(driver, "https://dinolingo.com/de/parents")
    checking.open()
    checking.parents_guide_verify_elements_de()


@allure.title("Schools page in German language. Verify elements ")
def test_schools_german(driver):
    checking = GermanLanding(driver, "https://dinolingo.com/de/schools-teachers")
    checking.open()
    checking.schools_verify_elements_de()

@allure.title("Homeschoolers page in German language. Verify elements ")
def test_homeschoolers_german(driver):
    checking = GermanLanding(driver, "https://dinolingo.com/de/homeschool")
    checking.open()
    checking.homeschoolers_verify_elements_de()


@allure.title("Privacy. Redirect to the new window")
def test_privacy_german(driver):
    privacy = GermanLanding(driver, "https://dinolingo.com/de/")
    privacy.open()
    privacy.privacy_verify_redirect_de()


@allure.title("Terms. Redirect to the new window")
def test_terms_german(driver):
    terms = GermanLanding(driver, "https://dinolingo.com/de/")
    terms.open()
    terms.terms_verify_redirect_de()

@allure.title("Contact us. Redirect to the new window")
def test_contact_us_german(driver):
    contact_us = GermanLanding(driver, "https://dinolingo.com/de/")
    contact_us.open()
    contact_us.contact_us_verify_redirect_de()


@allure.title("About us. Redirect to the new window")
def test_about_us_german(driver):
    contact_us = GermanLanding(driver, "https://dinolingo.com/de/about-us")
    contact_us.open()
    contact_us.about_us_verify_elements_de()

@allure.title("Help and Support. Redirect to the new window")
def test_help_and_support_german(driver):
    contact_us = GermanLanding(driver, "https://dinolingo.com/de/")
    contact_us.open()
    contact_us.help_and_support_verify_redirect_de()



@allure.title("Spanish for kids. Verify all elements / Video playing")
def test_spanish_for_kids_german(driver):
    spanish = GermanLanding(driver, "https://dinolingo.com/de/learn-spanish-for-kids")
    spanish.open()
    spanish.spanish_for_kids_verify_elements_de()


@allure.title("French for kids . Verify all elements / Video playing")
def test_french_for_kids_german(driver):
    french = GermanLanding(driver, "https://dinolingo.com/de/learn-french-for-kids")
    french.open()
    french.french_for_kids_verify_elements_de()


@allure.title("English for kids. Verify all elements / Video playing")
def test_english_for_kids_german(driver):
    english = GermanLanding(driver, "https://dinolingo.com/de/learn-english-for-kids")
    english.open()
    english.english_for_kids_verify_elements_de()

@allure.title("Italian for kids. Verify all elements / Video playing")
def test_italian_for_kids_german(driver):
    italian = GermanLanding(driver, "https://dinolingo.com/de/learn-italian-for-kids")
    italian.open()
    italian.italian_for_kids_verify_elements_de()

@allure.title("German for kids. Verify all elements / Video playing")
def test_german_for_kids_german(driver):
    german = GermanLanding(driver, "https://dinolingo.com/de/learn-german-for-kids")
    german.open()
    german.german_for_kids_verify_elements_de()

@allure.title("Japanese for kids. Verify all elements / Video playing")
def test_japanese_for_kids_german(driver):
    japanese = GermanLanding(driver, "https://dinolingo.com/de/learn-japanese-for-kids")
    japanese.open()
    japanese.japanese_for_kids_verify_elements_de()

@allure.title("European and Brasil Portuguese for kids. Verify all elements / Video playing")
def test_portuguese_for_kids_german(driver):
    portuguese_eu = GermanLanding(driver, "https://dinolingo.com/de/learn-portuguese-for-kids")
    portuguese_eu.open()
    portuguese_eu.portuguese_eu_for_kids_verify_elements_de()


@allure.title("Russian for kids. Verify all elements / Video playing")
def test_russian_for_kids_german(driver):
    russian = GermanLanding(driver, "https://dinolingo.com/de/learn-russian-for-kids")
    russian.open()
    russian.russian_for_kids_verify_elements_de()

@allure.title("Chinese for kids. Verify all elements / Video playing")
def test_chinese_for_kids_german(driver):
    chinese = GermanLanding(driver, "https://dinolingo.com/de/learn-chinese-for-kids")
    chinese.open()
    chinese.chinese_for_kids_verify_elements_de()

@allure.title("Greek for kids. Verify all elements / Video playing")
def test_greek_for_kids_german(driver):
    greek = GermanLanding(driver, "https://dinolingo.com/de/learn-greek-for-kids")
    greek.open()
    greek.greek_for_kids_verify_elements_de()

@allure.title("Swedish for kids. Verify all elements / Video playing")
def test_swedish_for_kids_german(driver):
    swedish = GermanLanding(driver, "https://dinolingo.com/de/learn-swedish-for-kids")
    swedish.open()
    swedish.swedish_for_kids_verify_elements_de()

@allure.title("Dutch for kids. Verify all elements / Video playing")
def test_dutch_for_kids_german(driver):
    dutch = GermanLanding(driver, "https://dinolingo.com/de/learn-dutch-for-kids")
    dutch.open()
    dutch.dutch_for_kids_verify_elements_de()

@allure.title("Polish for kids. Verify all elements / Video playing")
def test_polish_for_kids_german(driver):
    polish = GermanLanding(driver, "https://dinolingo.com/de/learn-polish-for-kids")
    polish.open()
    polish.polish_for_kids_verify_elements_de()

@allure.title("Arabic for kids. Verify all elements / Video playing")
def test_arabic_for_kids_german(driver):
    arabic = GermanLanding(driver, "https://dinolingo.com/de/learn-arabic-for-kids")
    arabic.open()
    arabic.arabic_for_kids_verify_elements_de()

@allure.title("Hebrew for kids. Verify all elements / Video playing")
def test_hebrew_for_kids_german(driver):
    hebrew = GermanLanding(driver, "https://dinolingo.com/de/learn-hebrew-for-kids")
    hebrew.open()
    hebrew.hebrew_for_kids_verify_elements_de()

@allure.title("Ukrainian for kids. Verify all elements / Video playing")
def test_ukrainian_for_kids_german(driver):
    language = GermanLanding(driver, "https://dinolingo.com/de/learn-ukrainian-for-kids")
    language.open()
    language.ukrainian_for_kids_verify_elements_de()

@allure.title("Latin for kids. Verify all elements / Video playing")
def test_latin_for_kids_german(driver):
    language = GermanLanding(driver, "https://dinolingo.com/de/learn-latin-for-kids")
    language.open()
    language.latin_for_kids_verify_elements_de()

@allure.title("Korean for kids. Verify all elements / Video playing")
def test_korean_for_kids_german(driver):
    language = GermanLanding(driver, "https://dinolingo.com/de/learn-korean-for-kids")
    language.open()
    language.korean_for_kids_verify_elements_de()

@allure.title("Hindi for kids. Verify all elements / Video playing")
def test_hindi_for_kids_german(driver):
    language = GermanLanding(driver, "https://dinolingo.com/de/learn-hindi-for-kids")
    language.open()
    language.hindi_for_kids_verify_elements_de()

@allure.title("Persian for kids. Verify all elements / Video playing")
def test_persian_for_kids_german(driver):
    language = GermanLanding(driver, "https://dinolingo.com/de/learn-persian-for-kids")
    language.open()
    language.persian_for_kids_verify_elements_de()

@allure.title("Croatian for kids. Verify all elements / Video playing")
def test_croatian_for_kids_german(driver):
    language = GermanLanding(driver, "https://dinolingo.com/de/learn-croatian-for-kids")
    language.open()
    language.croatian_for_kids_verify_elements_de()

@allure.title("Turkish for kids. Verify all elements / Video playing")
def test_turkish_for_kids_german(driver):
    language = GermanLanding(driver, "https://dinolingo.com/de/learn-turkish-for-kids")
    language.open()
    language.turkish_for_kids_verify_elements_de()

@allure.title("All languages. Verify all elements")
def test_all_languages_for_kids_german(driver):
    language = GermanLanding(driver, "https://dinolingo.com/de/language-courses")
    language.open()
    language.all_languages_verify_elements_de()














