import unittest
from selenium import webdriver
import time
import random
import string
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        letters = string.ascii_lowercase
        #create drider object
        browser = webdriver.Chrome("C:/chromedriver.exe")
        #passing the link to the chrome driver
        browser.get("https://www.linkedin.com/home")
        browser.maximize_window()
        browser.find_element_by_css_selector("a[class='nav__button-secondary']").click()
        time.sleep(5)
        browser.find_element_by_css_selector("input[id='username']").send_keys("dishakaul.es@gmail.com")
        browser.find_element_by_css_selector("input[id='password']").send_keys("Ohmygod24")
        browser.find_element_by_css_selector("button[type='submit']").click()

        browser.find_element_by_css_selector("li-icon[class='mr2']").click()
        time.sleep(5)
        browser.find_element_by_css_selector(" span[class='ph1']")
        browser.execute_script("window.scrollTo(10,document.body.scrollHeight)")
        time.sleep(5)
        containt="Hello\nThis is a python code\n\n" +random.choice(letters)+" Thanks n Regards\nPython Team"
        browser.find_element_by_css_selector("div[role='textbox']").send_keys(containt)
        time.sleep(10)
        # select_file=browser.find_element_by_css_selector("li-icon[type='document-icon']")
        # select_file.send_keys("C:/Users/Shristi/PycharmProjects/hello/email_posting.py")
        browser.find_element_by_xpath("//button[contains(@class,'share-actions')]").click()
        time.sleep(10)
        browser.find_element_by_css_selector("img.nav-item__profile-member-photo.nav-item__icon.ghost-person.ember-view").click()
        time.sleep(5)
        browser.find_element_by_xpath("//a[contains(@data-control-name,'recent_activity_nav_all')]").click()
        time.sleep(5)
        assert browser.find_element_by_xpath("//span[contains(text(),'now • ')]").is_displayed()

        time.sleep(5)
if __name__ == '__main__':
    unittest.main()
