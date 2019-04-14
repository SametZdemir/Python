def kökbulma(a,b,c):
    delta=b*2-4*c*a
    if (delta<0):
        print("Reel kök bulunamadı...")
        return
    else:
        x1=(-b+delta**0.5)/2*a
        x2=(-b-delta**0.5)/2*a
        return (x1,x2)

x=int(input("Denklemin a sını girin:"))
y=int(input("Denklemin b sını girin:"))
z=int(input("Denklemin c sını girin:"))

sonuc=kökbulma(x,y,z)
print(sonuc)