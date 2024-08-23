# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 14:52:08 2024

@author: Valijon
"""

# cars_0 = {'model':'jeep', 'rang':'pushti'}
# print(cars_0['rang'])

# talaba_18 = {'ism':'valijon maxmudov', 'yosh':'28', 't_yil':'1995'}

# print(f"{talaba_18['ism'].title()},\
# {talaba_18['t_yil']}-yilda tug'ilgan,\
# {talaba_18['yosh']} yoshda")

# talaba_18['kurs'] = 4
# talaba_18['fakultet'] = 'IT'
# talaba_18['ism'] = 'Qodirxon'

# talaba_1 = {}

# print(talaba_1)

# talaba_1['ism'] = 'odilxon'
# talaba_1['hudud'] = 'qashqadaryo'
# talaba_1['fani'] = 'matematika'

# print(f"Talaba {talaba_1['ism'].title()}ning yashash hududi {talaba_1['hudud'].title()}, o'zi yoqtirgan fani esa {talaba_1['fani']} ekanligini aniqladik.")

# del talaba_1['fani']

# telefonlar = {
#     'mi':'redmi 13 pro',
#     'apple':'iPhone 13 pro max',
#     'samsung':'S24 ultra',
#     'nokia':'1310'
#     }

# phone = telefonlar.get('pixel','Bunday brend bizda mavjud emas!')

# print(phone)

# otam = {'ism':'sharof muratov', 't_yil':'1971', 'kasbi':'inspektor'}

# onam = {'ism':'saodat muratova', 't_yil':'1975', 'kasbi':"o'qituvchi"}

# ukam = {'ism':'umid maxmudov', 't_yil':'2004', 'kasbi':'talaba'}

# print(f"Otamning ismi {otam['ism'].title()}, u kishi {otam['t_yil']}-yilda Sirdaryoda tug'ilgan. Hozirda {otam['kasbi']} bo'lib faoliyat yuritadi.")

# print(f"Onamning ismi {onam['ism'].title()}, u kishi {onam['t_yil']}-yilda Sirdaryoda tug'ilgan. Hozirda {onam['kasbi']} bo'lib faoliyat yuritadi.")

# print(f"Ukamning ismi {ukam['ism'].title()}, u kishi {ukam['t_yil']}-yilda Sirdaryoda tug'ilgan. Hozirda {ukam['kasbi']} bo'lib faoliyat yuritadi.")

# f_food = {
#     'otam':'tandir',
#     'onam':'salat',
#     'ukam':'fastfood'
#     }

# print(f"Otamning sevimli taomi {f_food['otam']},onam esa {f_food['onam']}ni juda yaxshi ko'radi, ukamga esa bir oy {f_food['ukam']} bersangiz ham bezimaydi.")

# python = {
#     'int':'son qiymat kiritilishini taminlaydi',
#     'str':'matn kiritilishini taminlaydi',
#     'get':'lugatlar bilan ishlashda birorta kalitni chaqirishga xizmat qiladi',
#     'del':'keraksiz elementni ochiradi',
#     'float':'onli kasrlar bilan ishlashga yordam beradi',
#     'if':'agar mazmunidagi buyruqlarni yaratadi',
#     'elif':'if va else birikmasi, vazifasi esa if ni davom etish',
#     'in':'royxatda biror elementni borligini tekshirishga yordam beradi',
#     'for':'sikl yaratishda kerak boladi',
#     'anvar':'pythonni organishda yordam beryotgan ustoz'
#     }

#hard homework
# en_uz = {'car':'moshina', 'do':'qilmoq', 'run':'yugurmoq', 'burn':'yoqmoq', 'read':'oqimoq'}

# key = input("Biror so'zni kiriting, men esa sizga uni tarjimasini aytaman:")

# word = en_uz.get(key)

# if word==None:
#     print("Hozircha lug'atimizda bunday so'z mavjud emas!")
# else:
#     print(f"{key} so'zi {word} deb tarjima qilinadi.")
    
# talaba_18 = {'ism':'valijon maxmudov', 'yosh':'28', 't_yil':'1995'}

# for key, value in talaba_18.items():
#     print(f"Kalit: {key}")
#     print(f"Qiymat: {value} \n")
    
telefonlar = {
    'mi':'redmi 13 pro',
    'apple':'iPhone 13 pro max',
    'samsung':'S24 ultra',
    'nokia':'1310'
    }
# for k, q in telefonlar.items():
#     print(f"{k.title()}ga tegishli telefon {q}")

mahsulotlar = {
    'olma': 8000,
    'shaftoli': 10000,
    'uzum': 12000,
    'nok': 15000,
    'banan': 22000,
    'kivi': 22000,
    'apelsin': 15000
    }

# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())


# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
    
# print(mahsulotlar.values())
# print("Do'konimizda quyidagi narxdagi mahsulotlar mavjud:")
# for mahsulot in mahsulotlar.values():
#     print(mahsulot)
    
# print(mahsulotlar.values())
# print("Do'konimizda quyidagi narxdagi mahsulotlar mavjud:")
# for mahsulot in set(mahsulotlar.values()):
#     print(mahsulot)

# cars = {'nissan', 'audi', 'volvo', 'bmw', 'jeep', 'bmw', 'toyota', 'audi'}

python = {
    'int':'son qiymat kiritilishini taminlaydi',
    'str':'matn kiritilishini taminlaydi',
    'get':'lugatlar bilan ishlashda birorta kalitni chaqirishga xizmat qiladi',
    'del':'keraksiz elementni ochiradi',
    'float':'onli kasrlar bilan ishlashga yordam beradi',
    'if':'agar mazmunidagi buyruqlarni yaratadi',
    'elif':'if va else birikmasi, vazifasi esa if ni davom etish',
    'in':'royxatda biror elementni borligini tekshirishga yordam beradi',
    'for':'sikl yaratishda kerak boladi',
    'anvar':'pythonni organishda yordam beryotgan ustoz'
    }

#1_task
# for k, v in python.items():
#         print(f"Atama: {k}")
#         print(f"Mazmuni: {v} \n")

capital = {'USA':'Vasington', 'France':'Paris', 'Italy':'Rome', 'Russia':'Moscow', 'Uzbekistan':'Tashkent'}
# print("There are some countries:")
# for coun in sorted(capital):
#     print(coun.title())
    
# print("\nThere are some capitals:")
# for cap in sorted(capital.values()):
#     print(cap.title())
    
# ask = input("O'zingiz istagan davlatni kiriting: >>>\n")
# if ask in capital:
#     print(f"{ask}ning poytaxti {capital.get(ask)}")
# else:
#     print("Bizda bunday ma'lumot yo'q!")

menu = {'osh':18000, 
        'honim':7000, 
        'manti':8000, 
        'non':5000, 
        'quymoq':4000,
        'baliq':30000,
        'pitsa':35000,
        'kit yuragi':36000,
        'burga oyogi':400000,
        'akula tishi':5000
        }

print("Iltimos, 3 ta taomga buyurtma bering: ")
buyurtma = []

for n in range(3):
    buyurtma.append(input(f"{n+1} ga nima buyurasiz? \n"))

#qilgan xatom: sikl buyurtma bo'yicha aylanishi kerak, men menu bo'yicha qilganim uchun ham xato bajarilgan ekan.

for taom in buyurtma:
    if taom in menu:
        print(f"{taom.title()} {menu[taom]} so'm")
    else:
        print("Bizda bunday taom yo'q")


menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }

# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")