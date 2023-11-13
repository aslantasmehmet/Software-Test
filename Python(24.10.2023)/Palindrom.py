number_1 = input("Lütfen Bir Sayı Giriniz: ")
number_2 = number_1[::-1]

if(number_1 == number_2):
    print("Palindrom sayıdır.")
else:
    print("Palindrom sayı değildir.")