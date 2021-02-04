# this a calulater build by Nitesh Rauniyar
a= input("Entre your first number:")
a=int(a)
b=input("entre your second number:")
b=int(b)
print('''1 for sum 
2 for subtract
3 for multiply
4 for divide''')

o=input()
o=(int(o))
add = (a+b)
sub = (a-b)
mult = (a*b)
div =(a/b)
if o == 1:
    print(add)
elif o == 2:
    print(sub)
elif o == 3:
    print(mult)
elif o == 4:
    print(div)


