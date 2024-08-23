# mehmonlar = ['Aziz', 'Shoxrux', 'Botir', 'Laziz', 'Oltin']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20-oktabr kuni nahorga oshga taklif etamiz")
#     print("Hurmat bilan, Pismadonovlar oilasi\n")
    
# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")


# sonlar = list(range(15))
# sonlar_kv = []
# for son in sonlar:
#     sonlar_kv.append(son**2)
    
# print(sonlar)
# print(sonlar_kv)

# dostlar = []
# print("5 ta eng yaqin do'stingizni kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting:"))

# print("Demak quyidagi insonlar sizning do'stlaringiz ekan:\n", dostlar)

# ismlar = ['Alisher', 'Husniddin', 'Bahodir', 'Valisher', 'Temurxon']
# for ism in ismlar:
#     print(f"{ism} bugun tadbirimiz bor edi. Kelolasanmi?")
    
# k = len(ismlar)
# print(f"Kod {k} marta takrorlandi!")

# t_sonlar = list(range(11,100,2))
# for t_son in t_sonlar:
#     print(f"{t_son} ning kubi {t_son**3} ga teng, bro")

# f_film = []
# print("5 ta eng sevimli kinolaringizni bilmoqchimiz.")
# for n in range(5):
#     f_film.append(input(f"{n+1}-sevimli kinoni kiriting:"))
                        
# print("Demak siz yoqtirgan 5 ta kino quyidagilar ekan:\n", f_film)


n_meeting = int(input("Bugun nechta inson bilan uchrashding?"))
odamlar = []
for n in range(n_meeting):
    odamlar.append(input(f"{n+1}-uchrashgan insoningiz ismini kiriting:\n"))
    
print(odamlar)


# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# print(ismlar)