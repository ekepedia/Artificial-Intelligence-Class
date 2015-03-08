##################################################################
# Eke Wokocha                                                    #
# November 29 , 2014                                             #
# Period 4                                                       #       
# Program Description: Make Trie Class                           #
################################################################## 

class Node(object):

	def __init__ (self, value):
		self.value		= value
		self.children 	= {}

	def __repr__(self):
		self.print('')
		return ''

	def print(self, stng):
		for key in self.children.keys():
			if key == '$':
				print(stng)
			else:
				stng1 = stng + self.children[key].value
				self.children[key].print(stng1)

	def display(self):
		if self.value == '$': return
		print('=====NODE=====')
		print('---> self.value		=', self.value )
		print('---> self.children:	[', end='')

		for key in self.children:
			if key != '$':
				print(key, sep='',end=', ')
		print(']')
		print('--------------')

		for char in self.children:
			(self.children[char]).display()

	def insert(self, stng):
		if stng == '':
			self.children['$'] = Node('$')
			return
		stng = stng.lower()
		while( ord(stng[0]) < 97 or ord(stng[0]) > 122 ):
			stng = stng[1:]
		if(stng[0] in self.children.keys() ):
			self.children[stng[0]].insert(stng[1:])
			return
		else:
			newNode = Node(stng[0])
			self.children[stng[0]] = newNode
			newNode.insert(stng[1:])
			return

	def search(self, stng):
		if (len(stng) == 0):
			return '$' in self.children.keys()
		elif(stng[0] in self.children.keys()):
			return self.children[stng[0]].search(stng[1:])
		return False
		
def main():
	root = Node('*')
	root.insert('cat')
	root.insert("can't")
	root.insert('cats')
	root.insert('catnip')
	print(root.search('cat'))
	print(root.search('ca'))
	print(root)

if __name__ == '__main__':
    from random import random, randint; from math import sqrt; from copy import deepcopy;
    from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+')
    print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')