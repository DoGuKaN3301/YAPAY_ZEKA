# bir değişkenin değerini değiştirmek için
toplam = 0
toplam = toplam + 1   # toplam değişkenin değerini 1 arttıyor
toplam = toplam + 2   # toplam değişkenin değerini 2 arttıyor
toplam += 4           # toplam değişkenine 4 ekler
toplam -= 7           # toplam değişkeninden 7 çıkarır

print(toplam)

print ("Doğukan\n"*5)  # 5 defa alt alta doğukan yazar \n new line yani alt satıra geç
print (125)

# döngüler
# for döngüsü
for i in range(5):  #[0,1,2,3,4] bu şekilde bir liste oluşturuyor ,i değişkenin değerinin 0 dan başlar 5 sayı ileri gider
  print(125) # kod bloğu

# 1 ile 10 arasında ki sayıları yazdır
for i in range(10):
   print(i + 1) # kod bloğu

# 1 ile 10 arasında ki sayıları yazdır range değişkeni ile
for i in range(1,11):  # range parantez içinde ilk yazdığımız hangi sayıdan başlaması gerekrtini , 2. sayı ise nerede biteceği
  print(i) # kod bloğu


# range komutu
# 1 ile 10 arasında ki sayıları yazdır
for i in range(1,11 , 2 ):  # burada ki 2 sayısı 2 arttıracağını belirtiyor
  print(i) # kod bloğu




# range komutu
# 1 ile 10 arasında ki sayıları yazdır
for i in range(11 , 1 , -2 ):  # burada ki 2 sayısı -2 çıkaracağını belirtiyor
  print(i) # kod bloğu





toplam = 0               # toplam değişkenini 0 a eşitler.
for i in range(7 , 20):  # 7 den 19 a kadar 1 arttırır.
  toplam += i            #i ile toplam değişkenini topla ( bir çeşit i değişkenini saklama)
print(toplam)            # toplam değişkenini yazdırır
# for döngüsünün kod bloğunun her bir çalıştırılmasına yineleme denir.





# 10 ile 3 arasıdaki tek sayıları yan yana yazıdrmak istersek
toplam = 0
for i in range(10 , 2, -1):
    if i % 2 != 0:

      print(i, end =" ")
toplam +=i






# for döngüsü özellik
# bir kelimedeki sesli harfleri ekrana yazma
for i in "mahir":
  if i.lower() in "aeiıoöuü":
    print(i)




# for döngüsü özellik
# bir kelimedeki sesli harflerin sayısı
sesliharf = 0
for i in "mahir":
  if i.lower() in "aeiıoöuü":
    sesliharf +=1
print(sesliharf,"şu kadar tane sesli harf vardır")






# kullanıcıdan parola alan ve doğru girerse tebrik eden kod
parola = "şafak"
for i in range(3):
  giris=input("parolayı giriniz ")
  if giris == parola:
      print("parolayı bildiniz ")
      break
  else:
       print(2-i," hakkınız kaldı")


#girilen bir sayısının faktörüyelini hesaplama
hsp = 1
sayi = int(input("bir sayı giriniz:"))
for i in range(sayi , 0 ,-1):
# for i in range(1 , sayi+1):
  hsp *= i
print(sayi , "! = ", hsp)


# WHİLE DÖNGÜSÜ
# while koşul
#   while kod bloğu

# 1 ile 100 arasında sayı girilene kadar kullanıcıdan sayı girsin
sayi = int(input("sayi giriniz"))
while sayi<0 or sayi>100:
  sayi = int(input("1 ile 100 arasında sayi girdiniz"))


# kullanıcı bye diyene kadar kullanıcan sayı isteyiniz
while True:
  cevap=input("çıkış için bye yazınız ").lower()
  if cevap == "bye":
    break
  #else:
  #  cevap = int(cevap)

while input("çıkış için bye yazınız ").lower() =="bye ":
  pass
