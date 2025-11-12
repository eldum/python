saldo = 100
monto = int(input("retirar ->"))

print(f"tu saldo es de {saldo}€")
while monto >0:
    try:
        if monto > saldo:
            print("no tienes tanto para retirar")
        else:
            if monto % 10 == 0:
                saldo -= monto
                break
            else: 
                print("tiene que ser divisible entre 10")
        monto = int(input("retirar ->"))
    except:
        print("tiene que ser mayor que 0")
        
print(saldo)
