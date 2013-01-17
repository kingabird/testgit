# class Person:
# 	def sayHi(self):
# 		print 'Hello, how are you?'

# p = Person()
# p.sayHi()
#

class Person(object):
	"""Represents a person"""
	population = 0

	def __init__(self, name):
		"""Initializes the person's data."""
		self.name = name
		print '(Initailizing %s)' % self.name

		# When this person is creted, he/she adds to the population
		Person.population += 1

	def __del__(self):
		'''I am dying.'''
		print '%s says bye.' % self.name

		Person.population -= 1

		if Person.population == 0:
			print 'I am the last one.'
		else:
			print 'There are still %d perple left.' % Person.population

	def sayHi(self):
		'''Greeting by the person.

		Really, that's all it does.'''
		print 'Hello, my name is %s.' % self.name

	def howMany(self):
		'''Prints the current population.'''
		if Person.population == 1:
			print 'I am the only person here.'
		else:
			print 'We have %d persons here.' % Person.population


# swaroop = Person('Swaroop')
# swaroop.sayHi()
# swaroop.howMany()

# # kalam = Person('Abdul Kalam')
# # kalam.sayHi()
# # kalam.howMany()

# swaroop.sayHi()
# swaroop.howMany()

class SchoolMember:
	"""Repressents any school member"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print '(Initialized SchoolMember: %s)' % self.name

	def tell(self):
		'''Tell my details.'''
		print 'Name: "%s" Age: "%s' % (self.name, self.age)

class Teacher(SchoolMember):
	"""Repressnts a teacher."""
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print 'Initialized Teacher: %s' % self.name

	def tell(self):
		SchoolMember.tell(self)
		print 'Salary: "%d"' % self.salary

class Student(SchoolMember):
	"""Repressnts a student."""
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self,name, age)
		self.marks = marks
		print '(Initialized Student: %s)' % self.name

	def tell(self):
		SchoolMember.tell(self)
		print 'Marks: "%d"' % self.marks

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swarrop', 22, 75)

members = [t, s]
for member in members:
	member.tell()