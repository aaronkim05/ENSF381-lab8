
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

print(f"Number of: {headings}")

links = 0
links += len(soup.find_all(f"a"))
print(f"Number of links: {links}")

paragraphs = 0
paragraphs += len(soup.find_all(f"p"))
print(f"Number of paragraphs: {paragraphs}")

# 4 -------------------------

text = soup.get_text()
words = text.lower().split()
key_words = []

for i in words:
    key_word = "".join(char for char in i if char.isalnum())
    if key_word:
        key_words.append(key_word)

user_key_word = input("Enter keyword: ").strip()

key_word_count = key_words.count(user_key_word.lower())

print(f"The keyword {user_key_word} appears {key_word_count} times")


# 5 -------------------------------

word_frequencies = {}

for i in key_words:
    word_frequencies[i] = word_frequencies.get(i, 0) + 1

top_five_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)[:5]

print("Top 5 words with most frequencies:")
for i, j in top_five_words:
    print(f"{i}: {j}")

# 6 -------------------------------








# 7 ------------------------------
labels = ['Headings', 'Links', 'Paragraphs']
values = [headings, links, paragraphs]
plt.bar(labels, values)
plt.title('Put your Group# Here')
plt.ylabel('Count')
plt.show()