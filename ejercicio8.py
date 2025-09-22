notas = []

for i in range(3):
    numero = float(input("nota->"))
    if numero >4:
        notas.append(numero)
aprobadas = len(notas) 
    
if aprobadas ==0:
    print("0 patatero")
elif aprobadas <3 and aprobadas>0:
    print("Tienes un 2")
else:
   nota_final = nota_final = notas[0]*0.3 + notas[1]*0.2 + notas[2]*0.5
   print(f"de nota final tines un {nota_final}") 
    
