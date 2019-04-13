sayi=int(input("Bir sayi giriniz:"))
toplam=0
while (True) :
    if (sayi<=0) :
        sayi=int(input("Pozitif bir sayi giriniz"))
    else:
        for i in range(1,sayi) :
            if (sayi%i==0):
                toplam+=i
        break

if(toplam==sayi):
    print("Sayi mükemmel sayidir")
else:
    print("Sayi mükemmel sayi degildir")