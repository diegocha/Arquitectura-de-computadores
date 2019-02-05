exponente = int(input("Ingrese el numero del exponente: "))
mantisa = int(input("Ingrese el numero de la mantisa: "))
binario = input("Ingrese el numero binario: ")

def rangototal(mantisa, exponente):
    mantisa1 = mantisa   
    mantisa2 = 0 
    rango = []
    sesgo = 2**(exponente-1)
    sesgox = sesgo
    while (sesgox != (-sesgo)):
        if(mantisa1>0):
            aNegativos = -(2-(
                2**-mantisa1))*(2**sesgox)
            rango.append(aNegativos)
            mantisa1 -= 1
        if(mantisa1==0):
            aNegativos = -(2**sesgox)
            rango.append(aNegativos)
            sesgox -= 1
    
    long = len(rango)
    rangoPos = []
    for i in range(long-1,-1,-1):
        rango1 = -rango[i]
        rangoPos.append(rango1)

    rango.extend(rangoPos)   
    return rango 
    
lista1 = rangototal(mantisa,exponente)
print(lista1)
print(len(lista1))

    