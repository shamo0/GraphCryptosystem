# GraphCryptosystem

## Encryption
  Program builds a graph using a dot file. The encrypted plaintext is turned
	into an integer('message'). We assign a random number to all the vertices in the graph
	such that the sum of all the numbers equals the 'message'. The second number for every
	vertex is the sum of its own first and the first of all adjacent vertices. Then
	we turn the vertices and their second values into a ciphertext which can only be decrypted
	given the private key.
  
## Decryption
   Program takes ciphertext and privatetext as arguments and decrypts the message.
