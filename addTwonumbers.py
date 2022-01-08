'''
Write a program to add two numbers without using Arthmetic operators
'''

def add(a,b):
    while b!=0:
        carry = a&b
        print(carry)
        a = a^b
        print(a)
        b = carry << 1 
        print(b)
    return a
print(add(8,10))