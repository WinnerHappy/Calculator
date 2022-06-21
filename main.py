# for i in range(10):
#     print(i) 

# x = list(range(5,20,))
# for i in x:
#     print(i) 

def sum(x, y):
    return x+y

def mult(x, y):
    return x*y

def sub(x, y):
    return x-y

def div(x, y):
    return x/y

x= input("Informe um Numero:")
x=int(x)

ope= input("Informe Operador:")

y= input("Informe um Numero:")
y=int(y)

if ope == "+": 
    print("A soma é {}".format(sum(x,y)))

elif ope == "*":
    print("A multiplicacao é {}".format(mult(x,y)))

elif ope == "-":
    print("A subtracao é {}".format(sub(x,y)))

elif ope == "/":
    print("A divisao é {}".format(div(x,y)))