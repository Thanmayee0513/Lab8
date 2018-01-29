def fix_start(s):
    a=s[0]
    b=s[1:]
    if a in b:
      result= b.replace(a,"*")
      return (a+result)


print(fix_start("babble"))
