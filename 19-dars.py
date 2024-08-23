# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 09:36:46 2024

@author: Valijon
"""

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
    
# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
    
# salom_ber('hasan')
# salom_ber('olim')

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
    
# toliq_ism('olim', 'jorayev')

# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2024-tugilgan_yil} yoshda")
    
# yosh_hisobla(ism='olim', tugilgan_yil=1995)

# def yosh_hisobla(t_yil, j_yil=2024):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f" Siz {j_yil-t_yil} yoshdasiz")
    
# yosh_hisobla(1995)

#HOMEWORK

# def t_yil(ism, yosh):
#     """Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya"""
#     print(f"{ism.title()} {2024-yosh} yili tug'ilgan ekan.")
    
# t_yil('qodir',37)

# def hisobla(son):
#     """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga, kubi esa {son**3} ga teng ekan.")
    
# hisobla(47)

# def aniqla(son):
#     """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son%2:
#         print(f"{son} toq son ekan.")
#     else:
#         print(f"{son} juft son ekan")
    
# aniqla(888)

# def aytchi('son1','son2'):
#     """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya"""
#     if son1==son2:
#         print("Sonlar teng!")
#     else:
#         print(max(aytchi()))
       
# aytchi(4,12)

# def son(x,y=2):
#     """Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya"""
#     print(f"Siz x sifatida {x} ni, y sifatida {y} ni kiritdingiz")
    
# son(4)

# def aniqla(son):
#     """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son%2:
#         print(f"{son} toq son ekan.")
#     else:
#         print(f"{son} juft son ekan")
        
# aniqla(7777888032)

# def son():
#     """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
#     sonlar = range(2,11)
#     for son in sonlar:
#         son%2
        
#     print(f"")
    
# son(4)

# # Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
# # Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def solishtir(x,y):
#     """Ikki sonni solishtiruvchi funksiya"""
#     if x>y:
#         print(f"{x}>{y}")
#     elif x<y:
#         print(f"{y}>{x}")
#     else:
#         print(f"{x}={y}")

# solishtir(10,20)
# solishtir(-9,12)
# solishtir(1223*5,5**4)

# Foydalanuvchidan son qabul qilib, sonni 2, 3, 4 va 5 ga qoldiqsiz bo'linishini tekshiruvchi 
# funksiya yozing. 
# Natijalarni konsolga chiqaring ("15 soni 3 ga qoldiqsiz bo'linadi" ko'rinishida)
def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)