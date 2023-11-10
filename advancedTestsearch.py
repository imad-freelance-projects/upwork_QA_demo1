import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://192.168.43.227"


class TestAll:
    @pytest.fixture(scope="module")
    def browser(self):
        driver = webdriver.Firefox()
        yield driver
        driver.quit()

    @pytest.fixture
    def login(self, browser):
        browser.get(url)
        yield browser

    def test_first_search(self, login):
        username = login.find_element(By.ID, "txtUsername")
        password = login.find_element(By.ID, "txtPassword")
        home_button = login.find_element(By.ID, "btnLogin")
        username.clear()
        username.send_keys("admin")
        password.clear()
        password.send_keys("!1Winner75")
        home_button.click()
        print(login.title)
        login.find_element(By.ID, "welcome").click()
        welcome_menu = login.find_element(By.ID, "welcome-menu")
        # wait = WebDriverWait(driver, timeout=2)
        # wait.until(lambda e: welcome_menu.is_displayed())
        # logout = driver.find_element(By.CSS_SELECTOR, "#welcome-menu li:nth-of-type(3)>a")
        login.find_element(By.CSS_SELECTOR, "#welcome-menu li:nth-of-type(3)>a").click()

    def test_advanced_search(self, login):
        username = login.find_element(By.ID, "txtUsername")
        password = login.find_element(By.ID, "txtPassword")
        home_button = login.find_element(By.ID, "btnLogin")
        username.clear()
        username.send_keys("admin")
        password.clear()
        password.send_keys("!1Winner75")
        home_button.click()
        print(login.title)
        login.find_element(By.ID, "welcome").click()
        # welcome_menu = driver.find_element(By.ID, "welcome-menu")
        login.find_element(By.CSS_SELECTOR, "#welcome-menu li:nth-of-type(1)>a")
        about = login.find_element(By.CSS_SELECTOR, "#companyInfo li:nth-of-type(1) p")
        print("about text is " + about.text)
        login.find_element(By.CSS_SELECTOR, "#welcome-menu li:nth-of-type(3)>a").click()

# def test_execute():
#     d = AllTest()
#     d.test_first_search()
#     d.test_advanced_search()
