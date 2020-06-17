from selenium import webdriver
import csv

driver = webdriver.Chrome()

BASE_URL = "https://www.goodreads.com/list/show/"
BOOK_LIST = "1.Best_Books_Ever?page="

# f = open("best_books_details.csv", 'w', encoding='UTF-8')

driver.get(f'{BASE_URL}{BOOK_LIST}1')

for i in range(1, 101):

