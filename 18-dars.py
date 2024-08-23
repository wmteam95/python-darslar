# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 12:07:30 2024

@author: Valijon
"""

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n=1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash != 'ha':
#         break
    
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
        
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ['lacetti', 'matiz', 'toyota', 'nexia', 'jeep', 'nexia', 'tico']
# car = 'matiz'
# while car in cars:
#     cars.remove(car)
# print(cars)

# students = ['hasan', 'olim', 'yasmina', 'nigora', 'jasur']
# marked_students = {}
# while students:
#     student = students.pop()
#     mark = input(f"{student.title()}ning bahosini kiriting: ")
#     print(f"{student.title()} baholandi!")
#     marked_students[student] = int(mark)

# print("Sizning buyurtmalaringizni qabul qilaman!")
# buyurtmalar = []
# n=1
# while True:
#     savol = f"{n}-buyurtmani kiriting: "
#     zakaz = input(savol)
#     buyurtmalar.append(zakaz)
#     takrorlash = input("Yana buyurtma berasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash != 'ha':
#         break
# print(buyurtmalar)

# savat =[]
# while True:
#     mahsulot = input("Savatga mahsulot qo'shing:")
#     savat.append(mahsulot)
#     javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
#     if javob != 'ha':
#         break



# e_bozor = ['olma', 'non', 'bulochka', 'kola', 'shakar']
# mah_narhlari = {}
# while e_bozor:
#     bozor = e_bozor.pop()
#     narh = input(f"{bozor.title()}ning bahosini kiriting: ")
#     mah_narhlari[bozor] = int(narh)
    
# while True:
#     if buyurtmalar in e_bozor:
#         print(f"{zakaz} bizda mavjud!")
#     else:
#         print("Bizda bunday mahsulot yo'q!")
        
# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")

