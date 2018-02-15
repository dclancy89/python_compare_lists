# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']



# by default assume they are the same.
areTheSame = True


#if they aren't the same length, the can't be the same
if len(list_one) == len(list_two):
	#check the list items against each other
	for i in range(len(list_one)):
		if list_one[i] != list_two[i]:
			print "The lists are not the same"
			areTheSame = False
			break;
	if areTheSame:
		print "The lists are the same"
else:
	areTheSame = False
	print "The lists are not the same"