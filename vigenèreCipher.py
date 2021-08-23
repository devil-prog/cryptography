alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt():
    txt = input("Enter the text: ")
    KEY = input("Enter key: ")
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

    for i in range(txti):
        x = alpha.index(out[i])
        y = alpha.index(txt[i])
            
        k = int(x+y)

        try:
            if k > 25:
                output = (output + alpha[k-26])
            else:
                output = (output + alpha[k])
        except UnboundLocalError:
            if k > 25:
                output = alpha[k-26]
            else:
                output = alpha[k]

    print(f"Encrypted: {output}\n\n")

def decrypt():
    print("1. With key \n2. Without key \nEnter your choice")
    i =  int(input())
    def dc1():
        KEY = input("Enter key: ")
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
        
        for i in range(txti):
            x = alpha.index(out[i])
            y = alpha.index(txt[i])

            k = int(y-x)

            try:
                output = (output + alpha[k])
            except UnboundLocalError:
                output = alpha[k]

        print(f"Decrypted: {output}\n\n")

    def dc2():
        #bruteforce
        BKEY = open('keys.txt','r').read().split('\n')
        for i in range (len(BKEY)):
            KEY = BKEY[i]
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
            
            for i in range(txti):
                x = alpha.index(out[i])
                y = alpha.index(txt[i])

                k = int(y-x)

                try:
                    output = (output + alpha[k])
                except UnboundLocalError:
                    output = alpha[k]

            print(output)
            output = ''

    
    if i == 1:
        txt = input("Enter Encrypted text: ")
        dc1()
    elif i == 2:
        txt = input("Enter Encrypted text: ")
        dc2()

def start():    
    print(f"{alpha}")


    print("1. Encrypt \n2. Decrypt \nEnter your choice")
    i = int(input())

    if i == 1:
        encrypt()

    elif i == 2:
        decrypt()
while True:
    start()