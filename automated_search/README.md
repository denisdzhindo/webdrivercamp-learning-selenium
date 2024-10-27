Python automation test project: Verify eBay results based on selected options

Framework: Selenium | ChromeDriver   
Implementation: PyCharm  

This project verifies eBay search results when users select a brand option    
It also checks for consistency between eBay's main search results page and individual item pages  

Steps to reproduce:  
Open eBay page https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0   
( Watch for sale | eBay ) and select Rolex in brand filter  
Verify the first two result items contain “Rolex” in their title, then save and print titles without "Rolex"  
Store title and price of the first two results in variables  
Open the two items in new tabs and verify their titles and the prices are the same as the stored data  
Save and print all the mismatches if any
Uncheck “Rolex“ option and check “Casio“ option  
Verify the last two result items contain “Casio“ in their title, then save and print titles without "Casio"  
