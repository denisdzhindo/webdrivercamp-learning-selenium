import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

# Open eBay watch page ( Watch for sale | eBay ) and select option Brand / Rolex in Filter pane
# Verify the first two result items contain “rolex” in their title
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0")




sleep(3)



