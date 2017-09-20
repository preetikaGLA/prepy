#generators/list comprehension/lambda/map/filter/reduce
def gen1():
  for i in  range(1,5):
    yield i
    if i%2==0:
      x=i*i
      yield x
g=gen1()
print('g= :',g)
print ('next(g)= :',next(g))
print ('next(g)= :',next(g))


#generator expression
a=(x*x for x in range(1,5))
print('a= :',a)
print ('next(a)= :',next(a))
print ('next(a)= :',next(a))





'''print ('next(g)= :',next(g))
print ('next(g)= :',next(g))
print ('next(g)= :',next(g))
print ('next(g)= :',next(g))
print ('next(g)= :',next(g))
print ('next(g)= :',next(g))
print ('next(g)= :',next(g))














var = 'foo'
def ex3():
    global var
    var = 'bar'
    print 'inside the function var is ', var

ex3()
print 'outside the function var is ', var
'''
'''
def A(a) :
  print(a,"in A() start")
  #a[0]=11
  def B() :
    a[0]=11
    print(a,"changed in B() start")
    def C() :
      #print(a,"in C() start")
      a[0]=12
      print(a,"changed in C() END")
    C()
    #a=4
    print(a,"in B() END")
  B()
  a='hi'
  print(a,"in A() END")
A([1,2])
'''
