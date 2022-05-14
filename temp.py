from itertools import count
import math

from datetime import date
from settings import categories

title = "422 X 101 ЕВРООТКРЫТКА"

category = False

for cat in categories:

	if title == cat["title"]:
		category = cat["category"]

print(category)