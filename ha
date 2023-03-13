# # def pagarvertikal(n):
# #     for i in range(n):
# #         print('#')

# # def pagarhorizontal(n):
# #     for i in range(n):
# #         print('#', end='')
# # n=int(input('masukkan n = '))
# # #tampilkan # sejumlah n secara vertikal


# # pagarvertikal(n)
# # pagarhorizontal(n)

# def persegitod(n):
#     for i in range(n):
#         for j in range(n):
#             print('|', end='')
#         print()

# n=int(input('masukkan n = '))
# persegitod(n)

# def segitigakiri(n):
#     for baris in range(1, n+1):
#         for kolom in range( 1, baris+1):
#             print('%', end="")
#         print()

# n=int(input('masukkan n = '))
# segitigakiri(n)

# def segitigakanan(n):
#     for baris in range(1, n+1):
#         spasi = n-baris
#         pagar=baris
#         for kolomspasi in range(spasi):
#             print(' ', end="")
#         for kolompagar in range(pagar):
#             print('#', end="")
#         print()
        

# n=int(input('masukkan n = '))
# segitigakanan(n)

# def persegibolong(n):
#     for baris in range(n):
#         print('@', end="")
#     print()
#     for baris in range(n-2):
#         spasi=n-2
#         print('@', end="")
#         for klm in range(spasi):
#             print(' ', end="")
#         print('@')
#     for baris in range(n):
#         print('@', end="")
#     print()


# n=int(input('masukkan n = '))
# persegibolong(n)

# def x(n):
#     for baris in range(n):
#         for kolom in range(n):
#             if baris==kolom:
#                 print('%', end="")
#             elif baris + kolom==n-1:
#                 print('%', end="")
#             else:
#                 print(' ', end="")
#         print()
        

# n=int(input('masukkan n = '))
# x(n)

# def plus(n):
#     for baris in range(n):
#         for kolom in range(n):
#             if baris== n//2:
#                 print('tod', end="")
#             elif kolom==n//2:
#                 print('tod', end="")
#             else:
#                 print(' ', end="")
#         print()
        
# n=int(input('masukkan n = '))
# print("Tanda SALIB =")
# plus(n)

def kampret(n):
    for baris in range(1, (n//1)+1):
        pagar = 2*baris-1
        spasi = (n-pagar)//2
        for i in range(spasi):
            print(' ', end="")
        for i in range(pagar):
            print('#', end="")
    for baris in range((n//2)-1, 0, -1):
        pagar = 2*baris-1
        spasi = (n-pagar)//2
        for i in range(spasi):
            print(' ', end="")
        for i in range(pagar):
            print('#', end="")


n=int(input('masukkan n = '))
print("Tanda SALIB =")
kampret(n)


