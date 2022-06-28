
links = ['https://123','https://567','https://890',]


with open('links_bundestag.txt', 'w', encoding='utf-8') as file:
	file.writelines([link+"\n" for link in links])

