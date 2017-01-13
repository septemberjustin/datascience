# def add_numbers(x, y):
#     return x + y

# def add_numbers(x,y,z=None):
# 	if (z==None):
# 		return x+y
# 	else:
# 		return x+y+z

# print(add_numbers(1, 2))
# pring(add_numbers(1, 2, 3))

# def add_numbers(x, y, z=None, flag=False):
# 	if(flag):
# 		print('Flag is true!')
# 	if(z==None):
# 		return x+y
# 	else:
# 		return x+y+z

# print(add_numbers(1, 2, flag=False))
# print(add_numbers(1, 2, 3, flag=True))

# def add_numbers(x,y):
# 	return x+y
# a = add_numbers
# print a(1,2)

# x = [1, 'a', 2, 'b']
# print type(x)
# x.append(3.3)
# print(x)

# for item in x:
#     print(item)

# i=0
# while (i != len(x)):
# 	print(x[i])
# 	i = i + 1

# print [1, 2] + [3, 4]

# print [1]*3

# print 1 in [1, 2, 3]

# x = 'This is a string'
# print(x[0])
# print(x[0:1])
# print(x[0:2])

# firstname = 'Christopher'
# lastname = 'Brooks'

# print(firstname + '' + lastname)
# print(firstname*3)
# print('Chris' in firstname)

# firstname = 'Christopher Arthur Hansen Brooks'.split('')[0]
# lastname = 'Christopher Arthur Hansen Brooks'.split('')[-1]

# x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
# print x['Christopher Brooks']

# x['Kevyn Collins-Thompson'] = None
# print x['Kevyn Collins-Thompson']

# for name in x:
#     print(x[name])

# for email in x.values():
# 	print(email)

# for name, email in x.items():
# 	print(name)
# 	print(email)

# x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
# fname, lname, email = x
# print fname
# print lname

# sales_record = {'price': 3.24, 'num_items': 4, 'person': 'Chris'}
# sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'
# print(sales_statement.format(sales_record['person'],
# 	                         sales_record['num_items'],
# 	                         sales_record['price'],
# 	                         sales_record['num_items']*sales_record['price']))

# import csv

# %precision 2

# with open('mpg.csv') as csvfile:
# 	mpg = list(csv.DictReader(csvfile))

# mpg[:3]
# len(mpg)
# mpg[0].keys()

# sum(float(d['cty']) for d in mpg) / len(mpg)
# sum(float(d['hwy']) for d in mpg) / len(mpg)
# cylinders = set(d['cyl'] for d in mpg)
# cylinders

# CtyMpgByCyl = []
# for c in cylinders: 
# 	summpg = 0
# 	cyltypecount = 0
# 	for d in mpg:
# 		if d['cyl'] == c:
# 			summmpg += float(d['cty'])
# 			cyltypecount += 1
# 	CtyMpgByCyl.append((c, summpg / cyltypecount))

# CtyMpgByCyl.sort(key=lambda x: x[0])
# CtyMpgByCyl

# vehicleclass = set(d['class'] for d in mpg)
# vehicleclass

# HwyMpgByClass = []

# for t in vehicleclass:
# 	summpg = 0
# 	vclasscount = 0
# 	for d in mpg:
# 		if d['class'] == t:
# 			summpg += float(d['hwy'])
# 			vclasscount += 1
# 	HwyMpgByClass.append((t, summpg / vclasscount))

# HwyMpgByClass.sort(key=lambda x: x[1])
# HwyMpgByClass

# import datetime as dt
# import time as tm

# print tm.time()

# dtnow = dt.datetime.fromtimestamp(tm.time())
# print dtnow

# print dtnow.second

# delta = dt.timedelta(days =100)
# print delta

# today = dt.date.today()
# print today - delta
# print today > today-delta

# class Person:
# 	department = 'School of Information' 

# 	def set_name(self, new_name):
# 		self.name = new_name
# 	def set_location(self, new_location):
# 		self.location = new_location

# person = Person()
# person.set_name('Christopher Brooks')
# person.set_location('Ann Arbor, MI, USA')
# print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))

# store1 = [10.00, 11.00, 12.34, 2.34]
# store2 = [9.00, 11.10, 12.34, 2.01]
# cheapest = map(min, store1, store2)

# for item in cheapest:
# 	print(item)

# my_function = lambda a, b, c : a + b
# print my_function(1, 2, 3)

# my_list = []
# for number in range(0, 100):
# 	if number %2 == 0:
# 		my_list.append(number)
# print my_list

# my_list = [number for number in range(1, 1000) if number %2 == 0]
# print my_list

import numpy as np

# mylist = [1, 2, 3]
# x = np.array(mylist)
# print x

# y = np.array([4, 5, 6])
# print y

# m = np.array([[7, 8, 9], [10, 11, 12]])
# print m

# print m.shape

# n = np.arange(0, 30, 2)
# print n
# n = n.reshape(3, 5)
# print n

# o = np.linspace(0, 4, 9)
# print o

# o.resize(3, 3)
# print o

# print np.ones((3, 2))
# print np.zeros((2, 3))

# print np.eye((3))
# print np.diag(y)

# print np.array([1, 2, 3] * 3)

# print np.repeat([1, 2, 3], 3)

# p = np.ones([2, 3], int)
# print p

# print np.vstack([p, 2*p])
# print np.hstack([p, 2*p])

x = np.array(map(float, [1, 2, 3]))
y = np.array(map(float, [4, 5, 6]))

# print (x + y)
# print (x - y)

# print (x * y)
# print (x / y)

# print (x**2)

# print x.dot(y)
z = np.array([y, y**2])
# print(len(z))

# print z.T

# z = z.astype('f')
# print z.dtype

# a = np.array(map(float, [-4, -2, 1, 3, 5]))
# print a.sum()
# print a.max()
# print a.min()
# print a.mean()
# print a.std()

# print a.argmax()
# print a.argmin()

s = np.arange(13)**2
# print s
# print s[0], s[4], s[-1]

r = np.arange(36)
r.resize((6, 6))
print r[2:4,2:4]

# print r[r > 30]

# r[r > 30] = 30
# print r

r2 = r[:3, :3]
# print r2

r2[:] = 0
# print r2
# print r

r_copy = r.copy()
r_copy[:] = 10
# print(r_copy)
# print(r)

# test = np.random.randint(0, 10, (4,3))
# print test 

# for row in test:
# 	print (row)
# for i in range(len(test)):
# 	print(test[i])
# for i, row in enumerate(test):
# 	print('row', i, 'is', row)

# test2 = test**2
# print test2

# for i, j in zip(test, test2):
# 	print(i, '+', j, '=', i+j)