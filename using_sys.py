# import sys

# print 'The command line arguments are:'
# for i in sys.argv:
# 	print i

# print '\n\nThe PYTHONPATH is', sys.path, '\n'

# if __name__ == '__main__':
# 	print 'This program is being run by itself'
# else:
# 	print 'I am being import from another module'

from mymodule import sayhi, version

sayhi()
print 'Version', version

# This is my shoping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(shoplist), 'items to purchase.'

print 'These items are:',
for item in shoplist:
	print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shoping list is now,', shoplist

print 'I will sort my list now'
shoplist.sort()
print 'Socted shoping list is', shoplist

print 'The first item I will buy is', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shoping list is now', shoplist

# 'ab' is short for 'a'ddress'b'ook

ab = {
		'Swaroop':'Swaroop@byteofpython.info',
		'Larry':'Larry@byteofpython.info',
		'Matsumoto':'Matsumoto@byteofpython.info',
		'Spammer':'Spammer@byteofpython.info',
	}

print "\nSwaroop's address is %s" % ab['Swaroop']

# Adding a key/value pair
ab['Guido'] = 'guido@python.org'

# Deleting a key/value pair
del ab['Spammer']

print '\nThere are %d contacts in the address-book\n' % len(ab)
for name, adress in ab.items():
	print 'Contact %s at %s' % (name, adress)

if 'Guido' in ab:
	print "\nGuido's address is %s" % ab['Guido']