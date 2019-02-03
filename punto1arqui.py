
def caracterAEntero(c):
    if (c == "0"):
        return 0
    if (c == "1"):
        return 1
#    return 0



exponente = int(input("Ingrese el numero de bits del exponente: "))
mantisa = int(input("Ingrese el numero de bits de la mantisa: "))
numRead = str(input("Ingrese el número: \n"))

entero = [0]*exponente
decimal = [0]*mantisa

if (len(numRead)<=0):
    print("Error leyendo el numero")

digitos = [None]*len(numRead)
for i in range(0,len(numRead)):
    digitos[i] = numRead[i]
print(digitos)

if digitos[0] == 0:
    signo = +1
else:
    signo = -1

digitos.pop(0)

pos = 0
for k in range(0,len(digitos)):
    if (k==exponente):
        pos = 0
    if (k<exponente):
        entero[pos] = caracterAEntero(digitos[k])
    else:
        decimal[pos] = caracterAEntero(digitos[k])
    pos = pos + 1

print(signo)
print(entero)
print(decimal)

# resEntero = 0    
# for i in range(exponente-1,-1,-1):
#     resEntero = resEntero + (entero[i] * (1 << (exponente - (i + 1))))
# print(resEntero)

# resDecimal = 0
# for i in range(0,mantisa):
#     exp = (1 << (i + 1))
#     res = 1/exp
#     resDecimal = resDecimal + (decimal[i] * res)

# valor = signo*(resEntero + resDecimal)    
# print("El resultado es %f \n" % valor)
