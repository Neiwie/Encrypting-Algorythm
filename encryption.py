import random
import base64

shift = random.randint(1, 224)
ascii = range(32, 256)
newAscii = random.sample(ascii, 224)
GREEN = "\033[92m"
RED   = "\033[91m"
CYAN  = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def encrypt():
    newText = ""
    text = input(f"{CYAN}Message that gets encrypted: {RESET}")
    for c in text:
        nc = ord(c)
        if nc in ascii:
            nc += shift
            if(nc > 255):
                nc -= 224
            newText += chr(newAscii[ascii.index(nc)])
        else:
            newText += chr(nc)
    return base64.b64encode(newText.encode("latin-1")).decode()

def decrypt():
    newText = ""
    key = input(f"{CYAN}Key eingeben: {RESET}")
    n = 4
    hexList = [key[i:i+n] for i in range(0, len(key), n)]
    joined ="".join(hexList)
    parts = joined.split("0x")
    keyList = [int(p, 16) for p in parts if p]
    shift = keyList[-1]
    newAscii = [int(e/shift) for e in keyList]
    text = input(f"{CYAN}Message that gets decrypted: {RESET}")
    text = base64.b64decode(text).decode("latin-1")
    for c in text:
        nc = ord(c)
        if nc in newAscii:
            nc = (ascii[newAscii.index(nc)])
            nc -= shift
            if nc < 32:
                nc += 224
            newText += chr(nc)
    return newText

def keygen():
    keyList = []
    for e in newAscii:
        e *= shift
        e = hex(e)
        keyList.append(e)
    keyList.append(hex(shift))
    key ="".join(map(str, keyList))
    return(key)

def encdecBase64():
    text2 = input("Text: ")
    ed2 = input("e/d: ")
    if ed2 == "e":
        return base64.b64encode(text2.encode("latin-1")).decode()
    else:  
        return base64.b64decode(text2).decode("latin-1")

print(f"{GREEN}Encrypt and Decrypt Text{RESET}")
ed = ""
while True:
    ed = input(f"{CYAN}What do you want to do? encrypt(e) | decrypt(d) | exit(x): {RESET}")
    match ed:
        case "e" | "E" | "encrypt" | "Encrypt":
            print(f"{GREEN}Encrypted Message:\n{encrypt()}{RESET}")
            print(f"{YELLOW}Key:\n{keygen()}{RESET}")
        case "d" | "D" | "decrypt" | "Decrypt":
            print(f"{GREEN}Decrypted Message:\n{decrypt()}{RESET}")
        case "base64":
            print(encdecBase64())
        case "x" | "X" | "exit" | "Exit":
            break;



    



