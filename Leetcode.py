import time
import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
urls = []
titles = []
for i in range(47):

    driver.get("https://leetcode.com/problemset/all/?page="+str(i))

    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    all_ques_div = soup.findAll('div', {"role": "row"})
    # print(all_ques_div)
    all_ques = []
    for ques in all_ques_div:
        s = ques.findAll('a',{"class": "h-5 hover:text-primary-s dark:hover:text-dark-primary-s"})
        if (s == None) :
            continue
        all_ques.append(s)


    for question in all_ques:
        for ques in question:
            urls.append("https://leetcode.com"+ques['href'])
            titles.append(str(ques.text.encode("utf-8")))
#
# with open("LC_problem_urls.txt", "w+") as f:
#    f.write('\n'.join(urls))
#
# with open("LC_problem_titles.txt", "w+") as f:
#    f.write('\n'.join(titles))



cnt = 0
for url in urls:
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    problem_text = soup.find('div', {"class": "content__u3I1 question-content__JfgR"})
    cnt += 1
    if problem_text==None:
        print(cnt)
        continue

    # main_text = problem_text.get_text()
    # main_text = main_text.encode("utf-8")
    # main_text = str(main_text)
    #
    # with open("LC_problem" + str(cnt) + ".txt", "w+") as f:
    #     f.write(main_text)

