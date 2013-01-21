#!/usr/bin/python

#Filename : helloworld.py
#####
#####

print 'Hello World'

print r'This is what??? """hahahhahah/"""' '\\ '



# i = 5
# print i
# i = i + 1
# print i

# s = '''This is a multi-line string.
# This is the second line.'''
# print s

# ss = 'This is a string. \
# This continues the string.'
# print ss

# lenght = 5
# breadth = 2
# area = lenght * breadth
# print 'Area is',area
# print 'Perimeter is', 2 * (lenght + breadth)

# number = 23

# if =========================================
# guess = int(raw_input('Enter an integer : '))

# if guess == number:
# 	print 'Congratulatinos, you guessed it.'
# 	print "(But you do not win any prizes!)"
# elif guess < number:
# 	print 'No, it is a litter higher than that'
# else:
# 	print 'No, it is a littler lower than that'

# print 'Done'

running = True

# while =========================================
# while running:
# 	guess = int(raw_input('Enter an integer : '))

# 	if guess == number:
# 		print 'Congratulatinos, you guessed it.'
# 		running = False
# 	elif guess < number:
# 		print 'No, it is a litter higher than that'
# 	else:
# 		print 'No, it is a littler lower than that'
# else:
# 	print 'The while loop is over.'

# print 'Done'

# for =========================================

# for i in range(1,10,2):
# 	print i
# else:
# 	print 'The for loop is over.'


# break, continue =========================================
# while True:
# 	s = raw_input('Enter something : ')
# 	if s == 'quit':
# 		break
# 	if len(s) < 3:
# 		print 'Input is of sufficient lenght'
# 		continue
# 	else:
# 		print 'Lenght of the string is', len(s)

# print 'Done'

# def sayHello(name):
# 	print 'Hello,', name

# sayHello('ning')

# def printMax(a, b):
# 	if a > b:
# 		return a
# 	else:
# 		print b, 'is maximun'

# printMax(2, 4)

# x = 80
# y = 7
# print printMax(x, y)

# def func(x):
# 	print 'x is ', x
# 	x = 2
# 	print 'Changed local x to ', x

# y = 50
# func(y)
# print 'x is still', y

# def say(message = 'ning', times = 1):
# 	print message * times

# say()
# say('fuck ', 5)

# def funx(a, b = 5, c =10):
# 	print 'a is', a, 'and b is', b, 'and c is ', c

# funx(1)
# funx(3,7)
# funx(23, c = 38)
# funx(c = 70, a = 10)

def printMax(x, y):
	'''Prints the maximum of two numeber.

	The two values must be integers.'''
	x = int(x)
	y = int(y)

	if x > y:
		print x, 'is maximum'
	else:
		print y, 'is maximum'

printMax(3, 5)
print printMax.__doc__
# help(printMax)