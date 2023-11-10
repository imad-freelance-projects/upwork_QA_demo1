from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://192.168.43.227"

driver = webdriver.Firefox()
driver.get(url)
username = driver.find_element(By.ID, "txtUsername")
password = driver.find_element(By.ID, "txtPassword")
home_button = driver.find_element(By.ID, "btnLogin")
username.clear()
username.send_keys("admin")
password.clear()
password.send_keys("!1Winner75")
home_button.click()
print(driver.title)
driver.find_element(By.ID, "welcome").click()
welcome_menu = driver.find_element(By.ID, "welcome-menu")
# wait = WebDriverWait(driver, timeout=2)
# wait.until(lambda e: welcome_menu.is_displayed())
# logout = driver.find_element(By.CSS_SELECTOR, "#welcome-menu li:nth-of-type(3)>a")
# driver.find_element(By.CSS_SELECTOR, "#welcome-menu li:nth-of-type(3)>a").click()
# driver.execute_script("arguments[0].scrollIntoView(true);", logout)
# time.sleep(0.5)
# logout.click()
# Checking the main links
# links = driver.find_elements(By.CSS_SELECTOR, "a[id^='menu']")
# for index, item in enumerate(links):
#     if item.text is None or item.text.strip() == "":
#         pass
#     else:
#         print(item.text)

# checking the links on admin main link
# driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
# links = driver.find_elements(By.CSS_SELECTOR, "a[id^='menu']")
# for index, item in enumerate(links):
#     if item.text is None or item.text.strip() == "":
#         pass
#     else:
#         print(item.text)


# checking the links on admin main link
driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
links = driver.find_elements(By.CSS_SELECTOR, "a[id$='viewSystemUsers']")
assert "System Users" in driver.find_element(By.CSS_SELECTOR, "#systemUser-information .head h1").text
if driver.find_element(By.CSS_SELECTOR, "#systemUser-information a").get_attribute("class") == "toggle tiptip":
    driver.find_element(By.CSS_SELECTOR, "#systemUser-information a").click()
    print(driver.find_element(By.CSS_SELECTOR, "#systemUser-information a").get_attribute("class"))
    driver.find_element(By.ID, "searchSystemUser_userName").send_keys("lalasee")
    driver.find_element(By.ID, "searchBtn").click()
    # print(driver.find_element(By.CSS_SELECTOR, "table#resultTable>tbody>tr.odd>td.left>a").text)
    assert "lalasee" in driver.find_element(By.CSS_SELECTOR, "table#resultTable>tbody>tr.odd>td.left>a").text
else:
    print("already activated")
# for index, item in enumerate(links):
#     if item.text is None or item.text.strip() == "":
#         pass
#     else:
#         print(item.text)


# href="/symfony/web/index.php/admin/viewSystemUsers"
driver.close()
