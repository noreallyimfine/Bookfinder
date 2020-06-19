from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import csv

driver = webdriver.Chrome()

BASE_URL = "https://www.goodreads.com/list/show/"
BOOK_LIST = "1.Best_Books_Ever?page="

# f = open("best_books_details.csv", 'w', encoding='UTF-8')
# csv_writer = csv.writer(f)
# csv_writer.writerow(['title', 'author', 'rating', 'language', 'description'])


def handle_signin(counter):
    try:
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/button').click()
        print("Found element and clicked!")
    except NoSuchElementException as e:
        print(e)
        counter += 1
    finally:
        return counter


counter = 0
# first run - 10 pages to test
for page in range(1, 11):
    driver.get(f'{BASE_URL}{BOOK_LIST}{page}')

    for i in range(1, 101):
        
        
        # dictionary to write consistently to csv
        # should start with keys pointint to Nones
        # there will be check to make sure the value is being written to the right key
        # can write Nones so we dont get bad data
        data = {"title": None,
                "author": None,
                "rating": None,
                "description": None,
                "Language Edition": None,
                "Language": None,
                "ISBN": None}

        time.sleep(1)
        if counter < 3:
            counter = handle_signin(counter)

        data["title"] = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/a/span')
        data["author"] = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/span[2]')
        data["rating"] = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/div[1]/span/span')

        title.click()
        time.sleep(.5)
        if counter < 3:
            counter = handle_signin(counter)

        # open more details
        more_deets = driver.find_element_by_xpath('//*[@id="bookDataBoxShow"]')
        more_deets.click()
        time.sleep(.5)

        language_edition = driver.find_element_by_xpath('//*[@id="bookDataBox"]/div[2]/div[1]')
        if 'Language' in language_edition.text:
            language = driver.find_element_by_xpath('//*[@id="bookDataBox"]/div[2]/div[2]')
        else:
            language = driver.find_element_by_xpath('//*[@id="bookDataBox"]/div[3]/div[2]')

        print("Language:", language.text)

        description = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/div[3]/div/span[2]')

        for d in description:
            print(d.get_attribute("innerText"))

        driver.back()


driver.close()
