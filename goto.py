def goto(label):
    if label == "display":
        print("This is 5.")

def loopWithGoto():
    a = 0
    while(a < 10):
        if(a == 5):
            goto("display")
            break
        print(a)
        a += 1
    print("Finally finished!")

loopWithGoto()