'''
@author: wojtekhaj
'''

from selenium import webdriver

path = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

driver=webdriver.Chrome(path)
driver.get("https://www.amazon.co.uk")
main_page_title="Amazon.co.uk: Low Prices in Electronics, Books, Sports Equipment & more"
assert main_page_title in driver.title
driver.maximize_window()
driver.implicitly_wait(10)

#sign in
login_main_page_button_xpath="//div[@id='nav-tools']//span[@class='nav-line-2' and (text()='Account & Lists')]"
user_email_xpath="//input[@id='ap_email']"
user_email_existing="xxxxxxxxxxxxxxxxxx@xxxxxxxxxxxxxx"
user_password_xpath="//input[@id='ap_password']"
user_password_existing="xxxxxxxxxxxxxxxxxxxxxxxxxx"
sign_in_title="Amazon Sign In"
sign_in_button_id="signInSubmit"



driver.find_element_by_xpath(login_main_page_button_xpath).click()
driver.implicitly_wait(10)
assert sign_in_title in driver.title

driver.find_element_by_xpath(user_email_xpath).send_keys(user_email_existing)
driver.find_element_by_xpath(user_password_xpath).send_keys(user_password_existing)
driver.find_element_by_id(sign_in_button_id).click()
assert main_page_title in driver.title
driver.save_screenshot("correct_pass.png")
driver.close()





