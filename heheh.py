# genap = (2, 2, 4, 5)
# genap = set(genap)
# print(genap)
# print(genap.add("3,8,0"))

data = [1,5,7,8,3,7,3,7,4,7,8,3]
unik = set()
hasil = []
for i in data:
    # if i in unik: #cara 1
    #     continue
    # else:
    #     unik.add(i)
    if i not in hasil: #cara 2
        hasil.append(i)
print(hasil)
# print(data.count[7])

for n in data: #cara 3
    unik.add(n)
print(list(unik))

print(data.pop())
print(data)
print(5 in data)
# print(data.clear())

merek_hp = {'Samsung', 'Apple', 'Xiaomi', 'Sony'}
merek_ac = {'LG', 'Samsung', 'Panasonic', 'Daikin', 'Sony'}
# union dari merek_hp dan merek_ac
gabungan = merek_hp | merek_ac
print(gabungan)

renang = {'siti', 'mail', 'ikhsan', 'upin', 'ipin'}
tenis = {'joko', 'mail', 'ipin', 'upin', 'tejo'}
# suka renang dan tenis
renang_tenis = renang & tenis
print(renang_tenis)

# bisa berbahasa english
english = {'desi', 'tono', 'evan', 'miko', 'takashi', 'chaewon'}
# bisa berbahasa korea
korean = {'chaewon', 'yeona', 'erika', 'miko'}
# siapa yang hanya bisa bahasa korea?
only_korean = korean - english
print(only_korean)
# siapa yang hanya bisa bahasa english?
only_english = english - korean
print(only_english)

english = {'desi', 'tono', 'evan', 'miko', 'takashi', 'chaewon'}
korean = {'chaewon', 'yeona', 'erika', 'miko'}
# hanya bisa bicara satu bahasa saja
one_language = english ^ korean
print(one_language)

def unique_sum(list):
# ubah dalam bentuk Set
    data_set = set(list)
# hitung jumlah seluruh anggota data_set
    total = 0
    for data in data_set:
        total = total + data
# return hasil akhir
    return total
# contoh penggunaan fungsi unique_sum()
contoh1 = [2, 4, 3, 2, 7, 8, 6, 4, 5, 5]
hasil1 = unique_sum(contoh1)
print(hasil1)

def cek_duplikat(string):
# buat set kosong
    karakter_set = set()
# cek semua karakter dalam string satu-persatu
    for karakter in string:
# apakah karakter ini ada dalam set?
        if karakter in karakter_set:
# ternyata ada, berarti duplikat
# hentikan pengecekan, langsung return
            return True
        else:
# jika belum ada, masukkan dalam set
            karakter_set.add(karakter)
# setelah looping semua karakter, tidak ada yang sama
    return False
# test case
string1 = 'Alexander the Great' # duplikat
print(cek_duplikat(string1))
string2 = 'UKDW' # semua unik
print(cek_duplikat(string2))

# input n kategori
n = int(input('Masukkan jumlah kategori: '))
# siapkan dictionary kosong
data_aplikasi = {}
# input nama kategori dan aplikasi di dalamnya
for i in range(n):
    nama_kategori = input('Masukkan nama kategori:')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
# siapkan list kosong untuk nama-nama aplikasi
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
# masukkan dalam dictionary
    data_aplikasi[nama_kategori] = aplikasi
# tampilkan dictionary data_aplikasi
print(data_aplikasi)
daftar_aplikasi_list = []
# ambil semua daftar aplikasi dari setiap kategori
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))
print(daftar_aplikasi_list)
# lakukan intersection ke semua set yang ada
hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])
print(hasil)


import random

print(random.randrange(1000, 10000))
