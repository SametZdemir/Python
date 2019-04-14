def geo(kenar,x="Bilgi yok",y="Bilgi yok",z="Bilgi yok",k="Bilgi yok"):


 if kenar==3:
     if((x==y)and(x==z)):
         print("Bir eskenar ücgendir")
     elif(x==y)or(y==z)or(x==z):
         print("İkizkenar ücgendir")
     else:
         print("Cesitkenar ücgendir")
 elif kenar==4 :
     if(x==y)and(x==z):
         print("Karedir...")
     elif((x==y)and (z==k))or((x==z)and(y==k))or((x==k)and(y==z)):
         print("Dikdörtgendir...")
     elif(x==y)or(x==k)or(x==z):
         print("Girdiginzi kenar uzunlukları çok saçma")
     else:
         print("Çesitkenar dörtgendir...")




dizi=[]
kenar=int(input("Kaç kenar olacak :"))

for i in range(0,kenar):
   k=int(input("Uzunlugu giriniz:"))
   dizi.append(k)


if kenar==3:
    geo(kenar,dizi[0],dizi[1],dizi[2])

elif(kenar<3):
    print("Bir geometrik sekil belirtmez...")
elif(kenar==4):
    geo(kenar,dizi[0],dizi[1],dizi[2],dizi[3])
else:
    print("Cok fazla algoritma var kendin yap :)")
