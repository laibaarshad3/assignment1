import re
while True:
    l = input("Enter an expression : ")
    n = re.findall("[0-9]+",l)
    az = len(re.findall("[a-zA-Z]",l))
    o = re.findall("['%' , '*' , '/' , '//' , '+' , '\-' , '**']+",l)
    e = len(re.findall("['[' , '}' , ',' , ':' , '{' , '(' , ')']", l))
    if az > 0:
        continue
    elif e > 0: 
        continue
    elif e == 0:
        x = int(n[0])
        y = int(n[1]) 
        z = o[0]
        r = ""
        if z == "+":
            r = x + y
        elif z == "-" :
            r = x - y
        elif z == "*" :
            r = x * y
        elif z == "/" :
            r = x / y
        elif z == "**" :
            r = x ** y
        elif z == "//" :
            r = x // y
        elif z == "%" :
            r = x % y
        else:
            print("invalid input")
        print("ANSWER : " , r)   
    l = input("Press 'no' to end  or 'ENTER' : ")
    if l == 'no' :
        break
    else:
        pass