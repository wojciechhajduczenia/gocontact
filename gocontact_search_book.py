'''
@author: wojtekhaj
'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

path = '/home/wojtekhaj/mindera/qa-sortable-challenge/solution/chromedriver'

driver=webdriver.Chrome(path)
driver.get("https://www.amazon.co.uk")
main_page_title="Amazon.co.uk: Low Prices in Electronics, Books, Sports Equipment & more"
assert main_page_title in driver.title
driver.maximize_window()
driver.implicitly_wait(10)


#search for books
main_search_field_xpath= "//input[@id='twotabsearchtextbox']"
search_phraze_book="chasing Excellence"

search_object=driver.find_element_by_xpath(main_search_field_xpath)
search_object.send_keys(search_phraze_book)
search_object.send_keys(Keys.ENTER)

#verification
search_title="Amazon.co.uk: chasing Excellence"
book_title="Chasing Excellence: A Story About Building the World's Fittest Athletes"                                                          
book_title_xpath="//span[contains(text(),'Chasing Excellence')]"

assert search_title in driver.title
element=driver.find_element_by_xpath(book_title_xpath)
ActionChains(driver).move_to_element(element).perform()
driver.save_screenshot("chasing_excelence.png")

#check author
author="Ben Bergeron"
author_xpath="//a[contains(text(),' "+author+"')]"

element=driver.find_element_by_xpath(author_xpath)
ActionChains(driver).move_to_element(element).perform()
driver.save_screenshot("author.png")



#check for user in comments
user_commenter="Cerith Leighton Watkins"
stars_icon_xpath_for_book="//div[@class='sg-row']//div[@class='sg-col-inner']//span[@class='a-size-medium a-color-base a-text-normal' and contains (text(), 'Chasing Excellence: A Story')]/../../../..//span[@class='a-icon-alt']"
see_all_xpath="//a[@class='a-size-small a-link-emphasis' and contains (text(), 'See all')]"
reviews_page_title="Amazon.co.uk:Customer reviews: Chasing Excellence: A Story About Building the World's Fittest Athletes"
search_field_comments_id="filterByKeywordTextBox"
search_phraze_comment_author="Cerith Leighton Watkins"
comment_author_not_found_text="Sorry, no reviews match your current selections."
search_results_xpath="//div[@id='cm_cr-review_list']"

driver.find_element_by_xpath(stars_icon_xpath_for_book).click()
driver.find_element_by_xpath(see_all_xpath).click()
assert reviews_page_title in driver.title
driver.find_element_by_id(search_field_comments_id).send_keys(search_phraze_comment_author, Keys.ENTER)
assert driver.page_source.find(comment_author_not_found_text)
driver.save_screenshot("comment_found.png")


#insert comment
my_comment_text="gostei de ler"
insert_comment_button_id="a-autoid-0-announce"
insert_comment_button_xpath="//a[@id='a-autoid-0-announce']"
comment_not_possible_for_new_users_xpath="//span[@class='a-color-error ryp__icon-alert__text']//span[contains (text(), 'We apologize')]"
apologize_text="We apologize"
review_page_title="Review Your Purchases"
sign_in_title="Amazon Sign In"

driver.back()
driver.find_element_by_id(insert_comment_button_id).click()
if sign_in_title in driver.title:
#sign in needed
    user_email_xpath="//input[@id='ap_email']"
    user_email_existing="wojciech.hajduczenia@gmail.com"
    user_password_xpath="//input[@id='ap_password']"
    user_password_existing="xxxxx"
    
    sign_in_button_id="signInSubmit"
    assert sign_in_title in driver.title
    driver.find_element_by_xpath(user_email_xpath).send_keys(user_email_existing)
    driver.find_element_by_xpath(user_password_xpath).send_keys(user_password_existing)
    driver.find_element_by_id(sign_in_button_id).click()
    
assert review_page_title in driver.title

if apologize_text not in driver.page_source:
    driver.save_screenshot("comment_inserted.png")

else:
    driver.save_screenshot("comment_not_inserted.png")
    ######logout
    
login_main_page_button_xpath="//div[@id='nav-tools']//span[@class='nav-line-2' and (text()='Account & Lists')]"
sign_out_text="Sign Out"
sign_out_button_xpath="//span[@class='nav-text' and contains(text(),'" + sign_out_text + "')]"
element=driver.find_element_by_xpath(login_main_page_button_xpath)
ActionChains(driver).move_to_element(element).perform()
sign_out=driver.find_element_by_xpath(sign_out_button_xpath)
ActionChains(driver).move_to_element(sign_out).click().perform()
driver.back()
driver.back()
driver.back()

#find comments with 1 star
one_star_xpath="//table[@id='histogramTable']//tr[@data-reftag='cm_cr_arp_d_hist_1']//a[@title='1 star']"

driver.find_element_by_xpath(one_star_xpath).click()
driver.save_screenshot("one_star.png")
driver.back()


#check comment from 17 September 2017
comment_date="17 September 2017"
comment_date_xpath="//span[contains(text(),'"+comment_date+"')]"
next_page_xpath="//a[contains(text(),'Next page')]"

try:
    element=driver.find_element_by_xpath(comment_date_xpath)
    if element.is_displayed():
        ActionChains(driver).move_to_element(element).perform()
        driver.save_screenshot("17Sept.png")
    
except NoSuchElementException:
    driver.find_element_by_xpath(next_page_xpath).click()   
    element_other_page=driver.find_element_by_xpath(comment_date_xpath)
    if element.is_displayed():
        ActionChains(driver).move_to_element(element_other_page).perform()
        driver.save_screenshot("17Sept_other_page.png")
driver.implicitly_wait(300)
driver.close()