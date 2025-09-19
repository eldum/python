hNumero = int(input("número de chicos:"))
mNumero = int(input("número de chicas:"))

Total = hNumero + mNumero

hporcentaje = hNumero / Total * 100
mporcentaje = mNumero / Total * 100

print(f"El porcentaje de hombres es {hporcentaje:.2f} % y el de mujeres es {mporcentaje:.2f} %")