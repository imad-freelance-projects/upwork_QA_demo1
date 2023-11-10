import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSetup:
    @pytest.fixture(scope="module")
    def browser(self):
        driver = webdriver.Firefox()
        yield driver
        driver.quit()

    @pytest.fixture
    def logged_in_browser(self, browser):
        browser.get("http://192.168.43.227")  # Replace with your URL
        # Perform login steps if needed
        yield browser
        # Additional teardown specific to this fixture, if needed

    def test_for_links(self, logged_in_browser):
        username = logged_in_browser.find_element(By.ID, "txtUsername")
        password = logged_in_browser.find_element(By.ID, "txtPassword")
        home_button = logged_in_browser.find_element(By.ID, "btnLogin")
        username.clear()
        username.send_keys("admin")
        password.clear()
        password.send_keys("!1Winner75")
        home_button.click()
        links = logged_in_browser.find_elements(By.CSS_SELECTOR, "a[id^='menu']")
        # Attach the links information as a file to the Allure report
        print(links)