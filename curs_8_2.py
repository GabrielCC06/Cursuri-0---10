from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Selectors():
    chrome = webdriver.Chrome(ChromeDriverManager().install())

# cream constante in functie de slectorii pe care o sa-i folosim

    INPUT_FIRST_NAME = (By.ID, 'first-name')
    def __init__(self):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        self.chrome.maximize_window()

    def first_name_field(self, first_name):
        first_name_text_field = self.chrome.find_element(*self.INPUT_FIRST_NAME) # first_name_text_field va fi elem de pe pag cu Id-ul first_name
        first_name_text_field.send_keys(first_name)

selector = Selectors()
selector.first_name_field('Ciprian')
sleep(5)


