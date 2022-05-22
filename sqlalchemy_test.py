from numpy import tile
import sqlalchemy
import pandas as pd
from pprint import pprint
from settings import categories

new_categories_set = []

for cat in categories:
	new_categories_set.append(cat['category'])

new_categories_set = set(new_categories_set)	


new_categories = []
for cat in new_categories_set:
	new_categories.append({
		"title" : cat
	}
	)
	

pprint(new_categories)


df = pd.DataFrame(new_categories, index=None)


engine = sqlalchemy.create_engine("mysql://pythonless:pythonless@localhost/623030")

df.to_sql(name="categories", con=engine, if_exists="replace", index=True, index_label='id')