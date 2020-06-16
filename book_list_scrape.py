from selenium import webdriver
import csv

driver = webdriver.Chrome()
BASE_URL = "https://www.goodreads.com/list/show/"
BOOK_LIST = "1.Best_Books_Ever?page="

f = open("best_books_titles.csv", 'w', encoding='UTF-8')
csv_writer = csv.writer(f)
csv_writer.writerow(["Title", "Author", "Rating"])
titles = []
for page in range(1, 5):
    driver.get(f'{BASE_URL}{BOOK_LIST}{page}')
    for i in range(1, 101):
        title = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]')
        title_list = title.text.split("\n")
        csv_writer.writerow(title_list)
# print(dir(title))
# Harry Potter and the Order of the Phoenix -> //*[@id="all_votes"]/table/tbody/tr[2]/td[3]
# The Hunger Games -> //*[@id="all_votes"]/table/tbody/tr[1]/td[3]
# Moby Dick (page 2) -> //*[@id="all_votes"]/table/tbody/tr[1]/td[3]
f.close()
hunger_games = titles[0]

print(hunger_games.text.split('\n'))
driver.close()
