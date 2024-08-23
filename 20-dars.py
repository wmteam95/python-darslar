# # -*- coding: utf-8 -*-
# """
# Created on Wed Aug 14 09:53:37 2024

# @author: Valijon
# """

# # def toliq_ism_yasa(ism, familiya):
# #     """To'liq ism qaytaruvchi funksiya"""
# #     toliq_ism = f"{ism.title()} {familiya.title()}"
# #     return toliq_ism
    
# # talaba = toliq_ism_yasa('ali', 'valiyev')

# # def toliq_ism_yasa(ism, familiya):
# #     """To'liq ism qaytaruvchi funksiya"""
# #     toliq_ism = f"{ism.title()} {familiya.title()}"
# #     return toliq_ism
    
# # talaba1 = toliq_ism_yasa('ali', 'valiyev')
# # talaba2 = toliq_ism_yasa('samad', 'kamolov')
# # print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# # print(f"{talaba2} darsga kechikib keldi, {talaba1} esa darsda shovqin qildi.")

# # def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
# #     """To'liq ism qaytaruvchi funksiya"""
# #     if otasining_ismi:
# #         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
# #     else:
# #         toliq_ism = f"{ism} {familiya}"
# #     return toliq_ism.title() 
   
     
# # talaba1 = toliq_ism_yasa('ali', 'valiyev')
# # talaba2 = toliq_ism_yasa('samad', 'kamolov', 'adayevich')
# # print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# # print(f"{talaba2} darsga kechikib keldi, {talaba1} esa darsda shovqin qildi.")

# # def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
# #     avto = {'kompaniya':kompaniya,
# #             'model':model,
# #             'rang':rangi,
# #             'korobka':korobka,
# #             'yil':yili,
# #             'narh':narhi}
# #     return avto

# # avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat',2018)
# # avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 15000)
# # avtolar = [avto1, avto2]
# # print('Onlayn bozordagi mavjud avtomashinalar:')
# # for avto in avtolar:
# #     if avto['narh']:
# #         narh = avto['narh']
# #     else:
# #         narh = "noma'lum"
# #     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# # def oraliq(min, max):
# #     sonlar = []
# #     while min<max:
# #         sonlar.append(min)
# #         min += 1
# #     return sonlar

# # print(oraliq(30, 70))
# # print(oraliq(400, 700))

# #HOMEWORK_DONE
# # def oraliq(min, max, qadam=1):
# #     sonlar = []
# #     while min<max:
# #         sonlar.append(min)
# #         min += qadam
# #     return sonlar

# # print(oraliq(0, 10, 2))

# # list(range(0,10,2))

# # def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
# #     avto = {'kompaniya':kompaniya,
# #             'model':model,
# #             'rang':rangi,
# #             'korobka':korobka,
# #             'yil':yili,
# #             'narh':narhi}
# #     return avto

# # print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# # avtolar = []
# # while True:
# #     print("\nQuyidagi ma'lumotlarni kiriting:", end='')
# #     kompaniya=input("\nIshlab chiqaruvchi: ")
# #     model=input("\nModeli: ")
# #     rangi=input("\nRangi: ")
# #     korobka=input("\nKorobka: ")
# #     yili=input("\nIshlab chiqarilgan yili: ")
# #     narhi=input("\nNarhi: ")
    
# #     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
# #     javob=input("Yana avto qo'shasizmi? (yes/no): ")
# #     if javob=='no':
# #         break
# # print("\nSalonimizdagi avtolar:")
# # for avto in avtolar:
# #     if avto['narh']:
# #         narh = avto['narh']
# #     else:
# #         narh = "noma'lum"
# #     print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}")
    
# def user_info(ismi, familiya, yoshi, t_yil, t_joy, email=None, tel=None):
#     user = {'ismi':ismi,
#             'familiya':familiya,
#             'yoshi':yoshi,
#             't_yil':t_yil,
#             't_joy':t_joy,
#             'e-mail':email,
#             'tel':tel}
#     return user

# print("Saytimizdagi foydalanuvchi haqida ma'lumotni shakllantiramiz.")
# userlar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:", end='')
#     ismi=input("\nIsmi: ")
#     familiya=input("\nFamiliyasi: ")
#     yoshi=input("\nYoshi: ")
#     t_yil=input("\nTug'ilgan yili: ")
#     t_joy=input("\nTug'ilgan joyi: ")
#     email=input("\nElektron pochtasi: ")
#     tel=input("\nTelefon raqami: ")
    
#     userlar.append(user_info(ismi, familiya, yoshi, t_yil, t_joy, email=None, tel=None))
#     javob=input("Yana foydalanuvchi qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# print(f"\nFoydalanuvchi ma'lumotlari: {user_info}")
