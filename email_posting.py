import unittest
from selenium import webdriver

import time
import random
import string



class Test(unittest.TestCase):

    def testName(self):
        def randomString(stringLength=10):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(stringLength))
        #create driver variable
        driver = webdriver.Chrome("C:/chromedriver.exe")
        #passing the link to the chrome driver
        driver.get("https://www.trash-mail.com/new-address/")
        #maximize the window
        driver.maximize_window()
        time.sleep(5)
        email = driver.find_element_by_css_selector("input#form-postbox-new").send_keys(randomString(10))
        password = driver.find_element_by_css_selector("input#form-password-new1").send_keys("abcd!@#$")
        confirmPassword = driver.find_element_by_css_selector("input#form-password-new2").send_keys("abcd!@#$")
        signUpButton = driver.find_element_by_css_selector("button#create-mail").click()

        composeButton = driver.find_element_by_css_selector("a[href*='/compose-mail']").click()
        time.sleep(2)
        receiverEmail = driver.find_element_by_css_selector("input#form-to").send_keys("gauravgamer43@gmail.com")
        time.sleep(2)
        subjectOfEmail = driver.find_element_by_css_selector("input#form-subject").send_keys("Python Assignment")
        time.sleep(3)
        emailBody = driver.find_element_by_css_selector("div#editor") \
            .send_keys("Hello\nThis is a python code\n\nThanks and Regards\nPython Team")
        time.sleep(2)
        attachFile = driver.find_element_by_css_selector("input[type='file']")
        time.sleep(5)
        attachFile.send_keys("C:/Users/Shristi/PycharmProjects/hello/email_posting.py")
        time.sleep(2)
        sendMailBtn = driver.find_element_by_css_selector("button#send-mails").click()
        time.sleep(2)


        driver.close()

if __name__ == "__main__":
    unittest.main()