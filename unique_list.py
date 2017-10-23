#This script is used to make a sub-list with the unique elements taken from the existing list.

def uniq_list(): #defining a function
	x = [] #Take an empty list which holds the uniq elements
	for a in l: #a iterates every element in the given list
		if a not in x: #checking if the iterative element is already presents in x
			x.append(a) #if 'a' is not present in x then it will get added to x

	return x #returning the x which is a unique list now


