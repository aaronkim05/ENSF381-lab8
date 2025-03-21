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

# count = input("Enter keyword to find count of it in webpage: ")
# count_user_input = 0
# count_user_input += len(soup.find_all(count))

# print(f"The user input is count is {count_user_input}")

extracted_text = soup.get_text().split()

new_list = []
for stuff in extracted_text:
    new_list.append(stuff.lower())
print(new_list)

new_list_copy = new_list.copy()

brand_new_list = []

for i in new_list_copy:
    if i not in brand_new_list:
        brand_new_list.append(i)


print(brand_new_list)


empty_array = []
for i in brand_new_list:
    count = 0 
    while i in new_list_copy:
        new_list_copy.remove(i)
        count += 1

    empty_array.append(count)
    print(f"Frequency for {i} is: {count}")

print(empty_array)

most_frequent_in_order = []

for i in range(5):
   
    frequent1 = max(empty_array)

    frequent1_index = empty_array.index(frequent1)
    most_frequent_in_order.append(brand_new_list[frequent1_index])
    empty_array.pop(frequent1_index)

print(most_frequent_in_order)


# Possible solutions at the bottom 

# for keywords -- I think this is what they meant (but its copied) (maybe we should ask prof what exactly they mean)

cleaned_words = []
for word in words:
    clean_word = "".join(char for char in word if char.isalnum())
    if clean_word:
        cleaned_words.append(clean_word)











