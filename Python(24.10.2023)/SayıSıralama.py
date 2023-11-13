x = input("Lütfen Bir X Sayısı Giriniz:")
y = input("Lütfen Bir Y Sayısı Giriniz:")
z = input("Lütfen Bir Z Sayısı Giriniz:")


if(x>y and x>z):
    print("En Büyük Sayı X:",x),
elif(y>x and y>z):
    print("En Büyük Sayı Y:",y),
else:
    print("En Büyük Sayı Z:",z)
