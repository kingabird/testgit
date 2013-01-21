#! /usr/bin/python

url = 'http://%s.yeeyan.%s'
values = ('www', 'com')
print url % values

from math import pi
print '%010.5f' % pi

# from string import Template
# s = Template('$x, golrius $x!')
# s.substitute(x='slurm')
# print s


width = 50
pritc_width = 10
item_width = width - pritc_width

hearder_format = '%-*s%*s'
format = '%-*s%*.2f'

print '=' * width
print hearder_format % (item_width, 'Item', pritc_width , 'Price')
print '-' * width
print format % (item_width, 'Pears', pritc_width , 0.5)
print format % (item_width, 'Apples', pritc_width , 0.4)
print format % (item_width, 'Cantaloupes', pritc_width , 1.92)
print '=' * width

name = 'My girlfriend is Carina.'
print url.find('www')
print name.find('girl')

print '+'.join(name)
print name.lower()
print name.title()
print name.replace('Carina', 'CARINA')
print name.split(' ')
# print name.translate(table, ' ')

name_strip = '     haha ha  hah dsfd df dfd      '
print name_strip
print name_strip.strip()

