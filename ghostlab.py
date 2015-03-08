##################################################################
# Eke Wokocha                                                    #
# November 29 , 2014                                             #
# Period 4                                                       #       
# Program Description: Win Ghost Game                            #
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
	
def quitHuman(case,stng,currentNode,player):
	print("\nGAME OVER,",player, " YOU LOSE!")
	if case:
		print("You spelled a word!", stng)
	else:
		print(stng, "does not being any word!")
		print("By the way, the word I was think of was", stng[0:-1] + spellWord(currentNode))
	exit()

def quitComputer(case,stng,currentNode):
	print("\nGAME OVER, YOU WIN!")
	if case:
		print("I spelled a word!", stng)
	else:
		print(stng, "does not being any word!")
		print("By the way, the word I was think of was", stng[0:-1] + spellWord(currentNode))
	exit()

def requestandCheckHumanMove(currentNode,stng, player):
	print(player, end = "")
	char = input(', enter your character.').lower()[0]
	if not char in currentNode.children.keys():
		quitHuman(0,stng+char,currentNode,player)
	currentNode = currentNode.children[char]
	if '$' in currentNode.children.keys() and len(stng) > 2: #human spelled word greater than 3
		quitHuman(1,stng+char,currentNode,player)
	return char

def requestandCheckComputerMove(currentNode,stng):
	char = ''
	tempSol = None
	for key in currentNode.children.keys():
		tempNode = currentNode.children[key]
		if not '$' in tempNode.children.keys():  #make sure the computer doesn't spell a word
			if len(spellWord(currentNode))%2:    #check if there exist a word of odd length
				char = tempNode.value
				break
			else:
				tempSol = key                   #if there exist a even word, not an perfect choice
	else:
		if tempSol:
			char = tempSol
		else:
			char = key
	if not char in currentNode.children.keys():
		quitComputer(0,stng+char,currentNode)
	currentNode = currentNode.children[char]
	if '$' in currentNode.children.keys() and len(stng) > 2:
		quitComputer(1,stng+char,currentNode)
	return char

def spellWord(currentNode):
	stng = ''
	while True:
		char = list(currentNode.children.keys())[0]
		if char == '$':
			return stng
		stng += char
		currentNode = currentNode.children[char]

def main():
	root = Node('*')
	file1 = open('GhostDictionary.py')
	for word in file1:
		root.insert(word.lower().strip())
	file1.close()
	stng = ''
	while True:
		char = requestandCheckHumanMove(root,stng,"player 1")
		stng += char
		root = root.children[char]
		char = requestandCheckHumanMove(root,stng, "player 2")
		stng += char
		root = root.children[char]
		char = requestandCheckComputerMove(root,stng)
		stng += char
		print("Okay, I'll guess", char)
		print("\nNow the current fragment is:\t\t",stng)
		root = root.children[char]


if __name__ == '__main__':
    from random import random, randint; from math import sqrt; from copy import deepcopy;
    from time import clock; START_TIME = clock(); main(); print('\n      +===<RUN TIME>===+')
    print('      |  %5.2f'%(clock()-START_TIME), 'seconds |'); print('      +================+')