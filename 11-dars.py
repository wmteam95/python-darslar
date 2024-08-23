# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:58:22 2024

@author: Valijon
"""

# yosh = int(input('Yoshingiz nechida?'))
# if yosh<=4:
#     print('Sizga kirish bepul')
# elif yosh<=12:
#     print('Sizga kirish chiptasi 5000 so\'m')
# else:
#     print('Sizga kirish chiptasi 10 000 so\'m')

# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni!')
# else:
#     print('Bugun ish kuni!')

# kun = input("Bugun nima kun? ")
# harorat = float(input("Havo harorati qanday? "))

# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz ekanda!")
  
# kun = input("Bugun nima kun? ")
# harorat = float(input("Havo harorati qanday? "))
  
# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
#     print("Uyda dam olamiz ekanda!")

# narh = 15000
# choy = True
# salat = True

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
    
# print(f"Jami {narh} so'm")

# narh = 15000
# choy = True
# salat = True
# non = True
# kompot = True
# assorti = True

# if choy:
#     print("Mijoz choy olgan.")
#     narh = narh + 3000
    
# if salat:
#     print("Mijoz salat olgan.")
#     narh = narh + 5000
    
# if non:
#     print("Mijoz non olgan.")
#     narh = narh + 2000
    
# if kompot:
#     print("Mijoz kompot olgan.")
#     narh = narh + 7000

# if assorti:
#     print("Mijoz assorti olgan.")
#     narh = narh + 3000
    
# print(f"Jami {narh} so'm bo'ldi.")

# menu = ['osh', 'somsa', 'manti', 'quymoq']
# ovqat = input('Nima ovqat yeysiz? ')
# if ovqat.lower() not in menu:
#     print('Afsuski boshqa joyda ovqat yer ekansiz')
# else:
#     print('Buyurtmangiz qabul qilindi.')

# menu = ['osh', 'shashlik', 'quymoq', 'lavash', 'bulochka']
# buyurtmalar = ['manti', 'osh', 'bulochka', 'lavash']

# # for taom in buyurtmalar:
# #     if taom in menu:
# #         print(f"Menuda {taom} bor.")
# #     else:
# #         print(f"Kechirasiz, menuda {taom} yo'q")

# if buyurtmalar:
#     print(f"Ro'yxatda {len(buyurtmalar)} ta taom bor")
# else:
#     print("Ro'yxat bo'sh")

# Uyga vazifa
# j_son = range(2,100,2)
# son = int(input('Iltimos, juft son kiriting:'))
# if son in j_son:
#     print("Rahmat")
# else:
#     print("Juft kiriting dedimku")

# yosh = int(input("Yoshingizni kiriting, men sizga chipta narhini aytaman: "))
# if yosh <= 4 or yosh>=60:
#     print("Chipta bepul")    
# elif yosh <= 18:
#     print("Chipta narhi 10 000 so'm")
# else:
#     print("Chipta narhi 20 000 so'm")

# tekshir
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# if a==b:
#     print(f"{a}={b}")
# if a>b:
#     print(f"{a}>{b}")
# if a<b:
#     print(f"{a}<{b}")

# hard
# mahsulotlar = ['sabzi', 'bodring', 'un', 'loviya', 'kakao', 'loviya', 'guruch', 'tuz', 'ogonyok', 'gugurt']
# savat = []
# n = list(range(5))
# for i in n:
#     mahsulot = input(f"{i + 1}-mahsulotni kiriting: ")
#     savat.append(mahsulot)

# for item in savat:
#     if item in mahsulotlar:
#         print("Mahsulot do'konimizda bor")
#     else:
#         print("Boshqa do'konlarni qarab ko'ring")

# can not do

# mahsulotlar = ['sabzi', 'bodring', 'un', 'loviya', 'kakao', 'loviya', 'guruch', 'tuz', 'ogonyok', 'gugurt']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# n = list(range(5))
# for i in n:
#     mahsulot = input(f"{i + 1}-mahsulotni kiriting: ")
#     savat.append(mahsulot)

# for item in savat:
#     if item in savat:
#         savat = bor_mahsulotlar[:]
#     else:
#         savat = mavjud_emas [:]

# foydalanuvchilar = ['admin', 'umid', 'bro', 'bolajon', 'lola']
# kirit = input("Loginni kiriting: \n")
# if kirit in foydalanuvchilar:
#     print("Bunday foydalanuvchi mavjud!")
# else:
#     print(f"Xush kelibsiz, {kirit}")

# bulish = range(2,101,2)
# son = int(input("Butun son kiriting: \n"))
# if son in bulish:
#     print(f"{son/2}")
#     print(f"{son/10}")

son = float(input("Juft son kiriting: "))
if son%2:
    print('Bu son juft emas.')
else:
    print("Rahmat!")