title = "422 X 101 ЕВРООТКРЫТКА"

def titleChangeSizeAfterName(title):
		
	title_list = title.split(" ")
	title_dict = dict(enumerate(title_list))
	

	# print(type(title_dict[0]))

	for el in title_dict:
		# print(title_dict[el]);
		try:		
			title_dict[el] = int(title_dict[el])-2
				
		except Exception as e:
			pass
			# print("Не число")
	
	title = " ".join(title_list[3:]) + " "  + "".join( [str( title_dict[0]), str(title_dict[1]).lower(), str(title_dict[2])] )

	return title

print(titleChangeSizeAfterName(title))
# category = False

# for cat in categories:

# 	if title == cat["title"]:
# 		category = cat["category"]

# print(category)