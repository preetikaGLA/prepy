#BCA question paper
def a(*arg):
    count=len(arg)
    sum=0
    if(count<2):
        print("ERROR")
    else:
        for i in range(0,count):
            sum+=arg[i]
        avg=sum/count
        print("sum:",sum)
        print("avg:",avg)

a()
a(1)
a(1,2,3,4)
a(-1,3,5,-2)
    



'''from __future__ import print_function, division


def do_twice(func, arg):
    func(arg)
    func(arg)


def print_twice(arg):
    print(arg)
    print(arg)


def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print_twice, 'spam')
print('')

do_four(print_twice, 'spam')
'''
