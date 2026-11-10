import random
import ast

shift = random.randint(1, 26)
asciiUpper = range(65, 91)
newAsciiUpper = random.sample(asciiUpper, 26)

def encrypt():
    newText = ""
    text = input("Massage that gets encrypted: ")
    for c in text:
        nc = ord(c)
        nc += shift
        if(nc > 90):
            nc -= 26
        if nc in asciiUpper:
            newText += chr(newAsciiUpper[asciiUpper.index(nc)])
    return newText

def decrypt():
    newText = ""
    key = input("Key eingeben: ")
    n = 4
    hexList = [key[i:i+n] for i in range(0, len(key), n)]
    joined ="".join(hexList)
    parts = joined.split("0x")
    keyList = [int(p, 16) for p in parts if p]
    print(keyList)
    KeyListM = keyList[:-1]
    shift = keyList[-1]
    newAsciiUpper = [int(e/shift) for e in KeyListM]
    print(newAsciiUpper)
    print(shift)
    text = input("Massage that gets decrypted: ")
    for c in text:
        nc = ord(c)
        if nc in newAsciiUpper:
            nc = (asciiUpper[newAsciiUpper.index(nc)])
            nc -= shift
        if(nc < 65):
            nc += 26
        newText += chr(nc)
    return newText

def keygen():
    keyList = []
    for e in newAsciiUpper:
        e *= shift
        e = hex(e)
        keyList.append(e)
    keyList.append(hex(shift))
    key ="".join(map(str, keyList))
    return(key)

ed = input("e/d: ")
if(ed == "e"):
    print(encrypt())
    print(keygen())
elif(ed == "d"):
    print(decrypt())



    



