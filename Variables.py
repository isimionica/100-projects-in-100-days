#input function 
print(len(input()))

#Write a program that switches the values stored in the variables a and b.
# There are two variables, a and b from input
a = input()
b = input()
#need to create a third variable to help switch the values
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)