import re

# handle =  open(input("masukkan:"), "r")
# handle = handle.read()
# x = re.sub("Menurut", "-", handle) #mengganti spasi dengan -
# print(x)
# print()
# y = re.sub("Dimas", "*", handle, 2) #mengganti spasi dengan * 2 saja
# print(y)
# import re

def bacatulis(txt):
    handle =  open(txt, "r")
    handle = handle.read()
    return handle

def regex(artikel):
    pattern = r"\b[A-Za-z][a-z][a-z][a-z][a-z]\b"
    hasil = re.findall(pattern, artikel)
    return hasil

# file = input("nama file:")
# artikel = bacatulis(file)
# # print(artikel)
# hasil = regex(artikel)
# print(hasil)\

def email(gmail):
    hasil = gmail.split("@")
    hasil = tuple(hasil)
    return hasil

def emrex(gmail):
    pattern = r"(.+)@(.+)"
    hasil = re.search(pattern, gmail)
    return hasil

def replace(lama, baru, artikel):
    artikel = re.sub(lama, baru, artikel)
    return artikel

def update(file, hasil):
    handle = open(file, "w")
    handle.write(hasil)
    handle.close()

# gmail = input("masukkan email:")
# hasil = email(gmail)
# print(emrex(gmail))

# print(f"username: {hasil[0]}")
# print(f"hostname: {hasil[1]}")

file = input("nama file:")
artikel = bacatulis(file)
# print(artikel)
lama = input("masukkan kata ingin direplace: ")
baru = input("masukkan barunya: ")

hasil = replace(lama,baru, artikel)

update(file, hasil)
print(file)

