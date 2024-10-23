wiek = 12
kasa = 40

#zagnieżdzanie ifów
# if wiek >= 18:
#     if kasa >= 35:
#         print("Możesz wejść")

# # #operatory logiczne:
# if wiek >= 18 and kasa >= 35:
#     print("Możesz wejść!")
# else:
#     print("Niestety nie możesz wejść")

# if wiek <= 12 or kasa >= 35:
#     print("Możecie wejść na film dla dzieci")

# #negacja
# if not wiek > 12:
#     print("Nie możecie wleźć")

# #kolejność łączenia warunkow
# if True or False and False: #najpierw się wykonało and a potem or
#     print("Prawda")
# else:
#     print("Fałsz")

##najbezpieczniej obejmować warunki nawiasami
if True and (False or False):
    print('Prawda')
else:
    print('nieprawda')


