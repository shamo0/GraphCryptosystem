#!/usr/bin/env python3

class Vertex:
	def __init__(self, name) :
		self.name = name
		self.first = 0
		self.second = 0

	def __hash__(self) :
	'''This method must be here for Vertex objects to work as keys in a Python Dictionary (because Python Dictionaries are just hashtables).
	'''
	return hash(self.name)

class Graph:
	def __init__(self) :
	'''As with your lab, your graph should be represented as an adjacency list.
	However, here, your keys should be Vertex objects.
	It is VERY IMPORTANT that only one Vertex object with a given name be floating around.
	This is because if you change one object's .first, but there are two such objects, the .first will not be changed in the other.
	The fact they both share the same .name is obviously irrelevant.
	Therefore, stringToVertex is a map useful for mapping string names to the single Vertex object with that name.
	That same object should appear as a key in adjList, and in the lists which are the values of adjList.
	'''
		self.stringToVertex = dict()
		self.adjList = dict()

	def fromDotFile(filename) :
	'''Build Graph from named .dot file provided as argument.
	'''
		fd = open(file,'r')
        file_read = fd.readline()
        while file_read!="":
            if file_read.startswith("graph"):
                file_read = fd.readline()
                continue
            elif file_read.startswith("}"):
                break
            split = file_read.strip(";\t\n").split("--")
            split0 = split[0].strip()
            split1 = split[1].strip()
            if split0 not in self.stringToVertex:
                self.stringToVertex[Vertex(split0)].adjList.append(split1)
            elif split0 in self.stringToVertex:
                self.stringToVertex[split0].adjList.append(split1)
            file_read = fd.readline()

	def encrypt(self, plaintext) :
	'''Encrypt the plaintext, returning the ciphertext as a single string.
	'''
		...

def main() :
	'''main function.
	'''
	...

if ( __name__ == "__main__" ) :
	main()
