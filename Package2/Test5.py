from Package1 import Test1
#from Package1 import *

Test1.m1()              #fn call -> ModuleName.fn()
Test1.m2()


d1=Test1.Demo1()            #Object Creation -> ModuleName.className()
d1.m3()
d1.m4()


Test1.Demo1().m3()          #methodCall -> ModuleName.className().methodName()

