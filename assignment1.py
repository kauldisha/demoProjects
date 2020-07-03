import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class Test(unittest.TestCase):
    def testName(self):
        #create drider object
        driver = webdriver.Chrome("C:/chromedriver.exe")
        #passing the link to the chrome driver
        driver.get("https://www.google.com")
        #maximix the window
        driver.maximize_window()
        search_box = driver.find_element_by_css_selector("input[title='Search']")
        #pass python tutorial in search box
        search_box.send_keys("python tutorial")

        submit_button = driver.find_element_by_css_selector("input[value='Google Search']")
        #click on search button of google home page
        submit_button.click()
        time.sleep(2)
        #list on links that we have to verify
        list = ["https://docs.python.org/3/tutorial/", "https://www.w3schools.com/python/",
                "https://www.tutorialspoint.com/python/index.htm", "https://www.learnpython.org/",
                "https://www.programiz.com/python-programming/tutorial", "https://www.programiz.com/python-programming",
                "https://www.guru99.com/python-tutorials.html", "https://www.javatpoint.com/python-tutorial",
                "https://realpython.com/"]

        for i in range(8):
            #dynamic xpath of links
            links = driver.find_elements_by_xpath("//div[@id='rso'] /div[@class='g'] /div /div //h3".replace('1', 'i'))
            #xpath of links description
            linksDescription = driver.find_elements_by_xpath("//div[@id='rso'] /div[@class='g'] //div[@class='s']".replace('1', 'i'))
            #used action chain to move cersor to the element
            actions = ActionChains(driver)
            #cersore move to the link description
            actions.move_to_element(linksDescription[i]).perform()
            time.sleep(2)
            #click on links
            links[i].click()
            time.sleep(2)
            #verifing links from the list
            assert driver.current_url in list
            print("jhkhk")
            time.sleep(2)
            # click on back button
            driver.back()
            time.sleep(2)
            i += 1
            time.sleep(2)

if __name__ == "__main__":
    unittest.main()