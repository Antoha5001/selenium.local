import csv

from datetime import datetime

today = datetime.today().strftime('%d-%m-%Y_%M%S')

people = [['Иван', 'Иванов', 34],['Сидоров', 'Сидор', 28] ]

with open(today+'.csv', 'wt', encoding='utf-8', newline='') as file:
	writer = csv.writer(file,delimiter=',')

	writer.writerow(['First name', 'Last Name', 'Years'])
	writer.writerows(people)