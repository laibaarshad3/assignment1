import re
while True:
    l = input("enter the expression : ")
    n = re.findall("[0-9]+" , l)
    az = len(re.findall("[a_zA_Z]" , l))
    o = re.findall("['+' , '\-' , '/'  , '//' , '*' , '**' , '%']+" , l)
    e = len(re.findall("['(',')','[',']','{','}',',',':']",l))
    if az > 0:
        continue
    elif e > 0:
        continue
    elif e == 0:
        
        x = int(n[0])
        y = int(n[1])
        z = o[0]
        re = ""
        if z == '+':
            re = x + y
        elif z =='-':
            re = x - y
        elif z == '/':
            re = x / y
        elif z == '//':
            re = x // y
        elif z =='*':
            re = x * y
        elif z == '**':
            re = x ** y
        elif z == '%':
            re = x % y
        else:
            print("invalid syntax : ")
        print("ANSWER : " , re)
        
        user = input("Press 'no' to end and 'yes' to continue : ")
        if user == 'yes':
            continue
        elif user == 'no':
            break