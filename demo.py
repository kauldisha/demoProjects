# coding=utf-8
import time
from selenium import webdriver
import unittest


class Test(unittest.TestCase):
    def  testName(self):
        list = ["https://docs.python.org/3/tutorial/","https://www.w3schools.com/python/","https://www.tutorialspoint.com/python/index.htm"
            ,"https://www.learnpython.org/","https://www.programiz.com/python-programming/tutorial"]
        browser = webdriver.Chrome("c:\chromedriver.exe")
        browser.get("https://www.google.com")
        browser.maximize_window()
        search_box = browser.find_element_by_xpath("//input[contains(@class,'gLFyf gsfi')]")
        search_box.send_keys("python tutorial")
        search_box.submit()
        for i in range(1, 8):
          time.sleep(2)
          links = browser.find_elements_by_xpath("//div[@class='g'] //h3".replace('1', 'i'))
          links[i].click()
          print(list[i])
          print(browser.current_url)
          time.sleep(5)
          assert (browser.current_url == list[i]) == True
          browser.back()
          time.sleep(5)
          print(i)
          time.sleep(5)
if __name__ == "__main__":
    unittest.main()