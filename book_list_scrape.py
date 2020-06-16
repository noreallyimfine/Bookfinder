from selenium import webdriver
import csv

driver = webdriver.Chrome()
BASE_URL = "https://www.goodreads.com/list/show/"
BOOK_LIST = "1.Best_Books_Ever?page="

f = open("best_books_titles.csv", 'w', encoding='UTF-8')
csv_writer = csv.writer(f)
csv_writer.writerow(["Title", "Author", "Rating"])
titles = []
for page in range(1, 524):
    driver.get(f'{BASE_URL}{BOOK_LIST}{page}')
    for i in range(1, 101):
        title = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]')
        title_list = title.text.split("\n")
        csv_writer.writerow(title_list)


f.close()
driver.close()
