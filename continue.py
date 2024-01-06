def loopWithContinue():
    a = 0
    while(a < 10):
        if(a == 5):
            a += 1
            continue
        print(a)
        a += 1
    print("Finally finished!")

loopWithContinue()