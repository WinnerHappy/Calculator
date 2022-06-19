# for i in range(10):
#     print(i) 

# x = list(range(5,20,))
# for i in x:
#     print(i) 

def sum(x, y):
    return x+y

def mult(x, y):
    return x*y

y= input("Informe um Numero:")
y=int(y)

ope= input("Informe Operador:")

x= input("Informe um Numero:")
x=int(x)

if ope == "+": 
    print("A soma é {}".format(sum(x,y)))
elif ope == "*":
    print("A multiplicacao é {}".format(mult(x,y)))