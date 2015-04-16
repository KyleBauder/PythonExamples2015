import os
import sys
import math

"""Kyle Bauder April 16, 2015

Exercise 7: create a function called is_anagram
which takes two different strings and rearranges
them to see if they are an anagram of the other.

The two arguments should be strings, although
they will also work with integers.

I've added in print statements to show what it is
doing, although you can take those out if it
muddies up your code. 


This exercise was taken from the online 
Think Python book, although I worked it out myself.
http://www.greenteapress.com/thinkpython/html/thinkpython011.html

You can try out some of weird Al's anagrams from here:
http://www.azlyrics.com/lyrics/weirdalyankovic/bob.html


"""
def replacer(x):
	"""takes a comma, colon, question mark, etc.
	out of a string"""
	xo = x.lower()
	xnew = xo.replace(" ","")
	xnew2 = xnew.replace(",","")
	xnew3 = xnew2.replace("?","")
	xnew4 = xnew3.replace(";","")
	xnew5 = xnew4.replace(":","")
	xnew6 = xnew5.replace("!","")
	xnew7 = xnew6.replace("'","")
	print(xnew7)
	return xnew7

def string_tointegerlist(xstr):
	"""turns a string into a list of characters
	then a list of integers representing each
	character. Useful for comparing strings"""
	#Create a new "string" variable
	x_string = str(xstr)
	x_list = []
	#creates an empty list for this string
	base = ord('0')
	"""we grab the ord('0') because all numbers
	are grouped together. If we can subtract the
	ord('0') we can get the number"""
	
	#turns every letter into a value
	for char in x_string:
		x_list.append(ord(char)-base)	
	return x_list

def is_anagramdebug(a,b,c,d):
	#these are just printing off the values for
	#debugging. You can get rid of these if you
	#like.
	print(a)
	print(b)
	print(' ')
	print(c)
	print(d)
	print('  ')	
	
def is_anagram(list_f,list_s):
	#first strips them of unnecessary symbols	
	listf_replace = replacer(list_f)
	lists_replace = replacer(list_s)

	#then converts the string to a list of integers
	listf_list = string_tointegerlist(listf_replace)
	lists_list = string_tointegerlist(lists_replace)

	#optional debug to print off values
	is_anagramdebug(listf_replace,listf_list,lists_replace,lists_list)	
	
	#Sorts the list so they are lowest to highest
	#in values. 
	listf_list.sort()
	lists_list.sort()
	
	#prints them again to see how they compare
	print(listf_list)
	print(lists_list)
	
	n = 1
	cond = 0
	
	"""first check if the lengths are the same
	length. They can't be an anagram if they
	are different lengths"""
	if len(listf_list) == len(lists_list):
		for n in range(len(listf_list)):
		#go through each index value to see if
		#they compare [0] = [0]; [1] = [1], etc.
			if listf_list[n] == lists_list[n]:
				cond +=1
				#adds up if they equal
				
		if cond == len(listf_list):
		#if they all are equal
			print('  ')
			print('Is an anagram')
		else:
			print('  ')
			print('Is not an anagram')
	else:
		print('   ')
		print('Is not an anagram')
	
	
list_f = "Go hang a salami,"
list_s = "I'm a lasagna hog!"
is_anagram(list_f,list_s)
