from selenium import webdriver
import csv

driver = webdriver.Chrome()
BASE_URL = "https://www.goodreads.com/list/show/"
BOOK_LIST = "1.Best_Books_Ever?page="

f = open("best_books_titles.csv", 'w', encoding='UTF-8')
csv_writer = csv.writer(f)
csv_writer.writerow(["Title", "Author", "Rating"])
titles = []
for page in range(1, 525):
    driver.get(f'{BASE_URL}{BOOK_LIST}{page}')
    for i in range(1, 101):

        # dictionary to write consistently to csv
        # should start with keys pointint to Nones
        # there will be check to make sure the value is being written to the right key
        # can write Nones so we dont get bad data

        title = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/a/span')
        author = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/span[2]')
        rating = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/div[1]/span/span')

        # print(title.text, author.text, rating.text)

        csv_writer.writerow([title.text, author.text, rating.text])


f.close()
driver.close()
