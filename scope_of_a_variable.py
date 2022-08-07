"""local scope
value can be accessed inside the function only"""
# def fun():
#     x=7;y=8;z=9
#     print(x+z)
# fun()

"""global scope of a variable , can be accessed by anyone"""
# a=2
# def bm():
#     a=4
#     b=3;c=5
#     print(a)
#     print(b)
# print(a)
# bm()
# print(a)

"""global is the keyword , which is need to be specified if we want to use
the local variables as global variables"""
# c=4
# def fun1():
#     a=3
#     global c,b
#     b=8 ; c=9
    # print(b)
# print(c)
# fun1()
# print(c)
# print(b)
# print(c)

"""count the length of the string without using built-in function"""
# def fn(st):
#     c=0
#     for in st:
#         c+=1
#     return c
# print(fn('python'))

"""a guy having multiple names"""

# def sc():
#     school='john'
#     print(f'name in school is {school}')
# def cl():
#     college='max'
#     print(f'name in college is {college}')
#     wk()
# def wk():
#     work='peter'
#     print(f'name at work location is {work}')
#     sc()
# cl()



 

