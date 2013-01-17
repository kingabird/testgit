poem = '''\
Programming is fun
When the work is done
if you wanna make your work akso fun:
		use Python! Hahahahah.
'''

f = file('/Users/kingabird/Sites/python/poem.txt', 'w') # open for 'w'riting
f.write(poem) # write text fo file
f.close() # close the file

f = file('/Users/kingabird/Sites/python/poem.txt')
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print line,
f.close


########