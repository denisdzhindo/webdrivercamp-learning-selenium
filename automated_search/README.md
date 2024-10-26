Python Automation project: Verification Select option on Ebay results
Framework: Selenium | ChromeDriver   
Implementation: Pycharm  

This project verifies results of selecting Brand option on the main Ebay page.  
User upens www.ebay.com website and looking for watches. Than they choose Rolex brand.  
Steps to reproduce:  
Open eBay watch page https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0   
( Watch for sale | eBay ) and select option Brand / Rolex in Filter pane  
Verify the first two result items contain “rolex” in their title  
Store title and price of the first two results in a variable  
Open item in a new tab and verify the title and the price by comparing them with the stored data  
Uncheck “Rolex“ option and check “Casio“ option  
Verify the last two result items contain “Casio“ in their title  
Save and print all the mismatches if any  
