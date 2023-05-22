#在一个函数内部修改全局变量
a=10
def ax():
    global a
    a=a**a
ax()
print(a)    