from main import ItalianLanding
import allure


@allure.title("Test open the Website in Italian language ")
def test_open_website_italian(driver):
    checking = ItalianLanding(driver, "https://dinolingo.com/it")
    checking.open()
    checking.verify_elements_on_homepage_it()

@allure.title("How is works page in Italian language. Verify elements ")
def test_how_it_works_italian(driver):
    checking = ItalianLanding(driver, "https://dinolingo.com/it/how-it-works")
    checking.open()
    checking.how_it_works_verify_element_it()

@allure.title("Customers Review page in Italian language. Verify elements ")
def test_customer_reviews_italian(driver):
    checking = ItalianLanding(driver, "https://dinolingo.com/it/reviews")
    checking.open()
    checking.customer_reviews_verify_elements_it()

@allure.title("Language cources page in Italian language. Verify elements ")
def test_language_courses_italian(driver):
    checking = ItalianLanding(driver, "https://dinolingo.com/it/language-courses")
    checking.open()
    checking.language_courses_verify_elements_it()

@allure.title("Curriculum page in Italian language. Verify elements ")
def test_curriculum_italian(driver):
    checking = ItalianLanding(driver, "https://dinolingo.com/it/curriculum")
    checking.open()
    checking.curriculum_verify_elements_it()

@allure.title("Parents guide page in Italian language. Verify elements ")
def test_parents_guide_italian(driver):
    checking = ItalianLanding(driver, "https://dinolingo.com/it/parents")
    checking.open()
    checking.parents_guide_verify_elements_it()


@allure.title("Schools page in Italian language. Verify elements ")
def test_schools_italian(driver):
    checking = ItalianLanding(driver, "https://dinolingo.com/it/schools-teachers")
    checking.open()
    checking.schools_verify_elements_it()

@allure.title("Homeschoolers page in Italian language. Verify elements ")
def test_homeschoolers_italian(driver):
    checking = ItalianLanding(driver, "https://dinolingo.com/it/homeschool")
    checking.open()
    checking.homeschoolers_verify_elements_it()


@allure.title("Privacy. Redirect to the new window")
def test_privacy_italian(driver):
    privacy = ItalianLanding(driver, "https://dinolingo.com/it/")
    privacy.open()
    privacy.privacy_verify_redirect_it()


@allure.title("Terms. Redirect to the new window")
def test_terms_italian(driver):
    terms = ItalianLanding(driver, "https://dinolingo.com/it/")
    terms.open()
    terms.terms_verify_redirect_it()

@allure.title("Contact us. Redirect to the new window")
def test_contact_us_italian(driver):
    contact_us = ItalianLanding(driver, "https://dinolingo.com/it/")
    contact_us.open()
    contact_us.contact_us_verify_redirect_it()


@allure.title("About us. Redirect to the new window")
def test_about_us_italian(driver):
    contact_us = ItalianLanding(driver, "https://dinolingo.com/it/about-us")
    contact_us.open()
    contact_us.about_us_verify_elements_it()

@allure.title("Help and Support. Redirect to the new window")
def test_help_and_support_italian(driver):
    contact_us = ItalianLanding(driver, "https://dinolingo.com/it/")
    contact_us.open()
    contact_us.help_and_support_verify_redirect_it()



@allure.title("Spanish for kids. Verify all elements / Video playing")
def test_spanish_for_kids_italian(driver):
    spanish = ItalianLanding(driver, "https://dinolingo.com/it/learn-spanish-for-kids")
    spanish.open()
    spanish.spanish_for_kids_verify_elements_it()


@allure.title("French for kids . Verify all elements / Video playing")
def test_french_for_kids_italian(driver):
    french = ItalianLanding(driver, "https://dinolingo.com/it/learn-french-for-kids")
    french.open()
    french.french_for_kids_verify_elements_it()


@allure.title("English for kids. Verify all elements / Video playing")
def test_english_for_kids_italian(driver):
    english = ItalianLanding(driver, "https://dinolingo.com/it/learn-english-for-kids")
    english.open()
    english.english_for_kids_verify_elements_it()

@allure.title("Italian for kids. Verify all elements / Video playing")
def test_italian_for_kids_italian(driver):
    italian = ItalianLanding(driver, "https://dinolingo.com/it/learn-italian-for-kids")
    italian.open()
    italian.italian_for_kids_verify_elements_it()

@allure.title("German for kids. Verify all elements / Video playing")
def test_german_for_kids_italian(driver):
    german = ItalianLanding(driver, "https://dinolingo.com/it/learn-german-for-kids")
    german.open()
    german.german_for_kids_verify_elements_it()

@allure.title("Japanese for kids. Verify all elements / Video playing")
def test_japanese_for_kids_italian(driver):
    japanese = ItalianLanding(driver, "https://dinolingo.com/it/learn-japanese-for-kids")
    japanese.open()
    japanese.japanese_for_kids_verify_elements_it()

@allure.title("European and Brasil Portuguese for kids. Verify all elements / Video playing")
def test_portuguese_for_kids_italian(driver):
    portuguese_eu = ItalianLanding(driver, "https://dinolingo.com/it/learn-euportuguese-for-kids")
    portuguese_eu.open()
    portuguese_eu.portuguese_eu_for_kids_verify_elements_it()


@allure.title("Russian for kids. Verify all elements / Video playing")
def test_russian_for_kids_italian(driver):
    russian = ItalianLanding(driver, "https://dinolingo.com/it/learn-russian-for-kids")
    russian.open()
    russian.russian_for_kids_verify_elements_it()

@allure.title("Chinese for kids. Verify all elements / Video playing")
def test_chinese_for_kids_italian(driver):
    chinese = ItalianLanding(driver, "https://dinolingo.com/it/learn-chinese-for-kids")
    chinese.open()
    chinese.chinese_for_kids_verify_elements_it()

@allure.title("Greek for kids. Verify all elements / Video playing")
def test_greek_for_kids_italian(driver):
    greek = ItalianLanding(driver, "https://dinolingo.com/it/learn-greek-for-kids")
    greek.open()
    greek.greek_for_kids_verify_elements_it()

@allure.title("Swedish for kids. Verify all elements / Video playing")
def test_swedish_for_kids_italian(driver):
    swedish = ItalianLanding(driver, "https://dinolingo.com/it/learn-swedish-for-kids")
    swedish.open()
    swedish.swedish_for_kids_verify_elements_it()

@allure.title("Dutch for kids. Verify all elements / Video playing")
def test_dutch_for_kids_italian(driver):
    dutch = ItalianLanding(driver, "https://dinolingo.com/it/learn-dutch-for-kids")
    dutch.open()
    dutch.dutch_for_kids_verify_elements_it()

@allure.title("Polish for kids. Verify all elements / Video playing")
def test_polish_for_kids_italian(driver):
    polish = ItalianLanding(driver, "https://dinolingo.com/it/learn-polish-for-kids")
    polish.open()
    polish.polish_for_kids_verify_elements_it()

@allure.title("Arabic for kids. Verify all elements / Video playing")
def test_arabic_for_kids_italian(driver):
    arabic = ItalianLanding(driver, "https://dinolingo.com/it/learn-arabic-for-kids")
    arabic.open()
    arabic.arabic_for_kids_verify_elements_it()

@allure.title("Hebrew for kids. Verify all elements / Video playing")
def test_hebrew_for_kids_italian(driver):
    hebrew = ItalianLanding(driver, "https://dinolingo.com/it/learn-hebrew-for-kids")
    hebrew.open()
    hebrew.hebrew_for_kids_verify_elements_it()

@allure.title("Ukrainian for kids. Verify all elements / Video playing")
def test_ukrainian_for_kids_italian(driver):
    language = ItalianLanding(driver, "https://dinolingo.com/it/learn-ukrainian-for-kids")
    language.open()
    language.ukrainian_for_kids_verify_elements_it()

@allure.title("Latin for kids. Verify all elements / Video playing")
def test_latin_for_kids_italian(driver):
    language = ItalianLanding(driver, "https://dinolingo.com/it/learn-latin-for-kids")
    language.open()
    language.latin_for_kids_verify_elements_it()

@allure.title("Korean for kids. Verify all elements / Video playing")
def test_korean_for_kids_italian(driver):
    language = ItalianLanding(driver, "https://dinolingo.com/it/learn-korean-for-kids")
    language.open()
    language.korean_for_kids_verify_elements_it()

@allure.title("Hindi for kids. Verify all elements / Video playing")
def test_hindi_for_kids_italian(driver):
    language = ItalianLanding(driver, "https://dinolingo.com/it/learn-hindi-for-kids")
    language.open()
    language.hindi_for_kids_verify_elements_it()

@allure.title("Persian for kids. Verify all elements / Video playing")
def test_persian_for_kids_italian(driver):
    language = ItalianLanding(driver, "https://dinolingo.com/it/learn-persian-for-kids")
    language.open()
    language.persian_for_kids_verify_elements_it()

@allure.title("Croatian for kids. Verify all elements / Video playing")
def test_croatian_for_kids_italian(driver):
    language = ItalianLanding(driver, "https://dinolingo.com/it/learn-croatian-for-kids")
    language.open()
    language.croatian_for_kids_verify_elements_it()

@allure.title("Turkish for kids. Verify all elements / Video playing")
def test_turkish_for_kids_italian(driver):
    language = ItalianLanding(driver, "https://dinolingo.com/it/learn-turkish-for-kids")
    language.open()
    language.turkish_for_kids_verify_elements_it()

@allure.title("All languages. Verify all elements")
def test_all_languages_for_kids_italian(driver):
    language = ItalianLanding(driver, "https://dinolingo.com/it/language-courses")
    language.open()
    language.all_languages_verify_elements_it()














