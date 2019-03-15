fact=1
while True :
    print("Bir sayi giriniz :")
    sayi=int(input())
    if sayi<=0 :
        print("Sayi negatiftir..")
    else:

        for i in range(1,sayi+1):
             fact*=i

        print("Faktoriyel hesabi",fact)

    break