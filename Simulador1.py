import aleatorio
CANTP=input("INGRESE LA CANTIDAD DE NUMEROS A GENERAR : ")
CANTP=int(CANTP)
contador=0
while contador <= CANTP:
    VARIABLE= aleatorio.aleatorio(0.006944,0.0013889)
    print(VARIABLE)
    contador=contador+1
