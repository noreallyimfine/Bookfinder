from selenium import webdriver
import csv

driver = webdriver.Chrome()
BASE_URL = "https://www.goodreads.com/list/show/"
BOOK_LIST = "1.Best_Books_Ever?page=2"

f = open("best_books_titles_missing.csv", 'w', encoding='UTF-8')
csv_writer = csv.writer(f)
csv_writer.writerow(["Title", "Author", "Rating"])
driver.get(f'{BASE_URL}{BOOK_LIST}')
for i in range(1, 101):
    title = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/a/span')
    author = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/span[2]')
    rating = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]/div[1]/span/span')

    # print(title.text, author.text, rating.text)

    csv_writer.writerow([title.text, author.text, rating.text])


f.close()
driver.close()