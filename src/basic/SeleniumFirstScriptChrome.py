'''
Created on Jul 18, 2018

@author: Anil.Kale
'''


from selenium import webdriver

i = 10
print (i)
print("Hello world")
driver = webdriver.Chrome("C:\\Users\\Anil.Kale\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://docs.seleniumhq.org")    
driver.find_element_by_xpath("//a[@title='Selenium Projects']").click();
result = driver.find_element_by_xpath("//a[@title='Selenium Projects']").is_displayed()
print (result)
driver.quit()


