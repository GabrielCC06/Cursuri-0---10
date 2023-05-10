from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Selectors():
    chrome = webdriver.Chrome(ChromeDriverManager().install())

# creeam constante in functie de selectorii pe care o sa ii folosim
# creeam o constanta pe care o vom numi
    INPUT_FIRST_NAME = (By.ID, 'first-name')
    INPUT_LAST_NAME = (By.CLASS_NAME, 'form-control')
    RADIO_BUTTON_1 = (By.CSS_SELECTOR, 'input#radio-button-1')
    RADIO_BUTTON_2 = (By.CSS_SELECTOR, 'input#radio-button-2')
    RADIO_BUTTON_3 = (By.CSS_SELECTOR, 'input#radio-button-3')
    AUTOCOMPLETE_LINK_TEXT = (By.LINK_TEXT, 'Autocomplete')
    ENABLED_DISABLED_LINK_TEXT = (By.PARTIAL_LINK_TEXT, 'Enabled')
    INPUT_FIRST_NAME_BY_XPATH = (By.XPATH, "//input[@id='first-name']")

    def __init__(self):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        self.chrome.maximize_window()

    def first_name_field(self, first_name):
        first_name_text_field = self.chrome.find_element(*self.INPUT_FIRST_NAME)# first_name_text_field va fi elementull de pe pagina cu  Id-ul first-name
        first_name_text_field.send_keys(first_name)

    def last_name_field(self, last_name):
        last_name_text_field = self.chrome.find_elements(*self.INPUT_LAST_NAME) # pentru a returna toate elementele cu acelasi ID(class name/tag) trebuie apelat find elements adica la plural
        last_name_text_field[1].send_keys(last_name)

    def click_radio_button(self, number):
        if number == 1:
            self.chrome.find_element(*self.RADIO_BUTTON_1).click()
        elif number == 2:
            self.chrome.find_element(*self.RADIO_BUTTON_2).click()
        elif number == 3:
            self.chrome.find_element(*self.RADIO_BUTTON_3).click()
        else:
            self.chrome.find_element(*self.RADIO_BUTTON_1).click()
            self.chrome.find_element(*self.RADIO_BUTTON_2).click()
            self.chrome.find_element(*self.RADIO_BUTTON_3).click()

    def click_autocomplete(self):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        self.chrome.find_element(*self.AUTOCOMPLETE_LINK_TEXT).click()

    def click_enabled_disabled(self):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        self.chrome.find_element(*self.ENABLED_DISABLED_LINK_TEXT).click()

    # def click_high_school_button(self):
    #     self.chrome.find_element(*self.RADIO_BUTTON_1).click()
    #
    # def click_high_school_button(self):
    #     self.chrome.find_element(*self.RADIO_BUTTON_2).click()
    #
    # def click_high_school_button(self):
    #     self.chrome.find_element(*self.RADIO_BUTTON_3).click()


selector = Selectors()
selector.first_name_field('Gabriel')
selector.last_name_field('Curcuta')
selector.click_radio_button(3)
selector.click_autocomplete()
sleep(2)
selector.click_enabled_disabled()
sleep(5)

# Acum vom da click pe unul din butoane dupa CSS si anume butonul High School

