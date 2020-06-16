from selenium import webdriver

driver = webdriver.Chrome()
BASE_URL = "https://www.goodreads.com/list/show/"

first_page = "1.Best_Books_Ever"
driver.get(BASE_URL + first_page)

titles = []
for i in range(1, 101):
    title = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]')
    titles.append(title)
# print(dir(title))

for i, title in enumerate(titles):
    if i % 5 == 0:
        print(f"Book {i}: {title.text}")

driver.close()
