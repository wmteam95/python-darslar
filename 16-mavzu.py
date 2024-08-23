# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:55:36 2024

@author: Valijon
"""

# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'matiz',
#         'rang':'qizil',
#         'yil':2020,
#         'narh':10000,
#         'km':40000,
#         'korobka':'mexanik'
#         }

# car2 = {
#         'model':'tracker',
#         'rang':'kulrang',
#         'yil':2023,
#         'narh':52000,
#         'km':10000,
#         'korobka':'avtomat'
#         }

# car = car0
# print(f"{car['model'].title()},"
#       f"{car['narh']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")

# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()},"
#       f"{car['narh']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")
    
# malibus = []
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None,
#         'yil':2020,
#         'narh':None,
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car)
    
# # for malibu in malibus:
# #     print(malibu)
    
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'    

# for malibu in malibus[3:6]:
#     malibu['rang']='qora'  
    
# for malibu in malibus[6:]:
#     malibu['rang']='qora'
#     malibu['korobka']='mexanika'
    
# # for malibu in malibus:
# #     print(malibu)

# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narh']=40000
#     else:
#         malibu['narh']=35000

# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'maryam':['c++','c#']
#     }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())
        
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f'{til.upper()} ', end='')    

hamkasblar = {
    'ali':{'familiya':'valiyev',
            'tyil':1995,
            'malumot':'oliy',
            'tillar':['python','c++']
            },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
              'tyil':1999,
              'malumot':'maxsus',
              'tillar':['python', 'php']}
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
        
# #HOMEWORK
# mashhurlar = {
#     'alisher':{'toliq_ismi':'alisher navoiy',
#                'sohasi':'shoir',
#                't_joyi':'hirot',
#                't_yili':1441,
#                'ijodi':['hamsa', 'lison-ul taym']},
#     'eynshteyn':{'toliq_ismi':'albert eynshteyn',
#                'sohasi':'fizik',
#                't_joyi':'germaniya',
#                't_yili':1879,
#                'ijodi':['qora tuynuk', 'murakkab savollarga oddiy javoblar']},
#     'bobur':{'toliq_ismi':'zahiriddin muhammad bobur',
#                'sohasi':'shoir, podshoh',
#                't_joyi':'andijon',
#                't_yili':1483,
#                'ijodi':['sherlar toplami', 'boburnoma']},
#     'tesla':{'toliq_ismi':'nikolas tesla',
#                'sohasi':'ixtirochi',
#                't_joyi':'avstriya',
#                't_yili':1856,
#                'ijodi':['the current war', 'tesla model G']}
#     }

# for toliq_ismi, info in mashhurlar.items():
#     print(f"\n{info['toliq_ismi'].title()} {info['t_joyi'].title()}da tavallud topgan, "
#           f"{info['t_yili']}-yilda tug'ilgan. "
#           f"Sohasi: {info['sohasi']}. \n"
#           "Quyida mashhur ishlari keltirilgan:")
    
#     for ijod in info['ijodi']:
#         print(ijod.title())

davlatlar = {
    'fransiya':{'joylashuvi':'yevropa',
                'poytaxt':'parij',
                'bosh_tizimi':'respublika'},
    'italiya':{'joylashuvi':'yevropa',
                'poytaxt':'rim',
                'bosh_tizimi':'respublika'},
    'belgiya':{'joylashuvi':'yevropa',
                'poytaxt':'budapesht',
                'bosh_tizimi':'respublika'}
    }

# for davlat, info in davlatlar.items():
#     print(f"Bugun ushbu davlat haqida ma'lumotlarga ega bo'lamiz! \n"
#           f"Davlat nomi: {davlat.title()} \n"
#           f"Joylashgan mintaqasi: {info['joylashuvi'].title()} \n"
#           f"Poytaxti: {info['poytaxt'].title()} \n"
#           f"Boshqaruv shakli: {info['bosh_tizimi'].title()} \n")
    
# ask = input("Qaysi davlat haqida ma'lumot olmoqchisiz? \n")
# for ask in davlatlar:
# if ask in davlatlar:
#     print(ask)