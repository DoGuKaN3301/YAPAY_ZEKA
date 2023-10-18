# Değişkenler
# içerisinde veri sakladığımız bellek birimidir
# 1 - Değer - İsim - Tür

name = "Doğukan" # değerin türü string olduğu için tırnak içinde yazdık
print(name)      # çıktı olarak doğukan yazar

#  1-Türkçe karakter karakter kullanılmaz
#  2-Değişken isimleri rakam ile başlayamayız
#  3-kullanılabileceğimiz tek özel karakter alt tire _
#  4-Python'a özgü anahtar kelimeler kullanılmaz ( or , and , print , not )



# Geçersiz değişken adları
# yaş = 30              türkçe karakter olduğu için 
# kitap sayısı = 15     arada boşluk olduğu için
# 1vize = 50            değişkenlerin başında rakam olmaz


yas = 30
kitap_sayisi = 15
vize1 = 90
sehir = "mersin"
maas = 5000.10
avagadro_sayisi = 6.02*10**-23
avagadro_sayisi = 6.02e-23
# değerde *10** gibi bir değer varsa onun yerine "e" yazmamız yeterli
seviyor_mu = False 
ogrenci_mi = "E"


yas = 30
vizem = 90
kitap_sayisi=15
sehir = "mersin"
print(yas,"yaşındayım", "ilk vizem" , vizem, "aylık olarak" , kitap_sayisi , "kitap okuyorum" , sehir ,"de", "yaşıyorum")
# çıktısı 
# 30 yaşındayım ilk vizem 90 aylık olarak 15 kitap okuyorum mersin de yaşıyorum



# kullanıcıdan değer okuma
isim = str(input("adınızı giriniz "))
yas = int(input("yaşınızı giriniz ")) #yas değişkenini int türüne çeviryor
boy = int(input("boyunuzu giriniz ")) # boy değişkenini int türüne çeviriyor

print ("hoşgeldin" ,isim ) # yukarıda input aldığımız isim değişkenini burada kullanıyor 
print ("yaşınız: " , yas )  # yukarıda input aldığımız yas değişkenini burada kullanıyor 
print ("boyunuz :" , boy )    # yukarıda input aldığımız boy değişkenini burada kullanıyor 

# çıktısı

#yarı çapı istenen çemberin çveresini hesaplayan kod
pi = 3.14
yaric= int(input("yarı çapı giriniz "))
cevre= 2*pi*yaric
print( "yarı çapı" , yaric , "olan cemberin çevresi" , cevre, "dir")



# vize ve final notlarını hesaplayıp geçme notunu hesaplama
vize1 = int(input("vize notunuzu giriniz "))
final1 = int(input("final notunu giriniz "))
gn = (vize1*40/100)+(final1*60/100)
print("geçme notunuz",gn,"dir")



# koşullu ifadeler
# if koşul :
  #koşul doğruysa


# örnek
yas=int(input("yaşınızı giriniz: "))
if yas >=18 :
        print("ehliyet alabilir")
if yas <18:
        print("ehliyet alamaz")





# koşullu ifadeler  else kullanımı
# örnek
yas=int(input("yaşınızı giriniz: "))
if yas >=18 :
        print("ehliyet alabilir") # girilen yaş eger 18 den büyükse ehliyet alabilir ekrana yazar
else:
        print("ehliyet alamaz")  # girilen yaş eger 18 den büyükse ehliyet alamaz ekrana yazar




# kullanıcıdan bilmecenin cevabını alıp dpoğruysa tebrik edin
# .upper harfleri hepsinin büyük yazar
cevab=input("çarşıdan aldım 1 tane eve geldim 1000 tane , cevabı nedir? ").upper()
if cevab=="NAR":
  print("tebrikler bildiniz...")
else:
  print("yanlış bildiniz...")




# elif koşullu kullanımı
# yukarıdaki koşul doğru değilse ve biz başka bir koşulu daha kontrol etmek istiyorsak kullanılır
# notları 0 ile 40 arasında olan öğrencilerin FF 40 ile 60 arasında olan CC 60 ile 100 arasında AA yazsın

vize1 = int(input("vize notunuzu giriniz "))
final1 = int(input("final notunu giriniz "))
gn = (vize1*40/100)+(final1*60/100)
if gn>=0 and gn<=40:
    print("HARF NOTUNZ FF - GEÇME NOTUNUZ",gn,"dir")
elif gn<=60:
  print("HARF NOTUNZ CC - GECME NOTUNUZ" , gn ,"dir")
elif gn>=60:
  print("HARF NOTUNZ AA - GEÇME NOTUNZ",gn,"dir")


#dolmuşa binen kişiler para üstü verecek öğrenci olup olmadığın bakacak
ogr=input("öğrencimisin ? evet - hayır ".lower()) # .lower tüm harfleri kücültüyor
para=int(input("kaç tl var"))

if ogr=="evet":
  if para < 10:
    print("yetersiz bakiye")
  else:
    print("para üstünüz" ,para-10)
elif ogr=="hayır":
  if para < 15:
    print("yetersiz bakiye")
  else:
    print("para üstünüz " ,para - 15)




