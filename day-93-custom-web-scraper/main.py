from bs4 import BeautifulSoup
import requests

# The BBC’s List of the Most Impactful Novels
web_url = ("https://www.penguinrandomhouse.com/the-read-down/the-bbcs-impactful-novels/")

response = requests.get(web_url)
web_page_html = response.text
soup = BeautifulSoup(web_page_html, "html.parser")

author_book_lines = soup.find_all(name="h2")

author_book_names = []
for line in author_book_lines:
    a_tag = line.find("a")
    if a_tag:
        author_book_names.append(a_tag.text)

books_array = author_book_names[1::2]
authors_array = author_book_names[2::2]


for i in range(len(books_array)):
    with open("most_impactful_books_of_all_time.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{books_array[i]} - {authors_array[i]} \n")
