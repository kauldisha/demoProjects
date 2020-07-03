from selenium import webdriver
import time

browser = webdriver.Chrome("c:\chromedriver.exe")
browser.get("https://blog.hubspot.com/service/best-contact-us-pages")
browser.maximize_window()
time.sleep(10)
browser.find_element_by_css_selector("input[name='fname']").send_keys("disha")
browser.find_element_by_css_selector("input[name='lname']").send_keys("kaul")
browser.find_element_by_css_selector('div[class="sc-kjoXOD kZTgCz"]').click()
time.sleep(30)
# iframe = browser.find_element_by_tag_name('iframe')
# #switch to the ifreme
# browser.switch_to.frame(iframe)
# browser.switch_to.default_content()
browser.find_element_by_css_selector("div[class='leadinModal-overlay']").click()
browser.find_element_by_css_selector('div[class="sc-kjoXOD kZTgCz"]').click()
browser.find_element_by_css_selector("input[placeholder='john@smith.com']").send_keys("random@hoymail.com")
browser.find_element_by_css_selector(".sc-jqCOkK.kinLXH .sc-jbKcbu.eOYwnk").click()






















# browser = webdriver.Chrome("c:\chromedriver.exe")
# browser.get("https://www.google.com")
# browser.maximize_window()
# search_box = browser.find_element_by_xpath("//input[contains(@class,'gLFyf gsfi')]")
# search_box.send_keys("Mercury tours")
# search_box.submit()
# time.sleep(5)
# browser.find_element_by_xpath("//h3[text()='Mercury Tours - demoaut.com']").click()
# time.sleep(4)
# browser.find_element_by_css_selector("td[align='right'] a[href*='mercuryregister']").click()
# time.sleep(2)
# browser.find_element_by_xpath("//input[contains(@name,'firstName')]").send_keys("Test")
# time.sleep(2)
# browser.find_element_by_xpath("//input[contains(@name,'lastName')]").send_keys("Demo")
# time.sleep(2)
# browser.find_element_by_xpath("//input[contains(@name,'phone')]").send_keys("1234567890")
# time.sleep(2)
# browser.find_element_by_xpath("//input[contains(@name,'userName')]").send_keys("demo@gmail.com")
# time.sleep(2)
# browser.find_element_by_xpath("//input[contains(@name,'address1')]").send_keys("ABCDEFGHIJKL")
# time.sleep(2)
# browser.find_element_by_xpath("//input[contains(@name,'city')]").send_keys("Indore")
# time.sleep(2)
# browser.find_element_by_xpath("//input[contains(@name,'state')]").send_keys("MP")
# time.sleep(2)
# browser.find_element_by_xpath("//input[contains(@name,'postalCode')]").send_keys("4567896")
# time.sleep(2)
# # Dropdown selection by visible text
# # element=browser.find_elements_by_name("country")
# # drp=Select(element)
# # drp.select_by_visible_text("INDIA")
# # Dropdown selection by value
# # drp.eselect_by_value("92")
# # Dropdown selection by Index
# # drp.select_by_index(20)
# browser.find_element_by_xpath("//input[contains(@name,'email')]").send_keys("demo @ gmail.com")
# time.sleep(1)
# browser.find_element_by_xpath("//input[contains(@name,'password')]").send_keys("demo@123")
# time.sleep(1)
# browser.find_element_by_xpath("//input[contains(@name,'confirmPassword')]").send_keys("demo@123")
# time.sleep(1)
# browser.find_element_by_xpath("//input[contains(@name,'register')]").click()
# time.sleep(2)
# browser.find_element_by_css_selector("a[href*='mercurysignon.php']").click()
# time.sleep(2)
# browser.find_element_by_xpath("//input[contains(@name,'userName')]").send_keys("demo@gmail.com")
# time.sleep(1)
# browser.find_element_by_xpath("//input[contains(@name,'password')]").send_keys("demo@123")
# time.sleep(2)
# browser.find_element_by_xpath("//input[contains(@name,'login')]").click()
# time.sleep(2)




