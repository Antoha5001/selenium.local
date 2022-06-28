from bs4 import BeautifulSoup as bs
import json
import requests


# links = []

# for i in range(0, 720, 20):
# 	url = f"https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}"

# 	resp = requests.get(url)
# 	page = bs(resp.text, 'lxml')

# 	mans = page.findAll(class_='bt-open-in-overlay')

# 	for man in mans:

# 		link = man.get('href')

# 		links.append(link)

# 		print(f"{count} : link - {link}")

# 		count = count + 1

count = 0
people = []

with open('links_bundestag.txt', 'rt', encoding='utf-8') as file:
	

	links = [link.strip() for link in file.readlines()]

	for link in links:

		resp = requests.get(link)		

		page = bs(resp.content, 'lxml')
		h3 = page.find(class_="bt-biografie-name").find('h3').text.strip()
		# print(h3)
		name_partia = h3.split(",")
		name = name_partia[0].strip()
		partia = name_partia[1].strip()
		socials = [link.get('href').strip() for link in page.findAll(class_='bt-link-extern')]

		man = {
			'name' : name,
			'partia' : partia,
			'links' : socials
		}

		people.append(man)

		print(f"{count} - User: {man}")
		count += 1
		# print(partia)


with open('bundestag.json', 'w', encoding='utf-8') as js:
	json.dump(people, js)
