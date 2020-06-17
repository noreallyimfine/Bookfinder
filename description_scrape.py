from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import csv

driver = webdriver.Chrome()

BASE_URL = "https://www.goodreads.com/list/show/"
BOOK_LIST = "1.Best_Books_Ever?page="

# f = open("best_books_details.csv", 'w', encoding='UTF-8')


def handle_signin(counter):
    try:
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/button').click()
        print("Found element and clicked!")
    except NoSuchElementException as e:
        print(e)
        counter += 1
    finally:
        return counter


driver.get(f'{BASE_URL}{BOOK_LIST}1')

counter = 0
for i in range(1, 5):

    time.sleep(1)
    if counter < 3:
        counter = handle_signin(counter)

    title = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/a/span')
    author = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/span[2]')
    rating = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/div[1]/span/span')
    
    title.click()
    time.sleep(1)
    if counter < 3:
        counter = handle_signin(counter)
    
    # open more details
    driver.find_element_by_xpath('//*[@id="details"]/div[3]').click()
    time.sleep(1)

    language_edition = driver.find_element_by_xpath('//*[@id="bookDataBox"]/div[3]/div[1]')
    print("Language Edition:", language_edition.text)
    language = driver.find_element_by_xpath('//*[@id="bookDataBox"]/div[3]/div[2]')
                                            # //*[@id="bookDataBox"]/div[3]/div[2]

    print("Language:", language.text)

    driver.back()


driver.close()

