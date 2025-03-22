
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")


print(soup.prettify())

# 3 --------------------------------------

headings = 0
for i in range(1, 7):
    headings += len(soup.find_all(f"h{i}"))

print(f"Number of headings: {headings}")

links = 0
links += len(soup.find_all(f"a"))
print(f"Number of links: {links}")

paragraphs = 0
paragraphs += len(soup.find_all(f"p"))
print(f"Number of paragraphs: {paragraphs}")

# 4 -------------------------

text = soup.get_text()
raw_words = text.split()
words_clean = []

for word in raw_words:
    cleaned = "".join(ch for ch in word if ch.isalnum()).lower()
    if cleaned:
        words_clean.append(cleaned)

search = input("Enter keyword: ").strip().lower()

search_count = words_clean.count(search)

print(f"The keyword {search} appears {search_count} times")


# 5 -------------------------------

word_frequencies = {}

for word in words_clean:
    word_frequencies[word] = word_frequencies.get(word, 0) + 1

top_five_words = sorted(word_frequencies, key=word_frequencies.get, reverse=True)[:5]

print("Top 5 words with most frequencies:")
for word in top_five_words:
    print(f"{word}: {word_frequencies[word]}")

# 6 -------------------------------








# 7 ------------------------------
labels = ['Headings', 'Links', 'Paragraphs']
values = [headings, links, paragraphs]
plt.bar(labels, values)
plt.title('Group# 35')
plt.ylabel('Count')
plt.show()
