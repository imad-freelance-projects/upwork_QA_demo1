from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://the-internet.herokuapp.com/"
driver = webdriver.Firefox()
driver.get(URL)

#  Question 1. A/B Testing
# TEXT = "Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through)."
# # A/B Testing
# driver.find_element(By.CSS_SELECTOR, "a[href='/abtest']").click()
# # print(driver.find_element(By.CSS_SELECTOR, "#content .example p").text)
# assert TEXT in driver.find_element(By.CSS_SELECTOR, "#content .example p").text

# Question 2: Add/Remove Element
# driver.find_element(By.CSS_SELECTOR, "a[href='/add_remove_elements/']").click()
# if driver.find_element(By.CSS_SELECTOR, "#elements .added-manually").is_displayed()
#     driver.find_element(By.CSS_SELECTOR, "#elements .added-manually").click()
#     print("button disabled")
# else:

# try:
#     print(driver.find_element(By.CSS_SELECTOR, "#elements .added-manually").text)
#     driver.find_element(By.CSS_SELECTOR, "#elements .added-manually").click()
#     print("button disabled")
# except:
#     driver.find_element(By.CSS_SELECTOR, "#content .example button").click()
#     print("Just added a button")
#     delete_button = driver.find_element(By.CSS_SELECTOR, "#elements .added-manually")
#     wait = WebDriverWait(driver, timeout=2)
#     wait.until(lambda e: delete_button.is_displayed())
#     if driver.find_element(By.CSS_SELECTOR, "#elements .added-manually").is_displayed():
#         driver.find_element(By.CSS_SELECTOR, "#elements .added-manually").click()
#         print("button disabled")
#     else:
#         print("error")
# finally:
#     pass

#  Question 3: Basic Auth
driver.find_element(By.CSS_SELECTOR, "a[href='/basic_auth']").click()
print(driver.window_handles.__len__())
# print(driver.find_elements(By.TAG_NAME, "iframe"))
driver.quit()
