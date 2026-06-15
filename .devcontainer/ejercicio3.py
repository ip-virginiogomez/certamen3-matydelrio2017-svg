print("¡Bienvenido!")

    
edad=int(input("Ingrese su edad: "))
opcion=int(input("¿Tienes tarjeta de socio? 1.- Si | 2.- No" ))
compra=int(input("Ingrese el monto de su compra: "))
descuento=compra*0.15
totalpago=compra-descuento

if edad>=60 or opcion==1 & compra>=10000:
    print("Eres beneficiario del descuento de 15%")
    print(f"Tu total a pagar es: {totalpago} ")

else:
    print("No eres beneficiario")
    print(f"Tu total a pagar es: {compra} ")



