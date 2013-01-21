#!/usr/bin/python

# months = ['January', 'Februay', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# endings = ['st', 'nd', 'rd'] + 17 * ['th']\
# 		+ ['st', 'nd', 'rd'] + 7 * ['th']\
# 		+ ['st']

# print ['haha', 'daadf', '123'] + ['4444']

# year = raw_input('Year: ')
# month = raw_input('Month: ')
# day = raw_input('Day (1-31): ')

# month_number = int(month)
# day_number = int(day)

# month_name = months[month_number-1]
# ordinal = day + endings[day_number-1]

# print month_name + ' ' + ordinal + ', ' + year

# print months[8:5:-1]

# url = 'http://www.yeeyan.org'
# print url[7:]

# if 'http://' in url:
# 	print 'hahaha, http is here.'

# sentence = raw_input('Enter somethings: ')

# screen_width = 40
# text_width = len(sentence)
# box_width = text_width + 6
# left_margin = (screen_width - box_width) // 2

# print
# print ' ' * left_margin + '+' + '-' * (box_width-4) +  '+'
# print ' ' * left_margin + '| ' + ' ' * text_width   + ' |'
# print ' ' * left_margin + '| ' + 	  sentence      + ' |'
# print ' ' * left_margin + '| ' + ' ' * text_width   + ' |'
# print ' ' * left_margin + '+' + '-' * (box_width-4) +  '+'
# print

# database = [['alert', '1234'], ['dilber', '4242'], ['smith', '7654'], ['jones', '9823']]
# username = raw_input('User name: ')
# pin = raw_input('PIN code: ')
# conment = [username, pin]

# if conment in database:
# 	print 'Access granted.'
# else:
# 	print 'It\'s wrong!'

lst = [1, 2, 3, 4, 5, 4]
new_lst = ['last', 'lala', 'y']

print 'This is currently list: ', lst

# new element
lst.extend(new_lst)
print 'This extend list: ', lst

# element counts
print '4 has appeared count', lst.count(4)
# element index
print '4 appear', lst.index(4)

lst.insert(2, 'insert')
print lst

print lst.pop(3)
print lst

lst.remove('last')
print lst

lst.reverse()
print lst

new_lst = lst[:]
new_lst.sort()
new_lsted = sorted(lst)
print new_lsted
print new_lst