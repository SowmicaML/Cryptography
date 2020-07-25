#python program to implement caesar cipher
import sys
#encrypt func
def encrypt(str,shift):
    res=""
    for char in str:
        if(char == ' '):
            continue
        if(char.isupper()):
            res += chr(((ord(char)+shift-65)%26)+65)
        else:
            res += chr(((ord(char)+shift-97)%26)+97)
    return res

#decrypt func
def decrypt(str,shift):
    res=""
    for char in str:
        if(char == ' '):
            continue
        if(char.isupper()):
            res += chr(((ord(char)-shift-65)%26)+65)
        else:
            res += chr(((ord(char)-shift-97)%26)+97)
    return res

print("CAESAR CIPHER")
while(1):
    choice=int(input("\n1.encrypt text\n2.decrypt text\n"))
    if choice==1:
        string=input("enter plain text: ")
        shift=int(input("shift ?"))
        print("cipher text: ",encrypt(string,shift))
    elif choice==2:
        string=input("enter cipher text: ")
        shift=int(input("shift ?"))
        print("plain text: ",decrypt(string,shift))
    else:
        exit()


