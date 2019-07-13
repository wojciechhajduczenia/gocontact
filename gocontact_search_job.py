'''
@author: wojtekhaj
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
path = '/home/wojtekhaj/mindera/qa-sortable-challenge/solution/chromedriver'

driver=webdriver.Chrome(path)
driver.get("https://www.amazon.jobs/en-gb")
jobs_title_text="Amazon.jobs"
assert jobs_title_text in driver.title
driver.maximize_window()
driver.implicitly_wait(10)


#search for portugal setubal
search_text_job_location="Portugal, setubal"
job_search_city_xpath="//input[@placeholder='Location' and @class='undefined form-control tt-input']"
jobs_found_xpath="//div[@class='col-sm-6 job-count-info' and contains (text(), 'Showing 1')]"

search_element=driver.find_element_by_xpath(job_search_city_xpath)
search_element.click()
search_element.send_keys(search_text_job_location)
search_element.send_keys(Keys.ENTER)
driver.find_element_by_xpath(jobs_found_xpath)
driver.save_screenshot("jobs_found.png")


#change to 5 miles
#if not on mi change to mi
km_button="//div[@class='container']//div[@class='slider round']//button[aria-label=contains(text(), 'Kilometers selected')]"
mile_button="//div[@class='container']//div[@class='slider round']//button[aria-label=contains(text(), 'Miles selected')]"
five_miles_unchecked_xpath="//div[@class='d-none d-md-block col-sm-4 search-page-filter']//button[(@aria-label='5 Miles' ) and (@aria-checked='false')]"
five_miles_checked_xpath="//div[@class='d-none d-md-block col-sm-4 search-page-filter']//button[(@aria-label='5 Miles' ) and (@aria-checked='true')]"
search_empty_id="search-empty"
#to have miles
try:
    driver.find_element_by_xpath(mile_button)
except NoSuchElementException:
    driver.find_element_by_xpath(km_button).click()
    
driver.find_element_by_xpath(five_miles_unchecked_xpath).click()
driver.find_element_by_xpath(five_miles_checked_xpath)
driver.find_element_by_id(search_empty_id)
driver.save_screenshot("no_jobs_5miles.png")


#search by software and use suggestion
reset_search_button="//div[@class='row']//a[@data-label='reset']"
search_field_job_xpath="//div[@class='navigation']//input[@placeholder='Search for jobs' and @class='form-control tt-input']"
search_text_job_name="software"
search_box_clear_activation_xpath="//div[@id='search-container']//span[@class='twitter-typeahead']//input[@name='loc_query']"
search_text_suggestion="//strong[text()='Software']"
search_job_type="Solutions Architect"
search_job_type_xpath="//button[@name='desktopFilter_job_category']//p[text()='" + search_job_type + "']"
search_text_job_location="San Francisco"

jobs_found_xpath="//div[@class='col-sm-6 job-count-info' and contains (text(), 'Showing 1')]"

#clearing filters applied
driver.find_element_by_xpath(reset_search_button).click()
location=driver.find_element_by_xpath(search_box_clear_activation_xpath)
location.click()
location.clear()
location.send_keys(Keys.ENTER)


job_search_element=driver.find_element_by_xpath(search_field_job_xpath)
job_search_element.click()
job_search_element.send_keys(search_text_job_name)
sugestion=driver.find_element_by_xpath(search_text_suggestion)
driver.save_screenshot("jobs_suggestion.png")
sugestion.click()
search_element=driver.find_element_by_xpath("//input[@placeholder='Location']")
search_element.send_keys(Keys.ENTER)
driver.save_screenshot("jobs_searching_sugestion.png")
driver.find_element_by_xpath(search_job_type_xpath).click()
driver.save_screenshot("jobs_Solution_arch.png")
location=driver.find_element_by_xpath("//input[@placeholder='Location']")
location.click()
location.send_keys(search_text_job_location)
location.send_keys(Keys.ENTER)
driver.find_element_by_xpath(jobs_found_xpath)
driver.save_screenshot("jobs_sol_arch_san_francisco.png")

driver.close()