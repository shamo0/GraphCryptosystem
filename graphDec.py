#!/usr/bin/env python3
'''
      Author: Genadi Shamugia
       Alpha: 216126
        Date: July 18, 2019
Program Name: Decryption
Program Description:
    Program takes ciphertext and privatetext as arguments and decrypts the
    message.
'''
import sys

def main():
    if len(sys.argv) !=3: #Check if number of arguments is 3
        print("Usage: graphDec.py [ciphertext] [privatetext]")
        exit()

    cipherTextFd = open(sys.argv[1],"r") #Open ciphertext file
    privateTextFd = open(sys.argv[2],"r") #open privatetext file

    dictCipher = {}
    cipherTextRead = cipherTextFd.readline() #read cipher Text line by line
    while cipherTextRead!= "":
        split = cipherTextRead.split(" ")
        dictCipher[split[0].strip()] = split[1].strip()
        cipherTextRead = cipherTextFd.readline()

    sum = 0
    privateTextRead = privateTextFd.readline() #read private text line by line
    while privateTextRead!="":
        if privateTextRead.strip() in dictCipher:
            sum+=int(dictCipher[privateTextRead.strip()])
        privateTextRead = privateTextFd.readline()
    print(intToStr(abs(sum)))

def intToStr(daInt) :
    b = daInt.to_bytes((daInt.bit_length() // 8)+1, byteorder='big')
    str = b.decode('ascii')
    return str

main()
