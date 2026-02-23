#Strings
print("Hello World!") #simple
print("Hello 'World'")
print("I am doing my bacholers in Mechatronics Engineering at UETP!")
print("Pakistan is a country.")

#assign to variable.
x = "Hello"
print(x)

#variable string and also finding the data type.
a = "Artifial Intelegence is a good field."
print(a)
print(type(a))

z = "AI is very fast growing field in todays world"
print(z)
print(type(z))

#multiline string with three quaotations.
m = """I am a Student at UET Peshawar
I am doing my Bacholers in Mechatronics
I have done my Fsc in Pre-engineering."""
print(m)
print(type(m))

#simple string
print("Google")
print("hello")

#single quotation.
print('I am living in Pakistan!')
print('I am currently in Pakistan!')

n = 'Hello Pakistan'
print(n)
print(type(n))


c = '''Hello, I am Abdullah.
I am eager to learn about Robotics and Automation!'''
print(c)
print(type(c))


#for finding the length of the string.
j = "Hello Pakistan"
print(j)
print(len(j))

t = 'World is full of meaningfull people'
print(t)
print(len(t))
print(type(t))

q = '''World is very big,
everyone here earn for themselves
not for anyone else'''
print(q)
print(len(q))
print(type(q))


#check if not incluse, (Not in)
k = "HEllo World"
print("Pakistan" not in k)


p = "kkkkkkkkkkkkkkk"
print("mmmmmmm" not in p)

#combining 2 strings using +
name = 'Hello'
Last = 'lamb'
Full = name + " " + Last
print(Full)


#Character

U = "Coder World"
print(U[0])
print(U[1])
print(U[5])
print(len(U))


#slicing

Y = "programmers"
print(Y[1:6])
print(Y[5:6])
print(Y[4:6])
print(len(Y))
print(type(Y))

#Modifing
o = "program development"
print(o.lower())
print(o.upper())
print(o.replace("P" , "W"))


#For concatenation or Combinations of string
Q  = "This is Coding"
W  = "App development"
E  = Q+W
R  = Q+""+W
print(E)
print(R)
print(type(R))

#Format String
q = 50
txt = f'I am {q}'
print(txt)
td = f"HEllo{q:.2f}"
print(td)
tg = f"Hello{q:.3f}"
print(tg)
dm = 56
print(f"I am {dm}")