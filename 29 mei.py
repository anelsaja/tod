def faktorial(n):
    if n==0 or n==1:
        return 1
    else:
        return faktorial(n-1) * n

def perkalian(bil1,bil2):
    if bil2==1:
        print("%d = " %(bil1),end='')
        return bil1
    else:
        print("%d + " %(bil1),end='')
        return bil1 + perkalian(bil1,bil2-1)

# def pangkat(bil1,bil2):
#     if bil2==1:
#         print("\%d = " \% (bil1) ,end='')
#         return bil1
#     else:
#         print("\%d * " \%(bil1),end='')
#         return bil1 * pangkat(bil1,bil2-1)
    
def fibo(n):
    f1,f2=1,1
    print(f1,", ",f2,", ",end='')
    for i in range(2,n):
        fib = f1+f2
        f1 = f2
        f2 = fib
        print(fib,", ",end='')

def helloworld(n):
    for i in range(n):
        print("Hello World")
        
def helloworld2(n):
    if n == 0:
        return
    else:
        print("Hello World!")
        helloworld2(n-1)
        
def sumloping(n):
    hasil = 0
    for i in range(1, n+1):
        hasil = hasil + i
    return hasil

def sumher(n):
    return int((1+n) * (n/2))

def reksum(n):
    if n == 1:
        return 1
    else:
        return reksum(n-1) + n
    
def pangkat(x,n):
    # return x**n  
    return pow(x, n) 

def pangper(x,n):
    hasil = 1
    for i in range(1, n+1):
        hasil = hasil * x
    return hasil

def rekpang(x,n):
    if x == 1:
        return 1
    elif n == 1:
        return x
    elif n == 0:
        return 1
    else:
        return rekpang(x,n-1) * x
    
# import timeit

# mulai = timeit.default_timer()
# hasil = rekpang(11,129)
# selesai = timeit.default_timer()
# waktu = selesai - mulai
# print(hasil)
# print(waktu)    

def palindromper(inputstr):
    inputstr = inputstr.lower()
    reversed_input = inputstr[::-1]
    if inputstr == reversed_input:
        return True
    else:
        return False

def palindromrek(inputan, dep, bel):
    a = inputan[dep]
    b =inputan[bel]
    if dep == bel:
        if inputan[dep] == inputan[bel]:
            return True
    elif bel == dep + 1:
        if inputan[dep] == inputan[bel]:
            return True
        else:
            return False
    else:
        if inputan[dep] == inputan[bel]:
            return palindromrek(inputan, dep + 1, bel - 1)
    
def fiboindex(n):
    f1,f2=1,1
    fib = 1
    for i in range(2,n):
        fib = f1+f2
        f1 = f2
        f2 = fib
    return fib
    
def fiborek(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fiborek(n-1)+fiborek(n-2)
    
def fibomem(n, listfibo):
    if n == 1 or n == 2:
        return 1
    else:
        if listfibo[n-1] != 0:
            return listfibo[n-1]
        else:
            listfibo[n-1] = fibomem(n-1, listfibo)+ \
                fibomem(n-2, listfibo)
            return fibomem(n-1, listfibo)+fibomem(n-2, listfibo)

print(fiboindex(20))
print(fiborek(20))
print(fibomem(20, [0]* 20 ))
    
    
    
    
    
# print(palindromper("kasur rusak"))
# kalimat = "kasur rusak"
# print(palindromrek((kalimat.lower()), 0, len(kalimat.lower() - 1)))

    


    
# print(rekpang(3,4))

# print(pangper(3,4))

# print(pangkat(3,4)) 


# print(reksum(17))
    
# print(sumher(17))

# print(sumloping(17))
        
# helloworld(2)

# helloworld2(5)

# fibo(7)

# print(pangkat(2,4))

# print(perkalian(2,4))

# print(faktorial(6))

