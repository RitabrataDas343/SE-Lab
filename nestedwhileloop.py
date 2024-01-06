def nestedWhileLoop():
    a, b = 0, 0
    while(a < 10):
        print(a)
        a += 1
        if (a == 5):
            while(b < 5):
                print(b)
                b += 1
    print("Finally finished!")

nestedWhileLoop()