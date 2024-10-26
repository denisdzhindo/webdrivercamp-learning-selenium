import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

# Open eBay watch page and pick Rolex under option Brand on the left
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0")
brand_rolex_filter = driver.find_element(By.XPATH, "//ul[@class='x-refine__left__nav']//input[@class='checkbox__control' and @aria-label='Rolex']")
brand_rolex_filter.click()
titles = driver.find_elements(By.XPATH, "//ul[@class='srp-results srp-grid clearfix']//a[@class='s-item__link']//span[@role='heading']")

# Verify the first two result items contain “rolex” in their title
# old school for practice:)
def brand_in_title(check_, slice_):
 mismatches = []
 count = 0
 for title in slice_:
     title = title.text
     if check_ not in title.lower():
         mismatches.append(title)
         count += 1
 return mismatches, count

test = "rolex"
cut = titles[:2]
result = brand_in_title(test, cut)
if len(result[0]) > 0:
     print(f"Brand {test} is not found in: {result[1]} titles:")
     for index, mismatch in enumerate(result[0]):
         print(index + 1, mismatch)

# Store title and price of the first two results in a variable
prices = driver.find_elements(By.XPATH, "//ul[@class='srp-results srp-grid clearfix']//span[@class='s-item__price']")
title_item_1 = titles[0].text
price_item_1 = float(prices[0].text.replace("$", "").replace(",", ""))
title_item_2 = titles[1].text
price_item_2 = float(prices[1].text.replace("$", "").replace(",", ""))


# Open item in a new tab and verify the title and the price by comparing them with the stored data

titles[0].click() # open the first item tab
driver.switch_to.window(driver.window_handles[1])
title_item_1_page = driver.find_element(By.XPATH, "//h1[@class='x-item-title__mainTitle']").text
price_item_1_page = driver.find_element(By.XPATH, "//div[@class='x-price-primary']/span[@class='ux-textspans']")
price_item_1_page = float(price_item_1_page.text.replace("US $", "").replace(",", ""))
if title_item_1_page != title_item_1:
    print(f"Title on the item page does not match with the main results page: \nMain page title:{title_item_1}\nItem page title:{title_item_1_page}")
if price_item_1_page != price_item_1:
    print(f"Price on the itme page doesn't match with the price on the main results page: \nMain page price:{price_item_1}\nItem page price:{price_item_1_page}")
driver.close()

driver.switch_to.window(driver.window_handles[0])
titles[1].click() # open the second item tab
driver.switch_to.window(driver.window_handles[1])
title_item_2_page = driver.find_element(By.XPATH, "//h1[@class='x-item-title__mainTitle']").text
price_item_2_page = driver.find_element(By.XPATH, "//div[@class='x-price-primary']/span[@class='ux-textspans']")
price_item_2_page = float(price_item_2_page.text.replace("US $", "").replace(",", ""))
if title_item_2_page != title_item_2:
    print(f"Title on the item page does not match with the main results page: \nMain page title:{title_item_2}\nItem page title:{title_item_2_page}")
if price_item_1_page != price_item_1:
    print(f"Price on the itme page doesn't match with the price on the main results page: \nMain page price:{price_item_2}\nItem page price:{price_item_2_page}")
driver.close()

# Uncheck "Rolex" option and check "Casio" option. Verify the last two result items contain "Casio" in their title
driver.switch_to.window(driver.window_handles[0])
brand_rolex_filter = driver.find_element(By.XPATH, "//ul[@class='x-refine__left__nav']//input[@class='checkbox__control' and @aria-label='Rolex']")
brand_rolex_filter.click()
brand_casio_filter = driver.find_element(By.XPATH, "//ul[@class='x-refine__left__nav']//input[@class='checkbox__control' and @aria-label='Casio']")
brand_casio_filter.click()
titles = driver.find_elements(By.XPATH, "//li[@class='s-item s-item__pl-on-bottom' and @data-gr4]//span[@role='heading']")

test = "casio"
cut = titles[-2:]
result = brand_in_title(test, cut)

if len(result[0]) > 0:
     print(f"Brand {test} is not found in: {result[1]} titles:")
     for index, mismatch in enumerate(result[0]):
         print(index + 1, mismatch)






