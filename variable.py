x = 10
def count():
    x = 2
    x += 1
    print("Local ", x)

count()
print("Global: ", x)

def count1():
    global x
    x += 1
    print("Global", x)
count1()
print("Global: ", x)

def f1():
    x=10
    def f2():
        nonlocal x
        x+=1
        print("Non Local: ",x)
    f2()
    print("NonLocal: ", x)
f1()
