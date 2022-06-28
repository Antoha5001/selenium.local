from bs4 import BeautifulSoup as bs
import json
import requests

headers = {
	'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
	'Accept' : '*/*'
}

links = []

count = 0
for i in range(0, 216, 24):
	url = f"https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=&to_date=&maxprice=500&o={i}&bannertitle=June"

	resp = requests.get(url, headers=headers)

	# print(resp.text)
	# with open('fest.txt', 'w', encoding='utf-8') as file:
	# 	file.write(resp.text.replace('\\',''))
	# break
	page = bs(resp.text.replace('\\',''), 'lxml')

	links_fest = page.findAll(class_='card-details-link')

	print(links_fest)	

	for link in links_fest:	
		link = link.get('href')

		links.append(f"https://www.skiddle.com{link}\n")

		print(f"{count} : link - "+f"https://www.skiddle.com{link}\n")

		count = count + 1


with open('links_fest.txt', 'w', encoding='utf-8') as file:
	file.writelines(links)



# people = []

# with open('links_bundestag.txt', 'rt', encoding='utf-8') as file:
	

# 	links = [link.strip() for link in file.readlines()]

# 	for link in links:

# 		resp = requests.get(link)		

# 		page = bs(resp.content, 'lxml')
# 		h3 = page.find(class_="bt-biografie-name").find('h3').text.strip()
# 		# print(h3)
# 		name_partia = h3.split(",")
# 		name = name_partia[0].strip()
# 		partia = name_partia[1].strip()
# 		socials = [link.get('href').strip() for link in page.findAll(class_='bt-link-extern')]

# 		man = {
# 			'name' : name,
# 			'partia' : partia,
# 			'links' : socials
# 		}

# 		people.append(man)

# 		print(f"{count} - User: {man}")
# 		count += 1
# 		# print(partia)


# with open('bundestag.json', 'w', encoding='utf-8') as js:
# 	json.dump(people, js)
