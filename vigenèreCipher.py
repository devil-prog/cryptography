def encrypt():
    txt = input()
    KEY = input()
    keyi = len(KEY) - 1
    txti = len(txt)

    j = 0
    for i in range(txti):
        if i == 0:
            out = KEY[j]
        else:
            out = (out + KEY[j])
        j = j+1
        if j > keyi:
            j = 0

    print('working..')

def decrypt():
    print("1. With key \n2. Without key \nEnter your choice")
    def dc1():
        KEY = input()
        keyi = len(KEY) - 1
        txti = len(txt)
        j = 0
        for i in range(txti):
            if i == 0:
                out = KEY[j]
            else:
                out = (out + KEY[j])
            j = j+1
            if j > keyi:
                j = 0
        
        print(out)


        print("working..")
    def dc2():
        print("Working..")
    
    i =  int(input())
    if i == 1:
        txt = input()
        dc1()
    elif i == 2:
        txt = input()
        dc2()
    


print("1. Encrypt \n2. Decrypt \nEnter your choice")
i = int(input())

if i == 1:
    encrypt()

elif i == 2:
    decrypt()