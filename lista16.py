banda = []

print ("Etapa 1:",banda)

banda.append("Jhon Lennon")
banda.append("Paul McCartney")
banda.append("George Harrioson")
print ("Etapa 2:",banda)

for members in range(2):
    banda.append(input("Novo Membro: "))
print("Etapa 3:", banda)

del banda[-1]
del banda[-1]
print("Etapa 4:",banda)

banda.insert(0,"RingoStarr")

print("Etapa 5:", banda)

print("The Fab:", len(banda))
