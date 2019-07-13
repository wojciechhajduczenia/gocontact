'''
@author: wojtekhaj
'''

from selenium import webdriver

path = '/home/wojtekhaj/mindera/qa-sortable-challenge/solution/chromedriver'

driver=webdriver.Chrome(path)
driver.get("https://www.amazon.co.uk")
main_page_title="Amazon.co.uk: Low Prices in Electronics, Books, Sports Equipment & more"
assert main_page_title in driver.title
driver.maximize_window()
driver.implicitly_wait(10)

#create account with existing user
login_main_page_button_xpath="//div[@id='nav-tools']//span[@class='nav-line-2' and (text()='Account & Lists')]"
create_account_button_xpath="//a[@id='createAccountSubmit']"
user_name_xpath="//input[@id='ap_customer_name']"
user_name_existing="xxxxxxxxxxxxxxxxxxx"
user_email_xpath="//input[@id='ap_email']"
user_email_existing="xxxxxxxxxxxxxxxxxx@xxxxxxxxxxxxx"
user_password_xpath="//input[@id='ap_password']"
user_password_existing="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
user_password_check_xpath="//input[@id='ap_password_check']"
create_account_button_finish_id="continue"
user_email_in_use_xpath="//h4[@class='a-alert-heading' and text()='E-mail address already in use']"
sign_in_title="Amazon Sign In"
register_title="Amazon Registration"


driver.find_element_by_xpath(login_main_page_button_xpath).click()
driver.implicitly_wait(10)
assert sign_in_title in driver.title
driver.find_element_by_xpath(create_account_button_xpath).click()
driver.implicitly_wait(10)
assert register_title in driver.title
driver.find_element_by_xpath(user_name_xpath).send_keys(user_name_existing)
driver.find_element_by_xpath(user_email_xpath).send_keys(user_email_existing)
driver.find_element_by_xpath(user_password_xpath).send_keys(user_password_existing)
driver.find_element_by_xpath(user_password_check_xpath).send_keys(user_password_existing)
driver.find_element_by_id(create_account_button_finish_id).click()
driver.find_element_by_xpath(user_email_in_use_xpath)
driver.save_screenshot("user_exists.png")
driver.close()

 
