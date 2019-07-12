#!/usr/bin/env python3
import sys

def main():

    cipherTextFd = open(sys.argv[1],"r")
    privateTextFd = open(sys.argv[2],"r")

    dictCipher = {}
    cipherTextRead = cipherTextFd.readline()
    while cipherTextRead!= "":
        split = cipherTextRead.split(" ")
        dictCipher[split[0].strip()] = split[1].strip()
        cipherTextRead = cipherTextFd.readline()

    sum = 0
    privateTextRead = privateTextFd.readline()
    while privateTextRead!="":
        if privateTextRead.strip() in dictCipher:
            sum+=int(dictCipher[privateTextRead.strip()])
        privateTextRead = privateTextFd.readline()
    print(intToStr(sum))

def intToStr(daInt) :
  b = daInt.to_bytes((daInt.bit_length() // 8)+1, byteorder='big')
  str = b.decode('ascii')
  return str

main()
