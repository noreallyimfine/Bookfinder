from selenium import webdriver

driver = webdriver.Chrome()
BASE_URL = "https://www.goodreads.com/list/show/"

first_page = "1.Best_Books_Ever"
driver.get(BASE_URL + first_page)



driver.close()
