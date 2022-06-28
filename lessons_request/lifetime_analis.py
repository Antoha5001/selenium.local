
from unicodedata import category
import requests
import json
import csv
from datetime import datetime

today = datetime.today().strftime('%d-%m-%Y_%M%S')
file_name = today+'_med.csv'
print(file_name)
categories = requests.get('https://www.lifetime.plus/api/analysis2').json()['categories']

items = []

for category in categories:
	cat_name = category.get('name')

	cat_items = category.get('items')

	for item in cat_items:

		item_name = item.get('name')
		item_price = item.get('price')
		item_days = item.get('days')
		item_biomaterial = item.get('biomaterial')
		item_description = item.get('description')
		item_preparationGuide = item.get('preparationGuide', '')

		ready_item = [cat_name ,item_name, item_price, item_days, item_biomaterial, item_description, item_preparationGuide]
		
		items.append(ready_item)

print(items)

# print('Ok0')
with open( file_name, 'wt', encoding= 'utf-8', newline='') as file:
	print('Ok1')
	writer = csv.writer(file, delimiter=',')
	writer.writerow(['Категория','Название','Цена','Дней на анализ','Биоматериал','Описание','Требуется для подготовки'])
	print('Ok')
	writer.writerows(items)

		

