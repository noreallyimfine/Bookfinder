from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import csv

driver = webdriver.Chrome()

BASE_URL = "https://www.goodreads.com/list/show/"
BOOK_LIST = "1.Best_Books_Ever?page="

f = open("best_books_details_4.csv", 'w', encoding='UTF-8')
csv_writer = csv.writer(f)
csv_writer.writerow(['title', 'author', 'rating', 'description',
                     'language', 'isbn'])


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
for page in range(11, 25):
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
                "language": None,
                "isbn": None}

        time.sleep(1)
        print("Counter:", counter)
        if counter < 3:
            counter = handle_signin(counter)

        title = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/a/span')
        author = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/span[2]')
        rating = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/div[1]/span/span')

        data['title'] = title.text
        data['author'] = author.text
        data['rating'] = rating.text

        title.click()
        time.sleep(1)
        if counter < 3:
            counter = handle_signin(counter)

        # open more details
        more_deets = driver.find_element_by_xpath('//*[@id="bookDataBoxShow"]')
        more_deets.click()
        time.sleep(.5)

        for div in range(1, 4):
            try:
                header = driver.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/div[5]/div[3]/div[1]/div[{div}]/div[1]').get_attribute('innerText')
                if header == 'Edition Language':
                    data['language'] = driver.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/div[5]/div[3]/div[1]/div[{div}]/div[2]').get_attribute('innerText')
                elif header == 'ISBN':
                    data['isbn'] = driver.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/div[5]/div[3]/div[1]/div[{div}]/div[2]').get_attribute('innerText')
            except NoSuchElementException:
                print(f"Error getting div {div}")

        description = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/div[3]/div/span[2]')

        if len(description) < 1:
            description = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/div[3]/div/span[1]')

        
        try:
            data['description'] = description[0].get_attribute('innerText')
        except:
            print(f"Error getting description, for book {title}")
        csv_writer.writerow([data['title'], data['author'], data['rating'],
                             data['description'], data['language'], data['isbn']])

        driver.back()


driver.close()
