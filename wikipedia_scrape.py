from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
driver = webdriver.Chrome()
driver.get(URL)

table = driver.find_element(By.CSS_SELECTOR, "#mw-content-text .mw-parser-output>table:nth-of-type(2)")
rows = table.find_elements(By.TAG_NAME, "tr")

# Initialize an empty list to store rows
data = []

# Iterate through rows and append data to the list
for row in rows:
    row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
    data.append(row_data)

# Close the webdriver
driver.quit()

# Create a DataFrame from the list of rows
df = pd.DataFrame(data)

# Specify the output file name
output_file = 'wiki.csv'

# Save the DataFrame to a CSV file
df.to_csv(output_file, index=False, header=False)

print(f'Data has been saved to {output_file}')

