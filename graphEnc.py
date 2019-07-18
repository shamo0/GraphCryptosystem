#!/usr/bin/env python3

import random

class Vertex:
	def __init__(self, name) :
		self.name = name
		self.first = 0
		self.second = 0

	def __hash__(self) :
		'''This method must be here for Vertex objects to work as keys in a Python
		Dictionary (because Python Dictionaries are just hashtables).'''
		return hash(self.name)

class Graph:
	def __init__(self) :
		'''As with your lab, your graph should be represented as an adjacency list.
		However, here, your keys should be Vertex objects.
		It is VERY IMPORTANT that only one Vertex object with a given name be floating around.
		This is because if you change one object's .first, but there are two such objects, the .first
		will not be changed in the other.
		The fact they both share the same .name is obviously irrelevant.
		Therefore, stringToVertex is a map useful for mapping string names to the single Vertex
		object with that name.
		That same object should appear as a key in adjList, and in the lists which are the values
		 of adjList.
		'''
		self.stringToVertex = dict()
		self.adjList = dict()


	def fromDotFile(self,filename) :
		'''Build Graph from named .dot file provided as argument.
		'''
		fd = open(filename,'r')
		file_read = fd.readline()
		while file_read!="":
			if "{" in file_read:
				file_read = fd.readline()
				continue
			elif "}" in file_read:
				break
			split = file_read.strip(";\t\n").split("--")
			split0 = split[0].strip()
			split1 = split[1].strip()
			# print(self.adjList)
			# if split0 not in self.stringToVertex:
			# 	self.stringToVertex[split0]=Vertex(split0)
			# 	self.adjList[self.stringToVertex[split0]]=[split1]
			# elif split0 in self.stringToVertex:
			# 	self.adjList[self.stringToVertex[split0]].append(split1)
			if split0 not in self.stringToVertex:
				self.stringToVertex[split0]=Vertex(split0)
				self.adjList[split0]=[split1]
			elif split0 in self.stringToVertex:
				if split1 not in self.adjList[split0]:
					self.adjList[split0].append(split1)
			if split1 in self.stringToVertex:
				if split0 not in self.adjList[split1]:
					self.adjList[split1].append(split0)
			else:
				self.stringToVertex[split1]=Vertex(split1)
				self.adjList[split1]=[split0]
			file_read = fd.readline()

	def strToInt(self,msg) :
		msg = int.from_bytes(str.encode(msg,'ascii'), byteorder='big')
		print(msg,"=Encrypted")
		return msg

	def encrypt(self, plaintext) :
		'''Encrypt the plaintext, returning the ciphertext as a single string.
		'''
		'''Assigning Firsts (add up to message)'''
		message = self.strToInt(plaintext)
		sum = 0
		for item in self.stringToVertex:
			int = random.randint(-message,message)
			sum+=int
			self.stringToVertex[item].first=int
			end = item
		sum = sum-self.stringToVertex[end].first
		self.stringToVertex[end].first= message - sum
		sum+= self.stringToVertex[end].first
		'''Assigning Seconds (sum of all adjacents)'''
		for item in self.adjList:
			second = 0
			for key in self.adjList[item]:
				second+=self.stringToVertex[key].first
			self.stringToVertex[item].second = second +self.stringToVertex[item].first
		fdWrite = open("cipher.txt",'w')
		for item in self.stringToVertex:
			string = str(item)+" "+str(self.stringToVertex[item].second)+"\n"
			fdWrite.write(string)

def main() :
	'''main function.
	'''
	testGraph = Graph()
	testGraph.fromDotFile('public.dot')
	testGraph.encrypt('thisisatestmotherfucker')

if ( __name__ == "__main__" ) :
	main()
