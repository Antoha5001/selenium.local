import sqlalchemy
import pandas as pd

from settings import categories

df = pd.DataFrame(categories, index=None)


engine = sqlalchemy.create_engine("mysql://pythonless:pythonless@localhost/623030")

df.to_sql(name="categories", con=engine)

# print(df)