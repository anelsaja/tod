# # # # # # # range(1,11)
# # # # # # # for i in range(15,30):
# # # # # # #     if i %2 == 0:
# # # # # # #         print(f"{i} genap")
# # # # # # #     else:
# # # # # # #         print(f"{i} ganjil")

# # # # # # def fibo(batas):
# # # # # #     bil1 = 1
# # # # # #     bil2 = 1
# # # # # # # tampilkan dua suku fibonacci pertama
# # # # # #     if bil1 < batas:
# # # # # #         print(bil1, end='\t')
# # # # # #         print(bil2, end='\t')
# # # # # # # suku-suku berikutnya dari bil1 + bil2
# # # # # #     suku_baru = bil1 + bil2
# # # # # #     while suku_baru < batas:
# # # # # #         print(suku_baru, end='\t')
# # # # # # # geser bil1 dan bil2
# # # # # #     bil1 = bil2
# # # # # #     bil2 = suku_baru
# # # # # # # hitung lagi suku berikutnya
# # # # # #     suku_baru = bil1 + bil2

# # # # # # # program utama
# # # # # # batas = int(input('Masukkan batas dari deret fibonacci: '))
# # # # # # fibo(batas)



# # # # # def is_prime(number):
# # # # #     pembagi = 0
# # # # #     for i in range(1, number+1):
# # # # #         if number%i==0:
# # # # #             pembagi+=1
# # # # #     if pembagi==2:
# # # # #         return True
# # # # #     else:
# # # # #         return False

# # # # # prima = int(input("Masukkan bilangan bawah= "))
# # # # # primas = int(input("Masukkan bilangan atas= "))
# # # # # for i in range(prima, primas+1):
# # # # #     if is_prime(i):
# # # # #         print(i)
# # # # #     else:
# # # # #         print('tidak ada hasil')

# # # # range(1,999)

# # # bilangan = 0
# # # genap = False
# # # while genap == False:
# # #     bilangan = int(input('Masukkan bilangan genap: '))
# # #     if bilangan % 2 == 0:
# # #         genap = True
# # # print(bilangan, 'yang anda masukkan adalah bilangan genap')

# import random

# def genarete_angka(bawah, atas):
#     angkakomputer = random.randrange(bawah, atas)
#     return angkakomputer

# langkah=0
# komputer=0

# tebakan = False
# hasil=False
# while tebakan == False:
#     if langkah==0:
#         break
#     bilangan = int(input('Masukkan bilangan: '))
#     langkah=langkah-1
#     if bilangan == komputer:
#         tebakan = True
#         hasil=True
#         break
#     else:
#         if bilangan>komputer:
#             print('terlalu besar, langkah anda sisa', int(langkah))
#         else:
#             print("terlalu kecil, langkah anda sisa", int(langkah))
# if hasil== True:
#     print(bilangan, 'yang anda masukkan adalah bilangan komputer, dengan sisa langkah', langkah)
# else:
#     print('anda kalah')

# # import random

# # print('SELAMAT DATANG DALAM PROGRAM PREDIKSI TOGEL HK HARI INI')
# # print('Prediksi togel hari ini adalah:',{random.randrange(1000,10000)})

def perkalian(bebas, tod):
    hasil=0
    print(f'{bebas}x{tod}= ', end="")
    for i in range(1,bebas+1):
        if i == bebas:
            print(f'{tod} = ', end="")
        else:
            print(f'{tod} + ', end="")
        hasil=hasil+tod
    print(f"{hasil}")

print(perkalian(6,5))


bawah=int(input("Masukkan = "))
atas=int(input("Masukkan = "))

if bawah>atas:
    for i in range(bawah,atas-1,-1):
        if i%2==1:
            if i == atas or i == atas+1:
                print(i)
            else:
                print(i, end=", ")
else:
    for i in range(bawah,atas+1):
        if i%2==1:
            if i == atas or i == atas-1:
                print(i)
            else:
                print(i, end=", ")




