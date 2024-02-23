from main import FrenchLanding
import allure


@allure.title("Test open the Website in French language ")
def test_open_website_french(driver):
    checking = FrenchLanding(driver, "https://dinolingo.com/fr")
    checking.open()
    checking.verify_elements_on_homepage_fr()

@allure.title("How is works page in French language. Verify elements ")
def test_how_it_works_french(driver):
    checking = FrenchLanding(driver, "https://dinolingo.com/fr/how-it-works")
    checking.open()
    checking.how_it_works_verify_element_fr()

@allure.title("Customers Review page in French language. Verify elements ")
def test_customer_reviews_french(driver):
    checking = FrenchLanding(driver, "https://dinolingo.com/it/reviews")
    checking.open()
    checking.customer_reviews_verify_elements_fr()

@allure.title("Language cources page in French language. Verify elements ")
def test_language_courses_french(driver):
    checking = FrenchLanding(driver, "https://dinolingo.com/fr/language-courses")
    checking.open()
    checking.language_courses_verify_elements_fr()

@allure.title("Curriculum page in French language. Verify elements ")
def test_curriculum_french(driver):
    checking = FrenchLanding(driver, "https://dinolingo.com/fr/curriculum")
    checking.open()
    checking.curriculum_verify_elements_fr()

@allure.title("Parents guide page in French language. Verify elements ")
def test_parents_guide_french(driver):
    checking = FrenchLanding(driver, "https://dinolingo.com/fr/parents")
    checking.open()
    checking.parents_guide_verify_elements_fr()


@allure.title("Schools page in French language. Verify elements ")
def test_schools_french(driver):
    checking = FrenchLanding(driver, "https://dinolingo.com/fr/schools-teachers")
    checking.open()
    checking.schools_verify_elements_fr()

@allure.title("Homeschoolers page in Italian language. Verify elements ")
def test_homeschoolers_french(driver):
    checking = FrenchLanding(driver, "https://dinolingo.com/fr/homeschool")
    checking.open()
    checking.homeschoolers_verify_elements_fr()


@allure.title("Privacy. Redirect to the new window")
def test_privacy_french(driver):
    privacy = FrenchLanding(driver, "https://dinolingo.com/fr/")
    privacy.open()
    privacy.privacy_verify_redirect_fr()


@allure.title("Terms. Redirect to the new window")
def test_terms_french(driver):
    terms = FrenchLanding(driver, "https://dinolingo.com/fr/")
    terms.open()
    terms.terms_verify_redirect_fr()

@allure.title("Contact us. Redirect to the new window")
def test_contact_us_french(driver):
    contact_us = FrenchLanding(driver, "https://dinolingo.com/fr/")
    contact_us.open()
    contact_us.contact_us_verify_redirect_fr()


@allure.title("About us. Redirect to the new window")
def test_about_us_french(driver):
    contact_us = FrenchLanding(driver, "https://dinolingo.com/fr/about-us")
    contact_us.open()
    contact_us.about_us_verify_elements_fr()

@allure.title("Help and Support. Redirect to the new window")
def test_help_and_support_french(driver):
    contact_us = FrenchLanding(driver, "https://dinolingo.com/fr/")
    contact_us.open()
    contact_us.help_and_support_verify_redirect_fr()



@allure.title("Spanish for kids. Verify all elements / Video playing")
def test_spanish_for_kids_french(driver):
    spanish = FrenchLanding(driver, "https://dinolingo.com/fr/learn-spanish-for-kids")
    spanish.open()
    spanish.spanish_for_kids_verify_elements_fr()


@allure.title("French for kids . Verify all elements / Video playing")
def test_french_for_kids_french(driver):
    french = FrenchLanding(driver, "https://dinolingo.com/fr/learn-french-for-kids")
    french.open()
    french.french_for_kids_verify_elements_fr()


@allure.title("English for kids. Verify all elements / Video playing")
def test_english_for_kids_frenchn(driver):
    english = FrenchLanding(driver, "https://dinolingo.com/fr/learn-english-for-kids")
    english.open()
    english.english_for_kids_verify_elements_fr()

@allure.title("Italian for kids. Verify all elements / Video playing")
def test_italian_for_kids_french(driver):
    italian = FrenchLanding(driver, "https://dinolingo.com/fr/learn-italian-for-kids")
    italian.open()
    italian.italian_for_kids_verify_elements_fr()

@allure.title("German for kids. Verify all elements / Video playing")
def test_german_for_kids_french(driver):
    german = FrenchLanding(driver, "https://dinolingo.com/fr/learn-german-for-kids")
    german.open()
    german.german_for_kids_verify_elements_fr()

@allure.title("Japanese for kids. Verify all elements / Video playing")
def test_japanese_for_kids_french(driver):
    japanese = FrenchLanding(driver, "https://dinolingo.com/fr/learn-japanese-for-kids")
    japanese.open()
    japanese.japanese_for_kids_verify_elements_fr()

@allure.title("European and Brasil Portuguese for kids. Verify all elements / Video playing")
def test_portuguese_for_kids_french(driver):
    portuguese_eu = FrenchLanding(driver, "https://dinolingo.com/fr/learn-euportuguese-for-kids")
    portuguese_eu.open()
    portuguese_eu.portuguese_eu_for_kids_verify_elements_fr()


@allure.title("Russian for kids. Verify all elements / Video playing")
def test_russian_for_kids_french(driver):
    russian = FrenchLanding(driver, "https://dinolingo.com/fr/learn-russian-for-kids")
    russian.open()
    russian.russian_for_kids_verify_elements_fr()

@allure.title("Chinese for kids. Verify all elements / Video playing")
def test_chinese_for_kids_french(driver):
    chinese = FrenchLanding(driver, "https://dinolingo.com/fr/learn-chinese-for-kids")
    chinese.open()
    chinese.chinese_for_kids_verify_elements_fr()

@allure.title("Greek for kids. Verify all elements / Video playing")
def test_greek_for_kids_french(driver):
    greek = FrenchLanding(driver, "https://dinolingo.com/fr/learn-greek-for-kids")
    greek.open()
    greek.greek_for_kids_verify_elements_fr()

@allure.title("Swedish for kids. Verify all elements / Video playing")
def test_swedish_for_kids_french(driver):
    swedish = FrenchLanding(driver, "https://dinolingo.com/fr/learn-swedish-for-kids")
    swedish.open()
    swedish.swedish_for_kids_verify_elements_fr()

@allure.title("Dutch for kids. Verify all elements / Video playing")
def test_dutch_for_kids_french(driver):
    dutch = FrenchLanding(driver, "https://dinolingo.com/fr/learn-dutch-for-kids")
    dutch.open()
    dutch.dutch_for_kids_verify_elements_fr()

@allure.title("Polish for kids. Verify all elements / Video playing")
def test_polish_for_kids_french(driver):
    polish = FrenchLanding(driver, "https://dinolingo.com/fr/learn-polish-for-kids")
    polish.open()
    polish.polish_for_kids_verify_elements_fr()

@allure.title("Arabic for kids. Verify all elements / Video playing")
def test_arabic_for_kids_french(driver):
    arabic = FrenchLanding(driver, "https://dinolingo.com/fr/learn-arabic-for-kids")
    arabic.open()
    arabic.arabic_for_kids_verify_elements_fr()

@allure.title("Hebrew for kids. Verify all elements / Video playing")
def test_hebrew_for_kids_french(driver):
    hebrew = FrenchLanding(driver, "https://dinolingo.com/fr/learn-hebrew-for-kids")
    hebrew.open()
    hebrew.hebrew_for_kids_verify_elements_fr()

@allure.title("Ukrainian for kids. Verify all elements / Video playing")
def test_ukrainian_for_kids_french(driver):
    language = FrenchLanding(driver, "https://dinolingo.com/fr/learn-ukrainian-for-kids")
    language.open()
    language.ukrainian_for_kids_verify_elements_fr()

@allure.title("Latin for kids. Verify all elements / Video playing")
def test_latin_for_kids_french(driver):
    language = FrenchLanding(driver, "https://dinolingo.com/fr/learn-latin-for-kids")
    language.open()
    language.latin_for_kids_verify_elements_fr()

@allure.title("Korean for kids. Verify all elements / Video playing")
def test_korean_for_kids_french(driver):
    language = FrenchLanding(driver, "https://dinolingo.com/fr/learn-korean-for-kids")
    language.open()
    language.korean_for_kids_verify_elements_fr()

@allure.title("Hindi for kids. Verify all elements / Video playing")
def test_hindi_for_kids_french(driver):
    language = FrenchLanding(driver, "https://dinolingo.com/fr/learn-hindi-for-kids")
    language.open()
    language.hindi_for_kids_verify_elements_fr()

@allure.title("Persian for kids. Verify all elements / Video playing")
def test_persian_for_kids_french(driver):
    language = FrenchLanding(driver, "https://dinolingo.com/fr/learn-persian-for-kids")
    language.open()
    language.persian_for_kids_verify_elements_fr()

@allure.title("Croatian for kids. Verify all elements / Video playing")
def test_croatian_for_kids_french(driver):
    language = FrenchLanding(driver, "https://dinolingo.com/fr/learn-croatian-for-kids")
    language.open()
    language.croatian_for_kids_verify_elements_fr()

@allure.title("Turkish for kids. Verify all elements / Video playing")
def test_turkish_for_kids_french(driver):
    language = FrenchLanding(driver, "https://dinolingo.com/fr/learn-turkish-for-kids")
    language.open()
    language.turkish_for_kids_verify_elements_fr()

@allure.title("All languages. Verify all elements")
def test_all_languages_for_kids_french(driver):
    language = FrenchLanding(driver, "https://dinolingo.com/fr/language-courses")
    language.open()
    language.all_languages_verify_elements_fr()














