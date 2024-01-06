def loopWithBreak():
    a = 0
    while(a < 10):
        if(a == 5):
            break
        print(a)
        a += 1
    print("Finally finished!")

loopWithBreak()