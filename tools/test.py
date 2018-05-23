# coding:utf-8


class Lst(object):
	def __init__(self, i):
		self.i = i

	def add_key(self, j):
		self.i.append[j]

	def get_key(self, num):
		return self.i[num]

	def update_list(self, lst2):
		self.i += lst2

	def del_key(self):
		temp = self.i.pop(len(self.i)-1)
		print self.i
		return temp


demo = [1, 2, 3]
lst = Lst(demo)
p = lst.del_key()
print p
