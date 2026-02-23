#Lists
Material = ["Electric Welding" , "Spot Welding" , "Electric Soldering Iron"]
Numbers = [30,20,10]
empty = []
fl = [ 30.1 , 20.2]
print(Material , Numbers ,empty , fl)
print(Material[2])

#Mutable
Material = ["Drivers" , "Motors"]
Material[1] = "Hello"
print(Material)

Number = [1,2,3,455,6,6]
Number[4] = 55555555555555555555
print(Number)

Components = ["Laptop" , "Mobile", "Cpu"]
Components[2]=  "Hello"
print(Components)

#List Operations
m = [2 , 3]
n = 3
b = m*n
print(b)

M = [2,3,4,5,6,7]*1
print(M)

#ADDITION
N = [9,8,7]
B = [5,43,3]
V = N+B
print(V)


a = [1,2,3]+[1,2,4]
print(a)


#List Slicing
List = ["Hello" , "World", "Pakistan" , "America"]
List2 = List[1:2]
print(List2)
List3 = List[3:]
print(List3)

Num = [10,29,49,56]
print(Num)
Num1 = Num[1:3]
Num2 = Num[2:]
Num4 = Num [ :4]
print(Num1,Num2,Num4)
print(Num[2:3])

#Replacing

Lst = ["qw" , "qw" ,"ER"]
Lst [2:] = ["qw"]
print(Lst)

Lst[0:2] = ["qW" , "qW"]
print(Lst)


#List Methods
Q = ["Hello" , "World" , "Pakistan"]
W = "Gone"
Q.append(W)
print(Q)

R = ["de", "er"]
E = "Hellooooo"
R.append(E)
print(R)

T = ["Error","Error","error"]
Q.extend(T)
print(Q)

Y = ['q','w','e']
U = ['a','b','c']
Y.sort()
print(Y)
Y.append(U)
print(Y)
Y.extend(U)
print(Y)


#Deleting Element
L = ['a','c','v']
x = L.pop(1)
print(L)
print(x)

G = ['a' , 'b ' , 'c']
del G[2]
print(G)

H = ['l' , 'k' , 'h']
H.remove('l')
print(H)

K = ['w','E','r']
del K[:2]
print(K)

#List and Function
Numberss = [1,2,3,4,5,20]
print(len(Numberss))
print(min(Numberss))
print(max(Numberss))
print(sum(Numberss))
print(sum(Numberss)/len(Numberss))

#List and strings
T = 'Country'
Y = list(T)
print(Y)

P = 'Hello Everyone'
O = P.split()
print(O)
print(O[0])

#
I = 'Pragramming-is-a-very-good-thing'
delimiter = '-'
print(I.split(delimiter))

#
i = 'Coding is','very important', 'for programmers'
delimiter = ' '
print(delimiter.join(i))