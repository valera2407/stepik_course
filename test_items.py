import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_busket_button_has_different_language(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button.is_displayed()
