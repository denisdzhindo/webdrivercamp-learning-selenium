import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import support
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

driver = webdriver.Chrome()

# 1. Open Browser: Navigate to URL ( www.ebay.com ), Print URL Close browser:
'''driver.get('https://www.ebay.com')
print(driver.current_url)
driver.close()'''

# 2. Add wait: Navigate to URL ( www.ebay.com ), WebDriverWait, Print URL, Close browser
'''driver.get('https://www.ebay.com')
wait = WebDriverWait(driver, 15)
element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//header[@class='gh-ui-6-5 gh-w gh-sch-prom ghx-evoa gh-simpleH']//td[@class='gh-td'][h1]")))
print(driver.current_url)
driver.close()'''

# 3. Search items:Navigate to URL ( www.ebay.com ), WebDriverWait - Waiting for the page to load
# Print URL, Type “women watch” into search field, Press search, Close browser
'''driver.get('https://www.ebay.com')
wait = WebDriverWait(driver, 15)
element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//header[@class='gh-ui-6-5 gh-w gh-sch-prom ghx-evoa gh-simpleH']//td[@class='gh-td'][h1]")))
print(driver.current_url)
search_field = driver.find_element(By.XPATH, "//table[@class='gh-tbl2']//input[@class='gh-tb ui-autocomplete-input']")
search_field.send_keys("women watch")
search_button = driver.find_element(By.XPATH, "//input[@class='btn btn-prim gh-spr']")
search_button.click()
sleep(3)
driver.close()'''

# 4. Verify the search results:
# Navigate to URL ( www.ebay.com )
# WebDriverWait -  Waiting for the page to load
# Print URL
# Type “women watch” into search field
# Press search
# Verify the header contains "results for women watch"
# Close browser

driver.get('https://www.ebay.com')
wait = WebDriverWait(driver, 15)
element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//header[@class='gh-ui-6-5 gh-w gh-sch-prom ghx-evoa gh-simpleH']//td[@class='gh-td']//h1")))
print(driver.current_url)
search_field = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
search_field.send_keys("women watch")
search_button = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
search_button.click()
sleep(3)


# items = driver.find_elements(By.XPATH,"//li[@class='s-item s-item__pl-on-bottom' and @data-gr4]//span[@role='heading' and contains(text(), \"Women's\") and contains(text(),'Watch')]")

items = driver.find_elements(By.XPATH,"//li[@class='s-item s-item__pl-on-bottom' and @data-gr4]//span[@role='heading']")

item_title = "women"

mismatches = []
count = 0
for item in items:
    title = item.text.lower()
    if item_title not in title:
        mismatches.append(title)

for i,mismatch in enumerate(mismatches):
    print(i + 1, mismatch)

driver.close()










