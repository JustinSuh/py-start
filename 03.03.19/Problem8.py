def accum(letters):
	newletters = ""
	for i in range(0,len(letters)):
		if i==0:
			newletters+=letters[i].upper()
		else:
			newletters+=("-"+letters[i].upper()+letters[i].lower()*i)
	print(newletters)
