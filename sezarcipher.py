ciphercharsen_A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphercharsen_a = "abcdefghijklmnopqrstuvwxyz"
print("\n1--->ENCODE\t2--->DECODE\n")
select = int(input("Enter the number in front of the operation you want: "))
if select ==1:
    text = input("Enter Text: ")
    key = int(input("Enter Key Number: "))
    textready = []
    cipher_text = ""
    for i in text:
        textready.append(i)

    for j in textready:
        if j.isalpha():
            if j.isupper():
                k = ciphercharsen_A.index(j)
                k+=key
                if k >=26:
                    k=k%26
                cipher_text += ciphercharsen_A[k]
            if j.islower():
                k = ciphercharsen_a.index(j)
                k+=key
                if k>=26:
                    k=k%26
                cipher_text +=ciphercharsen_a[k]
        else:
            cipher_text += j
    print("Cipher Text: ",cipher_text)
    
if select == 2:
    ciphertext = input("Enter Cipher Text: ")
    key = int(input("Enter Key Number: "))
    textready = []
    text = ""
    for i in ciphertext:
        textready.append(i)
    for j in textready:
        if j.isalpha():
            if j.isupper():
                k = ciphercharsen_A.index(j)
                k-=key
                if k <0:
                    k=26+k
                text += ciphercharsen_A[k]
            if j.islower():
                k = ciphercharsen_a.index(j)
                k-=key
                if k<0:
                    k=26+k
                text +=ciphercharsen_a[k]
        else:
            text += j
    print("Cipher Text: ",text)

