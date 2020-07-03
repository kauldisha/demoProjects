import unittest
from selenium import webdriver
import time
class Test(unittest.TestCase):
    def testName(self):
        #create drider object
        browser = webdriver.Chrome("C:/chromedriver.exe")
        #passing the link to the chrome driver
        browser.get("https://www.google.com")
        browser.maximize_window()
        search_box = browser.find_element_by_xpath("//input[contains(@class,'gLFyf gsfi')]")
        search_box.send_keys("registration form for testing")
        search_box.submit()
        link=browser.find_element_by_xpath("//h3[contains(text(),'Exam Registration Form Template | JotForm')]")
        if link.is_displayed():
            link.click()
        else:
            browser.get("https://www.spotify.com/in/signup/?sp_t_counter=1")
        time.sleep(20)
        iframe = browser.find_element_by_tag_name('iframe')
        #switch to the ifreme
        browser.switch_to.frame(iframe)
        browser.find_elements_by_xpath("h1[class='title']")
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        browser.find_element_by_css_selector("button[id='input_2']").click()
        assert browser.find_element_by_css_selector("div[class='form-error-message']").is_displayed()

        #browser.find_element_by_css_selector("input[id='first_9']").send_keys("hghjg")
        # browser.find_element_by_css_selector("input[id='last_9']").send_keys("hghjg")
        # browser.find_element_by_css_selector("input[id='input_10']").send_keys(5646465)
        # browser.find_element_by_css_selector("input[id='input_3']").send_keys("MCA")

        # browser.find_element_by_css_selector('select[id="input_4_day"]').send_keys(10)
        # browser.find_element_by_css_selector("select[id='input_4_month']").send_keys("JUNE")
        # browser.find_element_by_css_selector("select[id='input_4_year']").send_keys(2015)
        # browser.find_element_by_css_selector("select[id='input_5_day']").send_keys(20)
        # browser.find_element_by_css_selector("select[id='input_5_month']").send_keys("JULY")
        # browser.find_element_by_css_selector("select[id='input_5_year']").send_keys(2017)
        #







# import unittest
# from selenium import webdriver
# #from selenium.webdriver.common.action_chains import ActionChains
# import time
# class Test(unittest.TestCase):
#     def testName(self):
#         #create drider object
#         driver = webdriver.Chrome("C:/chromedriver.exe")
#         #passing the link to the chrome driver
#         driver.get("https://www.spotify.com/in/signup/?sp_t_counter=1")
#         #maximix the window
#         driver.maximize_window()
#         driver.find_element_by_css_selector("input[id='register-email']").send_keys("kauldisha.es@gmail.com")
#         driver.find_element_by_css_selector("input[id='register-confirm-email']").send_keys("kauldisha.es@gmail.com")
#         driver.find_element_by_css_selector("input[type='password']").send_keys("Kauldisha@123")
#         driver.find_element_by_css_selector("input[id='register-displayname']").send_keys("Disha")
#         driver.find_element_by_css_selector("input[id='register-dob-year']").send_keys(2000)
#         dob=driver.find_element_by_css_selector("select[id='register-dob-month']")
#         dob.send_keys("october")
#         driver.find_element_by_css_selector("input[id='register-dob-day']").send_keys("9")
#         driver.find_elements_by_css_selector('input[type="radio"]')[2].click()
#         driver.find_element_by_css_selector("input[id='register-thirdparty']").click()
#         time.sleep(20)
#         driver.find_element_by_css_selector("label[id='recaptcha-anchor-label']").click
#
#         driver.find_element_by_css_selector("a[id='register-button-email-submit']").click
#         time.sleep(20)
#
#
# if __name__ == "__main__":
#      unittest.main()










































# #"https://www.123formbuilder.com/free-form-templates/Exam-Registration-Form-3348871/"
# #https://www.123formbuilder.com/free-form-templates/
# #https://www.softwaretestingmaterial.com/test-scenarios-registration-form/
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
#
# class Test(unittest.TestCase):
#     def testName(self):
#         #create drider object
#         driver = webdriver.Chrome("C:/chromedriver.exe")
#         #passing the link to the chrome driver
#         driver.get("https://www.123formbuilder.com/free-form-templates/Online-Order-Form-271188/")
#         #maximix the window
#         driver.maximize_window()
#         iframe = driver.find_element_by_tag_name('iframe')
#        #switch to the ifreme
#         driver.switch_to.frame(iframe)
#         driver.find_elements_by_xpath("//h1[contains(text(),'Online Order Form')]")
#         driver.find_elements_by_css_selector('input[type="radio"]')[3].click()
#         time.sleep(5)
#         driver.find_element_by_css_selector("input[type='number']").send_keys(55)
#         time.sleep(5)
#         driver.find_element_by_css_selector("div[role='application']")
#         #ActionChains(driver).move_to_element("div[role='application").click().send_keys('01012011').perform()
#         time.sleep(5)
#         driver.find_element_by_css_selector("input[placeholder='Street Address']").send_keys(67)
#         driver.find_element_by_css_selector("input[placeholder='Street Address Line 2']").send_keys("new dewas road")
#         driver.find_element_by_css_selector("input[placeholder='City']").send_keys("Indore")
#         driver.find_element_by_css_selector("input[placeholder='Region']").send_keys("rural")
#         driver.find_element_by_css_selector("input[placeholder='Postal / Zip Code']").send_keys(452003)
#         driver.find_element_by_css_selector("input[placeholder='Country']").send_keys("India")
#         driver.find_element_by_css_selector("input[placeholder='First']").send_keys("Disha")
#         driver.find_element_by_css_selector("input[placeholder='Last']").send_keys("Kaul")
#         time.sleep(5)
#         driver.find_element_by_css_selector("input[placeholder='### ### #### ']").send_keys("7415009986")
#         time.sleep(5)
#         driver.find_element_by_css_selector("input[type='email']").send_keys("kauldisha.es@gmail.com")
#         driver.find_element_by_css_selector("label[data-role='checkbox']").is_selected()
#         driver.find_element_by_css_selector("button[type='submit']").click()
#         time.sleep(50)
#         driver.switch_to.default_content()
#
# if __name__ == "__main__":
#     unittest.main()
#
#