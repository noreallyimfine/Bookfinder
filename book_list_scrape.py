from selenium import webdriver

driver = webdriver.Chrome()
BASE_URL = "https://www.goodreads.com/list/show/"

first_page = "1.Best_Books_Ever"
driver.get(BASE_URL + first_page)

title = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[3]/div[5]/table/tbody/tr[1]/td[3]/a/span')
print(title)

driver.close()
