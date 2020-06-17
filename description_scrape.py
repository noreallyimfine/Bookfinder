from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import csv

driver = webdriver.Chrome()

BASE_URL = "https://www.goodreads.com/list/show/"
BOOK_LIST = "1.Best_Books_Ever?page="

# f = open("best_books_details.csv", 'w', encoding='UTF-8')


def handle_signin():
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/button/img').click()
    except NoSuchElementException:
        return


driver.get(f'{BASE_URL}{BOOK_LIST}1')

for i in range(1, 5):

    title = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/a/span')
    author = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/span[2]')
    rating = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/div[1]/span/span')
    
    title.click()
    time.sleep(3)
    driver.back()


driver.close()
