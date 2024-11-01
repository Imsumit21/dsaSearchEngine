import time
import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.interviewbit.com/coding-interview-questions/")

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
all_ques_div = soup.findAll('div', {"class": "pl-problem-tile"})
# print(all_ques_div)
all_ques = []
urls = []
titles = []
for ques in all_ques_div:
    s = ques.find('a',{"class": "pl-problem-tile__statement"})
    if (s == None) :
        continue
    all_ques.append(s)


for ques in all_ques:
    print(ques)
#     urls.append("https://www.interviewbit.com"+ques['href'])
#     titles.append(str(ques.text.encode("utf-8")))
#
# with open("IB_problem_urls.txt", "w+") as f:
#    f.write('\n'.join(urls))
#
# with open("IB_problem_titles.txt", "w+") as f:
#    f.write('\n'.join(titles))
#
#
#
# cnt = 0
# for url in urls:
#     driver.get(url)
#     time.sleep(2)
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#     problem_text = soup.find('div', {"id": "problem_description_markdown_content_value"})
#     if problem_text==None:
#         problem_text = soup.find('div', {"class": "p-html-content__container"})
#     if problem_text==None:
#         continue
#     cnt += 1
#     main_text = problem_text.get_text()
#     main_text = main_text.encode("utf-8")
#     main_text = str(main_text)
#
#     with open("IB_problem" + str(cnt) + ".txt", "w+") as f:
#         f.write(main_text)

