s=input("enter the string:")

def both_ends(s):
    if len(s)<2:
        return " "
    else:
        return (s[0:2]+s[-2:])



print(both_ends(s)) 
