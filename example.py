import time
from selenium import webdriver
import unittest


class Test(unittest.TestCase):
 def testName(self):
    browser = webdriver.Chrome("c:\chromedriver.exe")
    browser.get("https://www.google.com")
    browser.maximize_window()
    search_box = browser.find_element_by_xpath("//input[contains(@class,'gLFyf gsfi')]")
    search_box.send_keys("selenium tutorial")
    search_box.submit()

    for i in range(10):
        links = browser.find_elements_by_xpath("//div[@class='r']//h3".replace('0', 'i'))
        if i <6:
         links[i].click()
         print(browser.current_url)
         time.sleep(5)
         browser.back()
         time.sleep(10)
         i += 1

    # for i in range(10):
    #      print(i)
    #      if i == 0:
    #       links[i].click()
    #       time.sleep(50)
    #       browser.current_url.__contains__("https://www.guru99.com/selenium-tutorial.html")
    #       time.sleep(5)
    #       print(browser.current_url)
    #       browser.back()
    #      elif i == 1:
    #       links[i].click()
    #       browser.current_url.__contains__("https://www.guru99.com/selenium-tutorial.html")
    #       browser.back()
    #       time.sleep(5)
    #      elif i == 3:
    #       links[i].click()
    #       browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #       time.sleep(5)
    #       browser.current_url.__contains__("https://www.javatpoint.com/selenium-tutorial")
    #       print("pass3")
    #       browser.back()
    #      elif i == 4:
    #       links[i].click()
    #       browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #       time.sleep(5)
    #       browser.current_url.__contains__("https://intellipaat.com/blog/tutorial/selenium-tutorial/")
    #       print("pass4")
    #       browser.back()
    #      elif i == 5:
    #       links[i].click()
    #       browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #       time.sleep(5)
    #       browser.current_url.__contains__("https://www.toolsqa.com/selenium-tutorial/")
    #       print("pass5")
    #       browser.back()
    #      elif i == 6:
    #       links[i].click()
    #       browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #       time.sleep(5)
    #       browser.current_url.__contains__("https://artoftesting.com/selenium-tutorial")
    #       print("pass6")
    #       browser.back()
    #      elif i == 7:
    #       links[i].click()
    #       browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #       time.sleep(5)
    #       browser.current_url.__contains__("https://www.softwaretestinghelp.com/selenium-tutorial-1/")
    #       print("pass7")
    #       browser.back()
    #      elif i == 8:
    #       links[i].click()
    #       browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #       time.sleep(5)
    #       browser.current_url.__contains__("https://www.softwaretestingmaterial.com/selenium-tutorial/")
    #       print("pass8")
    #       browser.back()
    #      elif i == 9:
    #       links[i].click()
    #       browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #       time.sleep(5)
    #       browser.current_url.__contains__("https://www.softwaretestingmaterial.com/selenium-tutorial/")
    #       print("pass9")
    #       browser.back()
    #      elif i == 10:
    #       links[i].click()
    #       browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #       time.sleep(5)
    #       browser.current_url.__contains__("https://www.google.com/search?q=selenium+tutorial&tbm=isch&source=univ&sa=X&ved=2ahUKEwjgz8iHoLjoAhVk6nMBHdjDCPgQsAR6BAgEEAE&biw=1366&bih=613")
    #       print("pass10")
    #       browser.back()

if __name__ == "__main__":
    unittest.main()