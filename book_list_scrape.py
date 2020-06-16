from selenium import webdriver

driver = webdriver.Chrome()
BASE_URL = "https://www.goodreads.com/list/show/"

first_page = "1.Best_Books_Ever"
driver.get(BASE_URL + first_page)

titles = []
for i in range(1, 101):
    title = driver.find_element_by_xpath(f'//*[@id="all_votes"]/table/tbody/tr[{i}]/td[3]')
    titles.append(title)
# print(dir(title))
# Harry Potter and the Order of the Phoenix -> //*[@id="all_votes"]/table/tbody/tr[2]/td[3]
# The Hunger Games -> //*[@id="all_votes"]/table/tbody/tr[1]/td[3]
hunger_games = titles[0]

print(hunger_games.text.split('\n'))
driver.close()
