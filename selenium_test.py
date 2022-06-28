# from curses import echo
import imp
from itertools import count
from tkinter import Button
from selenium import webdriver  
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import date
import pickle
import pandas as pd
from datetime import date
import sqlalchemy
import math

from settings import categories as file_categories
from functions import titleChangeSizeAfterName

options = webdriver.ChromeOptions()
# options.add_argument("User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36")
options.add_argument("start-maximized") 
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome("driver/chromedriver.exe", options=options)


driver.get('https://sborka.run/')

for cookie in pickle.load(open('cookies.txt', 'rb')):
	driver.add_cookie(cookie)
	
time.sleep(2)
driver.refresh()

time.sleep(2)

button = driver.find_element(by=By.XPATH, value="//div[@class='btn_block']/child::a[3]/div")
# button = driver.find_element_by_class_name("btn_log_in")
time.sleep(2)
button.click()
time.sleep(2)

drp_reg = Select(driver.find_element(by=By.XPATH, value="//select[@name='region']"))
drp_reg.select_by_visible_text('Алтайский край')
time.sleep(1)


drp_reg2 = Select(driver.find_element(by=By.XPATH, value="//select[@name='city']"))
drp_reg2.select_by_visible_text('Барнаул')

time.sleep(2)

pickle.dump(driver.get_cookies(), open('cookies.txt', 'wb'))
button_enter = driver.find_element(by=By.XPATH, value="//select[@name='city']/parent::div/following-sibling::button")
time.sleep(1)
button_enter.click()

time.sleep(3)

categories = driver.find_elements(by=By.XPATH, value="//span[@otype='offset']/div/div")[1:]

dataframes = []

count = 1

engine = sqlalchemy.create_engine("mysql://pythonless:pythonless@localhost/623030")

today = date.isoformat(date.today())

with pd.ExcelWriter(f"{today}_result.xlsx") as writer:

	for category in categories:

		driver.implicitly_wait(3)
		driver.execute_script("arguments[0].click()", category)
		time.sleep(3)

		items = []

		# Заголовок
		title = driver.find_element(by=By.XPATH, value="//div[@class='offset-title']").text

		if title == "НАКЛЕЙКИ И СТИКЕРЫ" or title == "БЛОКИ ДЛЯ ЗАПИСЕЙ":
			continue

		table_name = False
		category_file = False
		title_eng = False

		# Категории из файла
		for cat in file_categories:
			if title == cat["title"]: 
				table_name = cat["table_name"]
				category_file = cat["category"]
				category_id = cat["category_id"]
				title_eng = cat["title_eng"]

		if table_name == False:
			print("!!!!!!!!! table_name=FALSE")

		if title_eng == False:
			title_eng = title

		tables = driver.find_elements(by=By.XPATH, value="//div[@class='material']")

		for table in tables:
			papper = table.find_element(by=By.CLASS_NAME, value="new_tooltip").text

			theads = table.find_elements(by=By.TAG_NAME, value="tr")[0]
			theads_td = theads.find_elements(by=By.TAG_NAME, value="td")[1:-1]

			# print(f"!!!!!!!!!!!!!! theads_td {theads_td[0].text}")
			# exit()
			one_side = table.find_element(by=By.XPATH, value="self::node()//tbody/tr[@class='one'][1]")
			time_to_done = one_side.find_element(by=By.XPATH, value="self::node()//td[@class='time_to_parse']").text
			# one_side_td = one_side.find_elements(by=By.XPATH, value="self::node()//td[@class='time_to_parse']").text
			one_side_td = one_side.find_elements(by=By.XPATH, value="self::node()//span[@class='rub']")


			obj = {
				"id": count,
				"title": titleChangeSizeAfterName(title),
				"done" : time_to_done,
				"papper" : papper,
				"colors" : "4+0",
				"category": category_file,
				"category_id": category_id,
				"date" : date.today().strftime("%d.%m.%Y")
			}

			count = count+1

			for td in range(0,len(one_side_td)):
				price_str = one_side_td[td].text
				price_list = price_str.split()
				price = int("".join(price_list))

				print(f"price: {price}")
				print(f"td: {td}")
				print(f"theads_td: {theads_td}")
				
				obj[f"sborka_{theads_td[td].text}"] = price
				obj[f"{theads_td[td].text}"] = round(math.ceil(price+price/100*20), -1)
				# print("!!!!!!!!!!!!!! thead: " + theads_td[td].text + f" / price: {price}")
			
				# print(prise)

			# print(f"one_side: {one_side}")
			items.append(obj)
			# print(obj)


			two_side = table.find_element(by=By.XPATH, value="self::node()//tbody/tr[@class='two'][1]")
			time_to_done2 = two_side.find_element(by=By.XPATH, value="self::node()//td[@class='time_to_parse']").text
			# two_side_td = two_side.find_elements(by=By.TAG_NAME, value="span")[:-1]			
			two_side_td = one_side.find_elements(by=By.XPATH, value="self::node()//span[@class='rub']")


			obj2 = {
				"id": count,
				"title": titleChangeSizeAfterName(title),
				"done" : time_to_done2,
				"papper" : papper,
				"colors" : "4+4",
				"category": category_file,
				"category_id": category_id,
				"date" : date.today().strftime("%d.%m.%Y")
			}
			
			count = count+1

			for td in range(0,len(two_side_td)):
				price_str = two_side_td[td].text
				price_list = price_str.split()
				price = int("".join(price_list))

				
				obj2[f"sborka_{theads_td[td].text}"] = price
				obj2[f"{theads_td[td].text}"] = round(math.ceil(price+price/100*20), -1)
				

			items.append(obj2)

			print(items)
		
		dataframes.append(pd.DataFrame(items))

		df = pd.DataFrame(items)
		time.sleep(1)
		df.to_excel(writer, sheet_name=title_eng, index=None)

		# df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
		df.to_sql(name="ofset", con=engine, if_exists='append', index=False)


		
		time.sleep(3)

	



# ActionChains(driver).move_to_element(categories).click(button).perform()
# print(categories)
try:	
	# categories.click()
	pass
except ElementNotInteractableException as e:
	# print(f"Ошибка: {e}")
	pass
finally:
	pass