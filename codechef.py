import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup  # Make sure to import BeautifulSoup

# Set up ChromeDriver using Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Initialize lists to hold URLs and titles
urls = []
titles = []
cnt = 1016

for i in range(20, 71):
    driver.get("https://www.codechef.com/practice?page=" + str(i) + "&limit=50&sort_by=difficulty_rating&sort_order=asc&search=&start_rating=0&end_rating=5000&topic=&tags=&group=all")
    time.sleep(5)

    # Get page source and create BeautifulSoup object
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Find all relevant question divs
    all_ques_div = soup.findAll("tr", {"class": "MuiTableRow-root"})
    all_ques = []

    for ques in all_ques_div:
        question = ques.find("a", {"class": "PracticePage_m-link__xLfvv"})
        if question is None:
            continue
        all_ques.append(question)

    # Collect URLs and titles
    for ques in all_ques:
        urls.append(ques['href'])
        titles.append(ques.text.strip())  # Use strip() to clean up the text

# Loop through collected URLs to scrape problem statements
for url in urls:
    driver.get(url)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extract the main text of the problem statement
    main_text_div = soup.find('div', {"id": "problem-statement"})
    if main_text_div:  # Ensure the div is found
        main_text = main_text_div.get_text(strip=True)  # Strip whitespace
    else:
        main_text = "Problem statement not found."

    # Increment counter and save to file
    cnt += 1
    with open("cc_problem_" + str(cnt) + ".txt", "w", encoding='utf-8') as f:  # Specify encoding
        f.write(main_text)

# Close the browser after scraping
driver.quit()
