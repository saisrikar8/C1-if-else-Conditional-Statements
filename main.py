'''
01/25/2021
__________________________________________
#Homework-data types

name = input("Enter your name:")
age = input("Enter you age:")
drink = input("Enter your favorite drink:")
grade = input("Enter your grade:")

print("I am " + name + "\nI am " + age + " years old. \nMy favorite drink is" + drink + ".\nI am " + grade + "grade.")

print("hi\t|\tbye")
__________________________________________

Review-Operators
1. Math Operators(Arithmetic Operators)
addition, +
subtraction, -
multiplication, *
division, /(Exact answer)
division, //(Quotient integer)
modulo, %(remainder)
exponents, **

5/2 = 2.5
5//2 = 2
5%2 = 1

9%10 = 9
8%2 = 0

2. Assignment Operators
= Assignment
+= Addition Operators
-= Subtraction Assignment
/=, Division Assignment
//=, quotient assignment
%=, Modulo Assignment
**= exponent assignment

Rule:

a=0
a+= 4 >> a=a+4

3 Compaison Operators
  == equal to
  != not equal to 
  < less than
  <= less than or equal to
  > greater than
  >= greater than or equal to

  5==4 False
  6>= 4 True
  0 != int("0")

  if(Condition):
    Indentation required
  else:
    BODY


'''
a=21

if(a%3 != 0): #21 % 3 = 0
  print("hi")

else:
  print("Bye")
