def doWhileLoop():
    a = 0
    while True:
        print(a)
        a = a+1
        if(a == 10):
            break
    print("Finally finished!")

doWhileLoop()