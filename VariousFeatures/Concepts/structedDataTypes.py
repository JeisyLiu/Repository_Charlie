import os
import subprocess

dic_alpha={
    "alpha":[1,2,3,4],
    "bravo":"standby",
    3:["boya","kokodayo"],
    4:[5,6,7,8],
    'd':5
}

list_alpha = [1, 2, 3, 4, 5]
list_bravo = ['c', 'h', 'e', 'e', 'r']

tuple_alpha = (6, 7, 8, 9, 0)
tuple_bravo = ('a', 'e' ,'i', 'u', 'o')
'''lambda express'''
lam = lambda x : x**3

def my_func_double(func,arg):#this is NOT a pure function
    return func(func(arg))

def func(x):
    return x*2

def my_func_trible(f,arg):
    return f(f(f(arg)))


format_alpha="the format string: {0},{1},{0}".format("apples","butter")
print(format_alpha)
print("2333".join(["bravo","charlie","delta"]))
print(lam(3))
print(my_func_trible(lambda x : 2*x, 5))
print(my_func_double(func, 5))
print("this is a map"+str(list(map(lam,list_alpha))))#the first para of map can be a func or lambda express
print("this is a filter" + str(list(filter(lambda x:x %2 == 0,list_alpha))))#the first para of filter must be a judgement   