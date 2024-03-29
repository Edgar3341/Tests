from main import SpanishLanding
import allure


@allure.title("Test open the Website in Spanish language ")
def test_open_website_spanish(driver):
    checking = SpanishLanding(driver, "https://dinolingo.com/es")
    checking.open()
    checking.verify_elements_on_homepage_es()

@allure.title("How is works page in Spanish language. Verify elements ")
def test_how_it_works_spanish(driver):
    checking = SpanishLanding(driver, "https://dinolingo.com/")
    checking.open()
    checking.how_it_works_verify_element_es()

@allure.title("Customers Review page in Spanish language. Verify elements ")
def test_customer_reviews_spanish(driver):
    checking = SpanishLanding(driver, "https://dinolingo.com/es/reviews")
    checking.open()
    checking.customer_reviews_verify_elements_es()

@allure.title("Language cources page in Spanish language. Verify elements ")
def test_language_courses_spanish(driver):
    checking = SpanishLanding(driver, "https://dinolingo.com/es/language-courses")
    checking.open()
    checking.language_courses_verify_elements_es()

@allure.title("Curriculum page in Spanish language. Verify elements ")
def test_curriculum_spanish(driver):
    checking = SpanishLanding(driver, "https://dinolingo.com/es/curriculum")
    checking.open()
    checking.curriculum_verify_elements_es()

@allure.title("Parents guide page in Spanish language. Verify elements ")
def test_parents_guide_spanish(driver):
    checking = SpanishLanding(driver, "https://dinolingo.com/es/parents")
    checking.open()
    checking.parents_guide_verify_elements_es()


@allure.title("Schools page in Spanish language. Verify elements ")
def test_schools_spanish(driver):
    checking = SpanishLanding(driver, "https://dinolingo.com/es/schools-teachers")
    checking.open()
    checking.schools_verify_elements_es()

@allure.title("Homeschoolers page in Spanish language. Verify elements ")
def test_homeschoolers_spanish(driver):
    checking = SpanishLanding(driver, "https://dinolingo.com/es/homeschool")
    checking.open()
    checking.homeschoolers_verify_elements_es()


@allure.title("Privacy. Redirect to the new window")
def test_privacy_spanish(driver):
    privacy = SpanishLanding(driver, "https://dinolingo.com/es/")
    privacy.open()
    privacy.privacy_verify_redirect_es()


@allure.title("Terms. Redirect to the new window")
def test_terms_spanish(driver):
    terms = SpanishLanding(driver, "https://dinolingo.com/es/")
    terms.open()
    terms.terms_verify_redirect_es()

@allure.title("Contact us. Redirect to the new window")
def test_contact_us_spanish(driver):
    contact_us = SpanishLanding(driver, "https://dinolingo.com/es/")
    contact_us.open()
    contact_us.contact_us_verify_redirect_es()


@allure.title("About us. Redirect to the new window")
def test_about_us_spanish(driver):
    contact_us = SpanishLanding(driver, "https://dinolingo.com/es/about-us")
    contact_us.open()
    contact_us.about_us_verify_elements_es()

@allure.title("Help and Support. Redirect to the new window")
def test_help_and_support_spanish(driver):
    contact_us = SpanishLanding(driver, "https://dinolingo.com/es/")
    contact_us.open()
    contact_us.help_and_support_verify_redirect_es()



@allure.title("Spanish for kids. Verify all elements / Video playing")
def test_spanish_for_kids_spanish(driver):
    spanish = SpanishLanding(driver, "https://dinolingo.com/es/learn-spanish-for-kids")
    spanish.open()
    spanish.spanish_for_kids_verify_elements_es()


@allure.title("French for kids . Verify all elements / Video playing")
def test_french_for_kids_spanish(driver):
    french = SpanishLanding(driver, "https://dinolingo.com/es/learn-french-for-kids")
    french.open()
    french.french_for_kids_verify_elements_es()


@allure.title("English for kids. Verify all elements / Video playing")
def test_english_for_kids_spanish(driver):
    english = SpanishLanding(driver, "https://dinolingo.com/es/learn-english-for-kids")
    english.open()
    english.english_for_kids_verify_elements_es()

@allure.title("Italian for kids. Verify all elements / Video playing")
def test_italian_for_kids_spanish(driver):
    italian = SpanishLanding(driver, "https://dinolingo.com/es/learn-italian-for-kids")
    italian.open()
    italian.italian_for_kids_verify_elements_es()

@allure.title("German for kids. Verify all elements / Video playing")
def test_german_for_kids_spanish(driver):
    german = SpanishLanding(driver, "https://dinolingo.com/es/learn-german-for-kids")
    german.open()
    german.german_for_kids_verify_elements_es()

@allure.title("Japanese for kids. Verify all elements / Video playing")
def test_japanese_for_kids_spanish(driver):
    japanese = SpanishLanding(driver, "https://dinolingo.com/es/learn-japanese-for-kids")
    japanese.open()
    japanese.japanese_for_kids_verify_elements_es()

@allure.title("European and Brasil Portuguese for kids. Verify all elements / Video playing")
def test_portuguese_for_kids_spanish(driver):
    portuguese_eu = SpanishLanding(driver, "https://dinolingo.com/es/learn-euportuguese-for-kids")
    portuguese_eu.open()
    portuguese_eu.portuguese_eu_for_kids_verify_elements_es()


@allure.title("Russian for kids. Verify all elements / Video playing")
def test_russian_for_kids_spanish(driver):
    russian = SpanishLanding(driver, "https://dinolingo.com/es/learn-russian-for-kids")
    russian.open()
    russian.russian_for_kids_verify_elements_es()

@allure.title("Chinese for kids. Verify all elements / Video playing")
def test_chinese_for_kids_spanish(driver):
    chinese = SpanishLanding(driver, "https://dinolingo.com/es/learn-chinese-for-kids")
    chinese.open()
    chinese.chinese_for_kids_verify_elements_es()

@allure.title("Greek for kids. Verify all elements / Video playing")
def test_greek_for_kids_spanish(driver):
    greek = SpanishLanding(driver, "https://dinolingo.com/es/learn-greek-for-kids")
    greek.open()
    greek.greek_for_kids_verify_elements_es()

@allure.title("Swedish for kids. Verify all elements / Video playing")
def test_swedish_for_kids_spanish(driver):
    swedish = SpanishLanding(driver, "https://dinolingo.com/es/learn-swedish-for-kids")
    swedish.open()
    swedish.swedish_for_kids_verify_elements_es()

@allure.title("Dutch for kids. Verify all elements / Video playing")
def test_dutch_for_kids_spanish(driver):
    dutch = SpanishLanding(driver, "https://dinolingo.com/es/learn-dutch-for-kids")
    dutch.open()
    dutch.dutch_for_kids_verify_elements_es()

@allure.title("Polish for kids. Verify all elements / Video playing")
def test_polish_for_kids_spanish(driver):
    polish = SpanishLanding(driver, "https://dinolingo.com/es/learn-polish-for-kids")
    polish.open()
    polish.polish_for_kids_verify_elements_es()

@allure.title("Arabic for kids. Verify all elements / Video playing")
def test_arabic_for_kids_spanish(driver):
    arabic = SpanishLanding(driver, "https://dinolingo.com/es/learn-arabic-for-kids")
    arabic.open()
    arabic.arabic_for_kids_verify_elements_es()

@allure.title("Hebrew for kids. Verify all elements / Video playing")
def test_hebrew_for_kids_spanish(driver):
    hebrew = SpanishLanding(driver, "https://dinolingo.com/es/learn-hebrew-for-kids")
    hebrew.open()
    hebrew.hebrew_for_kids_verify_elements_es()

@allure.title("Ukrainian for kids. Verify all elements / Video playing")
def test_ukrainian_for_kids_spanish(driver):
    language = SpanishLanding(driver, "https://dinolingo.com/es/learn-ukrainian-for-kids")
    language.open()
    language.ukrainian_for_kids_verify_elements_es()

@allure.title("Latin for kids. Verify all elements / Video playing")
def test_latin_for_kids_spanish(driver):
    language = SpanishLanding(driver, "https://dinolingo.com/es/learn-latin-for-kids")
    language.open()
    language.latin_for_kids_verify_elements_es()

@allure.title("Korean for kids. Verify all elements / Video playing")
def test_korean_for_kids_spanish(driver):
    language = SpanishLanding(driver, "https://dinolingo.com/es/learn-korean-for-kids")
    language.open()
    language.korean_for_kids_verify_elements_es()

@allure.title("Hindi for kids. Verify all elements / Video playing")
def test_hindi_for_kids_spanish(driver):
    language = SpanishLanding(driver, "https://dinolingo.com/es/learn-hindi-for-kids")
    language.open()
    language.hindi_for_kids_verify_elements_es()

@allure.title("Persian for kids. Verify all elements / Video playing")
def test_persian_for_kids_spanish(driver):
    language = SpanishLanding(driver, "https://dinolingo.com/es/learn-persian-for-kids")
    language.open()
    language.persian_for_kids_verify_elements_es()

@allure.title("Croatian for kids. Verify all elements / Video playing")
def test_croatian_for_kids_spanish(driver):
    language = SpanishLanding(driver, "https://dinolingo.com/es/learn-croatian-for-kids")
    language.open()
    language.croatian_for_kids_verify_elements_es()

@allure.title("Turkish for kids. Verify all elements / Video playing")
def test_turkish_for_kids_spanish(driver):
    language = SpanishLanding(driver, "https://dinolingo.com/es/learn-turkish-for-kids")
    language.open()
    language.turkish_for_kids_verify_elements_es()

@allure.title("All languages. Verify all elements")
def test_all_languages_for_kids_spanish(driver):
    language = SpanishLanding(driver, "https://dinolingo.com/es/language-courses")
    language.open()
    language.all_languages_verify_elements_es()














