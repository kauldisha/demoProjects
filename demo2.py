import time
from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
# https://docs.python.org/3/tutorial/
# https://www.w3schools.com/python/
# https://www.tutorialspoint.com/python/index.htm
# https://www.learnpython.org/
# https://www.programiz.com/python-programming/tutorial
# https://www.guru99.com/python-tutorials.html


class Test(unittest.TestCase):
    def testName(self):
        browser = webdriver.Chrome("c:\chromedriver.exe")
        browser.get("https://www.google.com")
        browser.maximize_window()
        search_box = browser.find_element_by_xpath("//input[contains(@class,'gLFyf gsfi')]")
        search_box.send_keys("python tutorial")
        search_box.submit()
        for i in range(5):
         time.sleep(2)
         links = browser.find_elements_by_xpath("//div[@class='g'] //h3".replace('0', 'i'))
         links[i].click()
         time.sleep(5)
         print(browser.current_url)
         print(links[i])
         assert (browser.current_url == links[i])
         browser.back()
         time.sleep(5)
        print(i)
        time.sleep(5)
if __name__ == "__main__":
    unittest.main()




#         for i in range(10):
#             time.sleep(2)
#             links = browser.find_elements_by_xpath("//div[@class='g'] //h3".replace('0', 'i'))
#             if i < 8:
#                 links[i].click()
#                 print(i)
#                 time.sleep(5)
#                 if i== 0:
#                     browser.current_url.__contains__("https://docs.python.org/3/tutorial/")
#                     print(browser.current_url)
#                     time.sleep(5)
#                     browser.back()
#
#                 elif i== 1:
#                     browser.current_url.__contains__("https://www.w3schools.com/python/")
#                     print(browser.current_url)
#                     time.sleep(5)
#                     browser.back()
#
#                 elif i== 2:
#                     browser.current_url.__contains__("https://www.tutorialspoint.com/python/index.htm")
#                     print(browser.current_url)
#                     browser.back()
#
#                 elif i== 3:
#                     browser.current_url.__contains__("https://www.learnpython.org/")
#                     print(browser.current_url)
#                     browser.back()
#
#                 elif i== 4:
#                     browser.current_url.__contains__("https://www.javatpoint.com/python-tutorial")
#                     print(browser.current_url)
#                     browser.back()
#
#                 elif i== 5:
#                     browser.current_url.__contains__("https://www.guru99.com/python-tutorials.html")
#                     print(browser.current_url)
#                     browser.back()
#                 else:
#                     print("bla bla bla")
#             else:
#                 print("Elseeeeeeeeeeeeeee")
# if __name__ == "__main__":
#     unittest.main()


