import string
import random
if __name__ == '__main__':
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    while(True):
        try:
            plen=int(input("Enter the lenght of your password: "))
            break
        except ValueError as e:
            print("Oops!!, Wrong Input.")
            a=input("Do you want to try again: (y/n): " ).lower()
            if a=='y':
                continue
            else:
                break
#Adding all alphabets,numbers and symbols in the list "s".   
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    print("The auto generted password is: ")
    print("".join(s[0:plen]))
    
    