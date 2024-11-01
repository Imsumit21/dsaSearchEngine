import time
import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://codeforces.com/problemset?f0a28=1")

time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
all_ques_div = soup.findAll("tr")
# print(all_ques_div[1].findAll("td"))
cnt=1
all_ques=[]
cnt = 0
for ques in all_ques_div:
  if cnt == 0:
    cnt = cnt + 1
    continue
  question=ques.findAll("td")
  all_ques.append(question[1].findAll("div")[0].find("a"))
  cnt+=1
  if cnt==101:
    break



urls = []
titles = []

for ques in all_ques:
   urls.append("https://codeforces.com/"+ques['href'])
   titles.append(str(ques.text.encode("utf-8")))

with open("cf_problem_urls.txt", "w+") as f:
   f.write('\n'.join(urls))

with open("cf_problem_titles.txt", "w+") as f:
   f.write('\n'.join(titles))
cnt=0
for url in urls:
    driver.get(url)
    cnt += 1
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    problem_text = soup.find('div', {"class": "problem-statement"})
    main_text=problem_text.findAll('div')[10].get_text()
    main_text = main_text.encode("utf-8")
    main_text = str(main_text)

    with open("cf_problem" + str(cnt) + ".txt", "w+") as f:
        f.write(main_text)

    if cnt==2:
        break
