from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


URL = "https://www.selenium.dev/documentation/webdriver/interactions/alerts/"
firefox_drive = webdriver.Firefox()
firefox_drive.get(URL)
firefox_drive.fullscreen_window()


# Alert confirmation
# ==================
# firefox_drive.find_element(By.LINK_TEXT, "See an example alert").click()
# wait = WebDriverWait(firefox_drive, timeout=2)
# alert = wait.until(expected_conditions.alert_is_present())
# text = alert.text
# print(text)
# alert.accept()

# Confirm BOX
# ============
# link_element = firefox_drive.find_element(By.LINK_TEXT, "See a sample confirm")
# ActionChains(firefox_drive).scroll_to_element(link_element).perform()
wait = WebDriverWait(firefox_drive, timeout=4)
sample_link = firefox_drive.find_element(By.LINK_TEXT, "See a sample confirm")
wait.until(expected_conditions.element_to_be_clickable(sample_link))
sample_link.click()
wait.until(expected_conditions.alert_is_present())
alert = firefox_drive.switch_to.alert
print(alert.text)

firefox_drive.quit()
