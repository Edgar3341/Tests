from main import PortugueseLanding
import allure


@allure.title("Test open the Website in Portuguese language ")
def test_open_website_portuguese(driver):
    checking = PortugueseLanding(driver, "https://dinolingo.com/pt")
    checking.open()
    checking.verify_elements_on_homepage_pt()

@allure.title("How is works page in Portuguese language. Verify elements ")
def test_how_it_works_portuguese(driver):
    checking = PortugueseLanding(driver, "https://dinolingo.com/pt/how-it-works")
    checking.open()
    checking.how_it_works_verify_element_pt()

@allure.title("Customers Review page in Portuguese language. Verify elements ")
def test_customer_reviews_portuguese(driver):
    checking = PortugueseLanding(driver, "https://dinolingo.com/pt/reviews")
    checking.open()
    checking.customer_reviews_verify_elements_pt()

@allure.title("Language cources page in Portuguese language. Verify elements ")
def test_language_courses_portuguese(driver):
    checking = PortugueseLanding(driver, "https://dinolingo.com/pt/language-courses")
    checking.open()
    checking.language_courses_verify_elements_pt()

@allure.title("Curriculum page in Portuguese language. Verify elements ")
def test_curriculum_portuguese(driver):
    checking = PortugueseLanding(driver, "https://dinolingo.com/pt/curriculum")
    checking.open()
    checking.curriculum_verify_elements_pt()

@allure.title("Parents guide page in Portuguese language. Verify elements ")
def test_parents_guide_portuguese(driver):
    checking = PortugueseLanding(driver, "https://dinolingo.com/pt/parents")
    checking.open()
    checking.parents_guide_verify_elements_pt()


@allure.title("Schools page in Portuguese language. Verify elements ")
def test_schools_portuguese(driver):
    checking = PortugueseLanding(driver, "https://dinolingo.com/pt/schools-teachers")
    checking.open()
    checking.schools_verify_elements_pt()

@allure.title("Homeschoolers page in Portuguese language. Verify elements ")
def test_homeschoolers_portuguese(driver):
    checking = PortugueseLanding(driver, "https://dinolingo.com/pt/homeschool")
    checking.open()
    checking.homeschoolers_verify_elements_pt()


@allure.title("Privacy. Redirect to the new window")
def test_privacy_portuguese(driver):
    privacy = PortugueseLanding(driver, "https://dinolingo.com/pt/")
    privacy.open()
    privacy.privacy_verify_redirect_pt()


@allure.title("Terms. Redirect to the new window")
def test_terms_portuguese(driver):
    terms = PortugueseLanding(driver, "https://dinolingo.com/pt/")
    terms.open()
    terms.terms_verify_redirect_pt()

@allure.title("Contact us. Redirect to the new window")
def test_contact_us_portuguese(driver):
    contact_us = PortugueseLanding(driver, "https://dinolingo.com/pt/")
    contact_us.open()
    contact_us.contact_us_verify_redirect_pt()


@allure.title("About us. Redirect to the new window")
def test_about_us_portuguese(driver):
    contact_us = PortugueseLanding(driver, "https://dinolingo.com/pt/about-us")
    contact_us.open()
    contact_us.about_us_verify_elements_pt()

@allure.title("Help and Support. Redirect to the new window")
def test_help_and_support_portuguese(driver):
    contact_us = PortugueseLanding(driver, "https://dinolingo.com/pt/")
    contact_us.open()
    contact_us.help_and_support_verify_redirect_pt()



@allure.title("Spanish for kids. Verify all elements / Video playing")
def test_spanish_for_kids_portuguese(driver):
    spanish = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-spanish-for-kids")
    spanish.open()
    spanish.spanish_for_kids_verify_elements_pt()


@allure.title("French for kids . Verify all elements / Video playing")
def test_french_for_kids_portuguese(driver):
    french = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-french-for-kids")
    french.open()
    french.french_for_kids_verify_elements_pt()


@allure.title("English for kids. Verify all elements / Video playing")
def test_english_for_kids_portuguese(driver):
    english = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-english-for-kids")
    english.open()
    english.english_for_kids_verify_elements_pt()

@allure.title("Italian for kids. Verify all elements / Video playing")
def test_italian_for_kids_portuguese(driver):
    italian = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-italian-for-kids")
    italian.open()
    italian.italian_for_kids_verify_elements_pt()

@allure.title("German for kids. Verify all elements / Video playing")
def test_german_for_kids_portuguese(driver):
    german = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-german-for-kids")
    german.open()
    german.german_for_kids_verify_elements_pt()

@allure.title("Japanese for kids. Verify all elements / Video playing")
def test_japanese_for_kids_portuguese(driver):
    japanese = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-japanese-for-kids")
    japanese.open()
    japanese.japanese_for_kids_verify_elements_pt()

@allure.title("European and Brasil Portuguese for kids. Verify all elements / Video playing")
def test_portuguese_for_kids_portuguese(driver):
    portuguese_eu = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-portuguese-for-kids")
    portuguese_eu.open()
    portuguese_eu.portuguese_eu_for_kids_verify_elements_pt()


@allure.title("Russian for kids. Verify all elements / Video playing")
def test_russian_for_kids_portuguese(driver):
    russian = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-russian-for-kids")
    russian.open()
    russian.russian_for_kids_verify_elements_pt()

@allure.title("Chinese for kids. Verify all elements / Video playing")
def test_chinese_for_kids_portuguese(driver):
    chinese = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-chinese-for-kids")
    chinese.open()
    chinese.chinese_for_kids_verify_elements_pt()

@allure.title("Greek for kids. Verify all elements / Video playing")
def test_greek_for_kids_portuguese(driver):
    greek = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-greek-for-kids")
    greek.open()
    greek.greek_for_kids_verify_elements_pt()

@allure.title("Swedish for kids. Verify all elements / Video playing")
def test_swedish_for_kids_portuguese(driver):
    swedish = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-swedish-for-kids")
    swedish.open()
    swedish.swedish_for_kids_verify_elements_pt()

@allure.title("Dutch for kids. Verify all elements / Video playing")
def test_dutch_for_kids_portuguese(driver):
    dutch = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-dutch-for-kids")
    dutch.open()
    dutch.dutch_for_kids_verify_elements_pt()

@allure.title("Polish for kids. Verify all elements / Video playing")
def test_polish_for_kids_portuguese(driver):
    polish = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-polish-for-kids")
    polish.open()
    polish.polish_for_kids_verify_elements_pt()

@allure.title("Arabic for kids. Verify all elements / Video playing")
def test_arabic_for_kids_portuguese(driver):
    arabic = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-arabic-for-kids")
    arabic.open()
    arabic.arabic_for_kids_verify_elements_pt()

@allure.title("Hebrew for kids. Verify all elements / Video playing")
def test_hebrew_for_kids_german(driver):
    hebrew = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-hebrew-for-kids")
    hebrew.open()
    hebrew.hebrew_for_kids_verify_elements_pt()

@allure.title("Ukrainian for kids. Verify all elements / Video playing")
def test_ukrainian_for_kids_portuguese(driver):
    language = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-ukrainian-for-kids")
    language.open()
    language.ukrainian_for_kids_verify_elements_pt()

@allure.title("Latin for kids. Verify all elements / Video playing")
def test_latin_for_kids_portuguese(driver):
    language = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-latin-for-kids")
    language.open()
    language.latin_for_kids_verify_elements_pt()

@allure.title("Korean for kids. Verify all elements / Video playing")
def test_korean_for_kids_portuguese(driver):
    language = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-korean-for-kids")
    language.open()
    language.korean_for_kids_verify_elements_pt()

@allure.title("Hindi for kids. Verify all elements / Video playing")
def test_hindi_for_kids_portuguese(driver):
    language = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-hindi-for-kids")
    language.open()
    language.hindi_for_kids_verify_elements_pt()

@allure.title("Persian for kids. Verify all elements / Video playing")
def test_persian_for_kids_portuguese(driver):
    language = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-persian-for-kids")
    language.open()
    language.persian_for_kids_verify_elements_pt()

@allure.title("Croatian for kids. Verify all elements / Video playing")
def test_croatian_for_kids_portuguese(driver):
    language = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-croatian-for-kids")
    language.open()
    language.croatian_for_kids_verify_elements_pt()

@allure.title("Turkish for kids. Verify all elements / Video playing")
def test_turkish_for_kids_portuguese(driver):
    language = PortugueseLanding(driver, "https://dinolingo.com/pt/learn-turkish-for-kids")
    language.open()
    language.turkish_for_kids_verify_elements_pt()

@allure.title("All languages. Verify all elements")
def test_all_languages_for_kids_portuguese(driver):
    language = PortugueseLanding(driver, "https://dinolingo.com/pt/language-courses")
    language.open()
    language.all_languages_verify_elements_pt()














