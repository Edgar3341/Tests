from main import RussianLanding
import allure


@allure.title("Test open the Website in Russian language ")
def test_open_website_russian(driver):
    checking = RussianLanding(driver, "https://dinolingo.com/ru")
    checking.open()
    checking.verify_elements_on_homepage_ru()

@allure.title("How is works page in Russian language. Verify elements ")
def test_how_it_works_russian(driver):
    checking = RussianLanding(driver, "https://dinolingo.com/ru/how-it-works")
    checking.open()
    checking.how_it_works_verify_element_ru()

@allure.title("Customers Review page in Russian language. Verify elements ")
def test_customer_reviews_russian(driver):
    checking = RussianLanding(driver, "https://dinolingo.com/ru/reviews")
    checking.open()
    checking.customer_reviews_verify_elements_ru()

@allure.title("Language cources page in Russian language. Verify elements ")
def test_language_courses_russian(driver):
    checking = RussianLanding(driver, "https://dinolingo.com/ru/language-courses")
    checking.open()
    checking.language_courses_verify_elements_ru()

@allure.title("Curriculum page in Russian language. Verify elements ")
def test_curriculum_russian(driver):
    checking = RussianLanding(driver, "https://dinolingo.com/ru/curriculum")
    checking.open()
    checking.curriculum_verify_elements_ru()

@allure.title("Parents guide page in Russian language. Verify elements ")
def test_parents_guide_russian(driver):
    checking = RussianLanding(driver, "https://dinolingo.com/ru/parents")
    checking.open()
    checking.parents_guide_verify_elements_ru()


@allure.title("Schools page in Russian language. Verify elements ")
def test_schools_russian(driver):
    checking = RussianLanding(driver, "https://dinolingo.com/ru/schools-teachers")
    checking.open()
    checking.schools_verify_elements_ru()

@allure.title("Homeschoolers page in Russian language. Verify elements ")
def test_homeschoolers_russian(driver):
    checking = RussianLanding(driver, "https://dinolingo.com/ru/homeschool")
    checking.open()
    checking.homeschoolers_verify_elements_ru()


@allure.title("Privacy. Redirect to the new window")
def test_privacy_russian(driver):
    privacy = RussianLanding(driver, "https://dinolingo.com/ru/")
    privacy.open()
    privacy.privacy_verify_redirect_ru()


@allure.title("Terms. Redirect to the new window")
def test_terms_russian(driver):
    terms = RussianLanding(driver, "https://dinolingo.com/ru/")
    terms.open()
    terms.terms_verify_redirect_ru()

@allure.title("Contact us. Redirect to the new window")
def test_contact_us_russian(driver):
    contact_us = RussianLanding(driver, "https://dinolingo.com/ru/")
    contact_us.open()
    contact_us.contact_us_verify_redirect_ru()


@allure.title("About us. Redirect to the new window")
def test_about_us_russian(driver):
    contact_us = RussianLanding(driver, "https://dinolingo.com/ru/about-us")
    contact_us.open()
    contact_us.about_us_verify_elements_ru()

@allure.title("Help and Support. Redirect to the new window")
def test_help_and_support_russian(driver):
    contact_us = RussianLanding(driver, "https://dinolingo.com/ru/")
    contact_us.open()
    contact_us.help_and_support_verify_redirect_ru()



@allure.title("Spanish for kids. Verify all elements / Video playing")
def test_spanish_for_kids_russian(driver):
    spanish = RussianLanding(driver, "https://dinolingo.com/ru/learn-spanish-for-kids")
    spanish.open()
    spanish.spanish_for_kids_verify_elements_ru()


@allure.title("French for kids . Verify all elements / Video playing")
def test_french_for_kids_russian(driver):
    french = RussianLanding(driver, "https://dinolingo.com/ru/learn-french-for-kids")
    french.open()
    french.french_for_kids_verify_elements_ru()


@allure.title("English for kids. Verify all elements / Video playing")
def test_english_for_kids_russian(driver):
    english = RussianLanding(driver, "https://dinolingo.com/ru/learn-english-for-kids")
    english.open()
    english.english_for_kids_verify_elements_ru()

@allure.title("Italian for kids. Verify all elements / Video playing")
def test_italian_for_kids_russian(driver):
    italian = RussianLanding(driver, "https://dinolingo.com/ru/learn-italian-for-kids")
    italian.open()
    italian.italian_for_kids_verify_elements_ru()

@allure.title("German for kids. Verify all elements / Video playing")
def test_german_for_kids_russian(driver):
    german = RussianLanding(driver, "https://dinolingo.com/ru/learn-german-for-kids")
    german.open()
    german.german_for_kids_verify_elements_ru()

@allure.title("Japanese for kids. Verify all elements / Video playing")
def test_japanese_for_kids_russian(driver):
    japanese = RussianLanding(driver, "https://dinolingo.com/ru/learn-japanese-for-kids")
    japanese.open()
    japanese.japanese_for_kids_verify_elements_ru()

@allure.title("European and Brasil Portuguese for kids. Verify all elements / Video playing")
def test_portuguese_for_kids_russian(driver):
    portuguese_eu = RussianLanding(driver, "https://dinolingo.com/ru/learn-portuguese-for-kids")
    portuguese_eu.open()
    portuguese_eu.portuguese_eu_for_kids_verify_elements_ru()


@allure.title("Russian for kids. Verify all elements / Video playing")
def test_russian_for_kids_russian(driver):
    russian = RussianLanding(driver, "https://dinolingo.com/ru/learn-russian-for-kids")
    russian.open()
    russian.russian_for_kids_verify_elements_ru()

@allure.title("Chinese for kids. Verify all elements / Video playing")
def test_chinese_for_kids_russian(driver):
    chinese = RussianLanding(driver, "https://dinolingo.com/ru/learn-chinese-for-kids")
    chinese.open()
    chinese.chinese_for_kids_verify_elements_ru()

@allure.title("Greek for kids. Verify all elements / Video playing")
def test_greek_for_kids_russian(driver):
    greek = RussianLanding(driver, "https://dinolingo.com/ru/learn-greek-for-kids")
    greek.open()
    greek.greek_for_kids_verify_elements_ru()

@allure.title("Swedish for kids. Verify all elements / Video playing")
def test_swedish_for_kids_russian(driver):
    swedish = RussianLanding(driver, "https://dinolingo.com/ru/learn-swedish-for-kids")
    swedish.open()
    swedish.swedish_for_kids_verify_elements_ru()

@allure.title("Dutch for kids. Verify all elements / Video playing")
def test_dutch_for_kids_russian(driver):
    dutch = RussianLanding(driver, "https://dinolingo.com/ru/learn-dutch-for-kids")
    dutch.open()
    dutch.dutch_for_kids_verify_elements_ru()

@allure.title("Polish for kids. Verify all elements / Video playing")
def test_polish_for_kids_russian(driver):
    polish = RussianLanding(driver, "https://dinolingo.com/ru/learn-polish-for-kids")
    polish.open()
    polish.polish_for_kids_verify_elements_ru()

@allure.title("Arabic for kids. Verify all elements / Video playing")
def test_arabic_for_kids_russian(driver):
    arabic = RussianLanding(driver, "https://dinolingo.com/ru/learn-arabic-for-kids")
    arabic.open()
    arabic.arabic_for_kids_verify_elements_ru()

@allure.title("Hebrew for kids. Verify all elements / Video playing")
def test_hebrew_for_kids_russian(driver):
    hebrew = RussianLanding(driver, "https://dinolingo.com/ru/learn-hebrew-for-kids")
    hebrew.open()
    hebrew.hebrew_for_kids_verify_elements_ru()

@allure.title("Ukrainian for kids. Verify all elements / Video playing")
def test_ukrainian_for_kids_russian(driver):
    language = RussianLanding(driver, "https://dinolingo.com/ru/learn-ukrainian-for-kids")
    language.open()
    language.ukrainian_for_kids_verify_elements_ru()

@allure.title("Latin for kids. Verify all elements / Video playing")
def test_latin_for_kids_russian(driver):
    language = RussianLanding(driver, "https://dinolingo.com/ru/learn-latin-for-kids")
    language.open()
    language.latin_for_kids_verify_elements_ru()

@allure.title("Korean for kids. Verify all elements / Video playing")
def test_korean_for_kids_russian(driver):
    language = RussianLanding(driver, "https://dinolingo.com/ru/learn-korean-for-kids")
    language.open()
    language.korean_for_kids_verify_elements_ru()

@allure.title("Hindi for kids. Verify all elements / Video playing")
def test_hindi_for_kids_russian(driver):
    language = RussianLanding(driver, "https://dinolingo.com/ru/learn-hindi-for-kids")
    language.open()
    language.hindi_for_kids_verify_elements_ru()

@allure.title("Persian for kids. Verify all elements / Video playing")
def test_persian_for_kids_russian(driver):
    language = RussianLanding(driver, "https://dinolingo.com/ru/learn-persian-for-kids")
    language.open()
    language.persian_for_kids_verify_elements_ru()

@allure.title("Croatian for kids. Verify all elements / Video playing")
def test_croatian_for_kids_russian(driver):
    language = RussianLanding(driver, "https://dinolingo.com/ru/learn-croatian-for-kids")
    language.open()
    language.croatian_for_kids_verify_elements_ru()

@allure.title("Turkish for kids. Verify all elements / Video playing")
def test_turkish_for_kids_russian(driver):
    language = RussianLanding(driver, "https://dinolingo.com/ru/learn-turkish-for-kids")
    language.open()
    language.turkish_for_kids_verify_elements_ru()

@allure.title("All languages. Verify all elements")
def test_all_languages_for_kids_russian(driver):
    language = RussianLanding(driver, "https://dinolingo.com/ru/language-courses")
    language.open()
    language.all_languages_verify_elements_ru()










