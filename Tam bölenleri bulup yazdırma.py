sayi=int(input("Please enter a number:"))

k=0
while (True) :
    if(sayi<=0):
        sayi=int(input("Please enter a positive number:"))
    else:
        dizi = []
        for i in range(1,sayi+1):
            if(sayi%i==0) :
                dizi.append(i)
                k+=1
        break


for j in range(0,k):
    print(dizi[j])