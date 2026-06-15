vel=[50,20,140,80,200]


promedio=vel(sum)/vel(len)
print("la velocidad maxima fue: ", vel(max))
print("el promedio de velocidad es: ", promedio)

if all(60>=v<=120 for v in vel):
    print("Estan dentro de lo permitido")